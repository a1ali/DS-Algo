import ctypes


'''
If an underlying array is full
1. allocate a new array B with larger capacity
2. set B[i] = A[i] for i =0, ...,n-1, where n denotes current number of items.
3. set A = B, that is, we henceforth use B as the array supporting the list.
4. Insert the new element in the new array.

'''


class DynamicArray:
    '''A dynamic array class akin to a simplified Python list.'''

    def __init__(self):
        '''create and empty array.'''
        self._n = 0 #count actual elements
        self._capacity = 1  #defualt array capacity
        self._A = self._make_array(self._capacity) #low-level array

    def __len__(self):
        '''return number of elements stored in the array.'''
        return self._n 

    def __getitem__(self, k):
        '''Return element at index k.'''
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k] # retrieve from array

    def append(self, obj):
        '''Add object to end of the array.'''
        if self._n == self._capacity: #not enough room
            self._resize(2*self._capacity) #so double capacity
        self._A[self._n] = obj 
        self._n += 1 

    def _resize(self, c): #nonpublic utility
        '''Resize internal array to capacity c.'''
        B = self._make_array(c) #new (bigger) array
        for k in range(self._n): #for each existing value
            B[k] = self._A[k]
        self._A = B  #use bigger array
        self._capacity = c 

    def _make_array(self, c): #nonpublic
        '''Return new array with capacity C.'''
        return (c*ctypes.py_object)() #see ctypes documentation


a = DynamicArray()

a.append(1)
print(len(a))