'''

FIFO (First in First out) implementation of a queue using circular lists
when we deque an element and want to advance the front index use the 
arithmetic f = (f + 1) % N where N is the size of the list


'''

class ArrayQueue:
    '''Fifo queue implementatio using a Python list as underlying storage.'''
    DEFAULT_CAPACITY = 10 #queue size

    def __init__(self):
        '''create an empty queue.'''
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY 
        self._size = 0 #current size of the queue (number of elements present)
        self._front = 0 #init the front to be 0

    def __len__(self):
        '''Return teh number of elements in the queue.'''
        return self._size 
    
    def is_empty(self):
        '''return true if the queue is empty.'''
        return self._size == 0 

    def first(self):
        '''return but do not remove the element at the front of the queue.
        raise an exception if the queue is empty.'''
        if self.is_empty():
            raise Empty('Queue is empty') #Empty class from arrayStack.py
        return self._data[self._front]

    def dequeue(self):
        '''remove and return the first elemtent of the queue FIFO
        raise exception if the queue is empty'''

        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None # help garbade collection, reclaim unused space
        self._front = (self._front + 1) % len(self._data) #circular implementation
        self._size -= 1
        return answer
    
    def enqueue(self, e):
        '''add an element to the back of the queue.'''
        if self._size == len(self._data):
            self._reisze(2*len(self._data)) #double the array size
        avail = (self._front + self._size) % len(self._data) #compute location of the next opening based on this formula
        self._data[avail] = e 
        self._size += 1 

    def _resize(self, cap):
        '''resize to a new list of capacity >= len(self).'''
        old = self._data #keep track of existing list
        self._data = [None]*cap #allocate list withn new capacity
        walk = self._front
        for k in range(self._size): #only consider existing elements
            self._data[k] = old[walk] #shift indices
            walk = (1 + walk) % len(old)

        self._front = 0 #front has been realigned




