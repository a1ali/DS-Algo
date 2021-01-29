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

    def delete_last(self):
        '''remove and return the element from the last of the dequeu.
        raise an exception if the dequeue is empty.'''
        if self.is_empty():
            raise Empty('list is empty')
        return _delete_node(self._trailer._prev)

    

class PositionalList(_DoublyLinkedBase):
    '''A sequential container of elements allowing positional access'''

    #nestedd Position class 
    class Position:
        '''An abstraction representing the location of a single element.'''

        def __init__(self, container, node):
            '''constructor should not be invoked by user.'''

            self._container = container
            self._node = node 

        def element(self):
            '''return the element stores at this position'''
            return self._node._element

        def __eq__(self, other):
            '''return true if other is a position representing the same location'''
            return type(other) is type(self) and other._node is self._node 

        def __ne__(self, other):
            '''return true if other does not represent the same location.'''
            return (self == other) #opposite of __eq__

    #utility method
    def _validate(self, p):
        '''return position node, or raise appropriate error if invalid'''
        if not isinstance(p, self._Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node 

    def _make_position(self, node):
        '''return position instance for given node (or None if sentianl).'''
        if node is self._header or node is self._trailer:
            return None 
        else:
            return self.Position(self, node)

    #accessors
    def first(self):
        '''return the first position in the liost or none if list is empty'''
        return self._make_position(self._header._next)
    
    def last(self):
        '''return the last postion in the ;list of none if empty'''
        return self._make_position(self._trailer._prev)
    
    def before(self, p):
        '''return the position just before position p or none if p is first'''
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        '''return the position just after position p or none if p is last.'''
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        '''generate a forward iteration of the elements of the list.'''
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    #------------------------------- mutators -------------------------------
    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        '''Add element between existing nodes and return new Position.'''
        node = super(). insert_between(e, predecessor, successor)
        return self._make_position(node)   

    def add_first(self, e):
        '''Insert element e at the front of the list and return new Position.'''
        return self._insert_between(e, self. header, self. header. next)  

    def add_last(self, e):
        '''Insert element e at the back of the list and return new Position.'''
        return self._insert_between(e, self. trailer. prev, self. trailer)  

    def add_before(self, p, e):
        '''Insert element e into list before Position p and return new Position.'''
        original = self._validate(p)
        return self._insert_between(e, original. prev, original)    

    def add_after(self, p, e):
        '''Insert element e into list after Position p and return new Position.'''
        original = self._validate(p)
        return self._insert_between(e, original, original. next) 

    def delete(self, p):
        '''Remove and return the element at Position p.'''
        original = self._validate(p)
        return self._delete_node(original) # inherited method returns element   

    def replace(self, p, e):
        '''Replace the element at Position p with e.
         Return the element formerly at Position p.
         '''
        original = self._validate(p)
        old_value = original._element # temporarily store old element
        original.element = e # replace with new element
        return old_value # return the old element value    