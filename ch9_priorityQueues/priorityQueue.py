'''
use a composition design pattern by defining an _item class that assured that each element remained paired
with its associated count in the adt 
'''

class PriorityQueueBase:
    '''Abstract base class for a priority queue.'''

    class _item:
        '''lightwieght composite to store priority queue items'''
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v 

        def __lt__(self, other):
            return self._key < other._key #compare items based on their keys 
    
    def is_empty(self):
        '''return true if the priority queue is empty'''
        #concrete method assuming abstract len 
        return len(self) == 0 


'''
use an unsorted list to store the entries. inherits the base class above. 
each time a key val pair is added to the priority queue via the add method 
create an new _tem composite for the key and val, and add that item to the end
of the list. to locate the min key we must loop until we find the minumum. We assume 
a doubly linked list as the list
'''

class UnsortedPriorityQueue(PriorityQueueBase): #base class defines _item 
    '''A min-oriented priority queueu implemented with an unsorted list. '''

    def _find_min(self): #nonpublic
        '''return position of item with min key'''
        if self.is_empty(self):
            raise Empty('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk 
            walk = self._data.after(walk)
        return small 
    
    def __init__(self):
        '''create a new empty priority queue'''
        self._data = PositionalList() # use the doubly linked class from chapter 7 

    def __len__(self):
        '''return the number of items in the prioriy queue'''
        return len(self._data) #this is the inehritance from the doubly base in chapter 7 

    def add(self, key, value):
        '''add a key value pair'''
        self._data.add_last(self._item(key, value))

    def min(self):
        '''return but do not remove (k,v) tuple with minimum key.'''
        p = self._find_min()
        item = p.element() #also from doubly ll
        return (item._key, item._value) #tuple(k,v)

    def remove_min(self):
        '''remove and return (k,v) tuple with minimum key.'''
        p = self._find_min()
        item = self._data.delete(p) 
        return (item._key, item._value)


'''
sorted positional list, maintain the entries sorted by nondecreading keys. the first element
will be the one with the smallest key. the add method requires scanning the list before adding to 
find the appropriate position to insert the new item
'''
class SortedPriorityQueue(PriorityQueueBase):
    '''A min oriented priority queue implemented with a sorted list'''

    def __init__(self):
        '''create a new empty priority queue.'''
        self._data = PositionalList()

    def __len__(self):
        '''return the number of items in the priority queue'''
        return len(self._data)

    def add(self, key, value):
        '''add a key value pair'''
        newest = self._item(key, value) #make new item instance
        walk = self._data.last() #walk backward looking for smaller key 
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk) #find the positon where to insert the new element 
        if walk is None: #the new key will be the smallest
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest) #newest goes after walk 

    def min(self):
        '''return but do not remove (k,v) tuple with minimum key.'''
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        '''remove and return (k,v) tuple with minimum key.'''
        if self.is_empty():
            raise Empty('Priority queue is empty')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)
