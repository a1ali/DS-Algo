'''
FIFO implementation of a queue using linked lists 
the front of the queue is set to be the head which allows for easy dequeuing 
the back of the queue is the tail which allows for enqueing new nodes 
'''

class LinkedQueue:
    '''FIFO queue implementation using a singly linked list for storage.'''

    class _Node:
        '''same as the one we used for stack
        nonpublic class for storing a singly linked node'''
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
            self._element = element
            self._next = next 

    def __init__(self):
        '''create an empty queue.'''
        self._head = None #init head to none
        self._tail = None
        self._size = 0 #number of elements in queue initially 0

    def __len__(self):
        '''return the number of elements in the queue.'''
        return self._size
    
    def is_empty(self):
        '''return true if the queue is empty'''
        return self._size == 0 
    
    def first(self):
        '''return (but do not remove) the element at the front of the queue this will be the head element'''
        if is_empty():
            Empty('The Queue is empty')
        return self._head._element #front aligned with head of list 
    
    def dequeu(self):
        '''remove and return the first element of the queue 
        raise exception if the queue is empty'''
        if is_empty():
            Empty('The queue is empty')
        answer = self._head._element #old head element 
        self._head = self._head._next  #make the new head the old head's next 
        self._size -= 1 #decrement the size of the queue 
        if self.is_empty(): #this is a special case as queue is empty after dequeing 
            self._tail = None #the removed head had been the tail 
        return answer 

    def enqueue(self, e):
        '''add an element to the back of the queue.'''
        newest = self._node(e, None) #node will be the tail node
        if self.is_empty():
            self._head = newest # this is a special case in which the list is initially empty 
        else:
            self._tail._next = newest # set the next of the current tail to be the new node
        self._tail = newest #make the new node the current tail 
        self._size += 1 #increase the size of the queue 


    
    

