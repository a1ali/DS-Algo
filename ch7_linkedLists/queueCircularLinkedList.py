class CircularQueue:
    '''Queue implementation using circular linked list for storage.'''

    class _Node:
        '''lightweight nonpublic class for storing a singly linked node.'''
        __slots__ = '_element', '_next'
        def __init__(self,element,next):
            self._element = element
            self._next = next 

    def __init__(self):
        '''create an empty queue'''
        self._tail = None #will represent the tail of the queue
        #we do not need to store the head becuase we can retrieve it with _tail._next 
        self._size = 0 #number of elements in the queueu 
    
    def __len__(self):
        '''return the size of the queue'''
        return self._size 

    def is_empty(self):
        '''return true if the queue is empty '''
        return self._size == 0

    def first(self):
        '''return but do not remove the first element in the queue 
        raise exception if the queue is empty'''
        if is_empty():
            Empty('The queue is empty')
        return self._tail._next._element #the head's element which is the next of the tail 

    def dequeue(self):
        '''remove and return the first element in the queue
        raise exception if the queue is empty.'''
        if is_empty():
            Empty('The queue is empty')

        oldhead = self._tail._next #the old head after the tail 
        if self._size == 1: #if removing only 1 element in the queueu
            self._tail = None
        else:
            self._tail._next = oldhead._next #this is the element after the head so self._tail._next._next 
        self._size -= 1 
        return oldhead._element #return the old heads element  
    
    def enqueue(self, e):
        '''add an element to the back of queue.'''
        newest = self._Node(e, None) #create an node with initailly no next 
        if self.is_empty():
            newest._next = newest #this gives circularity the node points to itself
        else:
            newest._next = self._tail._next #the new nodes next will become the old tails next which is the head
            self._tail._next = newest #make the old tails next be the new node 
        self._tail = newest #make the newest become the current tail 
        self._size += 1 

    def rotate(self):
        '''rotate front element to back of the queue.'''
        if is_empty():
            Empty('The queue is empty')
        self._tail = self._tail._next #old head becomes new tail 
