
'''

Last-In-First-Out (LIFO) based stack that used python lists 
the top of the stack will be the last element in the list _data[-1]

'''


'''Create a class that avoids the pitfall of raising an exception of popping an empty list'''
class Empty(Exception):
    '''Error attempting to access an element from an empty container.'''
    pass

class ArrayStack:
    '''LIFO stack implementation using a Python list as underlying storage.'''

    def __init__(self):
        '''create an empty stack.'''
        self._data = []
    
    def __len__(self):
        '''return the number of elements in the stack.'''
        return len(self._data)

    def is_empty(self):
        '''return true if the stack is empty.'''
        return len(self._data) == 0
    
    def push(self, e):
        '''add element e to the top of the stack.'''
        self._data.append(e) #new item stored at the end of list

    def top(self):
        '''return but do not remove the element at the top of teh stack
        raise empty exception if the stack is empty.'''
        
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data[-1] #the last item in the list
    
    def pop(self):
        '''remove and return the element from the top of the stack (LIFO)
        raise Empty exception if the stack is empty.'''

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop() #if no index passed the defualt is -1 meaning the last item 

    def __str__(self):
        '''print stack as a list'''
        return str(self._data)

s = ArrayStack()
s.push(5)
s.push(3)
print(s)
print(s.is_empty())

'''
[5, 3]
False

'''