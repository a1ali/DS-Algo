
'''Create a class that avoids the pitfall of raising an exception of popping an empty list'''
class Empty(Exception):
    '''Error attempting to access an element from an empty container.'''
    pass

class LinkedStack:
    '''Lifo stack implementation using a singly linked list for storage.'''

    #Nested _Node class
    class _Node:
        '''lightweight, nonpublic class for storing a singly linked node.'''
        __slots__ = '_element', '_next' #streamline memory usage 

        '''
        The special attribute __slots__ allows you explicitly state which instance attributes u expect 
        your object instances to have, this inturn allows for 
            faster attribute access
            space saving in memroy
        '''

        def __init__(self, element, next): #initialize node's fields
            self._element = element
            self._next = next 

    '''
    Each stack instance maintains two variables. The _head member is a ref
    to the node at the head of the list (None if empty), alsoe keep track
    of number of elements in the list, pushing an element on to that stack 
    is similar to the algorithm to add a new head 

    '''

    #stack methods
    def __init__(self):
        '''create an empty stack.'''
        self._head = None #reference to head node intially it is set to None which will get pushed to tail
        self._size = 0 #number of stack elements

    def __len__(self):
        '''return the number of elements in the stack'''
        return self._size
    
    def is_empty(self):
        '''Return True if the stack is empty'''
        return self._size == 0
    
    def push(self, e):
        '''push an element to the top of the stack.'''
        self._head =  self._Node(e, self._head) #create and link a new node
         #the _next field of the new node is set to the existing top node and then self._head is reassigned
        self._size += 1 #increase the size of elements in the stack

    def top(self):
        '''return the current head element but do not remove it
           raise empty exception if the stack is emtpy'''
        if self._head == None:
            raise Empty('No element in stack')
        return self._head._element 
    
    def pop(self):
        '''remove top element in stack and return it.
           raise exception if the stack is empty'''
        if self.is_empty():
            return Empty('Stack is empty') 
        
        element = self._head._element #store the current head element 
        self._head = self._head._next #replace the old head with its next 
        self._size -= 1  #decrease stack size
        return element #return the old element 
    
    def printList(self):
        '''traversing through the linked list'''
        temp = self._head 
        for _ in range(0,self._size):
            print(temp._element)
            temp = temp._next 

    def reverse(self):
        '''return a reversed linked list of the original '''
        dum = LinkedStack()
        l = []
        temp = self._head
        for _ in range(self._size):
            l.append(temp._element)
            temp = temp._next
        #l = l[::-1]
        for i in l:
            dum.push(i)

        return dum  
    
x = LinkedStack()

x.push(2)
x.push(3)
x.push(1)
print(x.top())
x.printList()
x.pop()
x.printList()