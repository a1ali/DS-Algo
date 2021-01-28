class _DoublyLinkedBase:
    '''A base class providing a doubly linked list representation'''

    class _Node:
        '''Lightwieght nonpublic class for storing a doubly linked node.'''
        __slots__ = '_element' , '_next', '_prev'
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev #this time we keep track of the previous node 
            self._next = next 

    def __init__(self):
        '''create an empty list.'''
        self._header = self._Node(None, None, None) #create the sentinels
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer #connect the sentinals together 
        self._trailer._prev = self._header
        '''
        all elements inserted and delted will be in between the header and trailer
        '''
        self._size = 0

    
    def __len__(self):
        return self._size 
    
    def is_empty(self):
        return self._size == 0 

    def _insert_between(self, e, predecessor, successor):
        '''Add element e between two existing nodes and reutrn new node.'''
        newest = _Node(e, predecessor, successor) #linked to neighbors
        predecessor._next = newest #link previous element to new
        successor._prev = newest #link the succsor to the new
        self._size += 1 
        return newest

    def _delete_node(self, node):
        '''Delete nonsentinal node from the list and return its element'''
        '''Connect the nodes sourrounding the node to delete'''
        predecessor = node._prev 
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor 
        self._size -= 1 
        element = node._element #store the deteling node's element 
        node._prev = node._next = node._element = None #deprecate node 
        return element

class LinkedDeque(_DoublyLinkedBase):
    #using inheritance 
    '''Double ended queue implementation based on a doubly linked list.'''

    def first(self):
        '''return (but do not remove) the element at the front of the deque.'''
        if is_empty():
            raise Empty('The list is empty')
        return self._header._next._element #real item just after header 
    
    def last(self):
        '''return (but do not remove) the element at the back of the deque.'''
        if is_empty():
            raise Empty('The list is empty')
        return self._trailer._prev._element #real item just before the trailer 

    def insert_first(self, e):
        '''add an element to the front of the deuquee.'''
        self._insert_between(e, self._header, self._header._next) #after header 

    def insert_last(self, e):
        '''add an element to the back of the dequeue.'''
        self._insert_between(e, self._trailer._prev, self._trailer) #vefore trailer 

    def delete_first(self):
        '''remove and retrun the elemtn from the front of the dequeu.
        raise an exception if the dequeu is empty'''
        if self.is_empty():
            raise Empty('list is empty')
        return _delete_node(self._header._next)

    



    