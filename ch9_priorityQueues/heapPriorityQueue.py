class HeapPriorityQueue(PriorityQueueBase): #inherit the base class that was defined in priorityQueue.py
    '''A min-oriented priority queue implemented with a binary heap.'''

    #non-public methods 

    def _parent(self, j):
        return (j-1)//2 
    
    def _left(self, j):
        return 2*j + 1 
    
    def _right(self, j):
        return 2*j + 2 

    def _has_left(self, j):
        return self._left(j) < len(self._data) #is the index beyond end of list

    def _has_right(self, j):
        return self._right(j) < len(self._data) #similar to above 

    def _swap(self, i, j):
        '''swap the elements at indices i and j of array'''
        self._data[i], self._data[j] = self._data[j], self._data[i]
    
    def _upheap(self, j):
        '''upheap is a way of adding a new element to our tree
        we initially place the new element in the bottom and then recursively 
        check if we should move it up the tree to place it in the right order '''
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j ,parent)
            self._upheap(parent) recursion on the parent element 

    def _downheap(self, j):
        '''down heap is a similar method like uphead, but here we are initially removing
        the root element and trying to replace it with the appropriate element. So 
        once the element is removed take elements in the bottom of the tree and place it as root 
        and then move it down to appropriate position by swapping.
        '''
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right #the right element is the smallest 
            if self._data[small_child] < self._data[j]:
                self._swap(j , small_child)
                self._downheap(small_child) #recursion to keep moving the element up the tree

    
    #public behavior 
    def __init__(self):
        '''create an new empty Priority Queue.'''
        self._data = []

    def __len__(self):
        '''return the number of items in the priority queue.'''
        return len(self._data)

    def add(self, key, value):
        '''add a key value pair to the priority queue'''
        self._data.append(self._item(key, value))
        self._upheap(len(self._data) - 1) #upheap newly added position 

    def min(self):
        '''return but do not remove (k,v) tuple with minimum key.
        raise exception if emtpy
        '''
        if self.is_empty():
            raise Empty('Priority queue is empty')
        item = self._data[0]
        return (item._key, item._value)
    
    def remove_min(self):
        '''remove and return (k,v) tuple with minumum key.
        raise emtpy exception if empty'''
        if self.is_empty():
            raise Empty('Priority queue is emtpy')
        self._swap(0, len(self._data) - 1) #put minimum item at the end 
        item = self._data.pop() #remove the min item we just swapped (pop removed last element)
        self._downheap(0) #then fix the root element that we just placed
        return (item._key, item._value)


'''we can even use priority queues to sort a collection of elements'''
def pq_sort(C):
    '''sort a collection of elements stored in a positional list.'''
    n = len(C)
    P = SortedPriorityQueue()
    for j in range(n):
        element = C.delete(C.first())
        P.add(element, element) #the element will be both the key and value

    for j in range(n):
        (k,v) = P.remove_min()
        C.add_last(v) 