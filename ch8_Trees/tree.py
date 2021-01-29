class Tree:
    '''Abstract base class representing a tree structure'''

    #Nested position class 
    class Position:
        '''An abstraction representing the location of a single element'''

        def element(self):
            '''return the element stored at this position'''
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            '''return true if other position represents teh same location'''
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            '''return True if other does not represent the same location
            '''
            return not (self == other)

    #abstract methods that concreter sublcass must support 
    def root(self):
        '''return position representing the tree's root or none if empty'''
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        '''return position representing p's parent or none if p is root'''
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        '''return the number of children that position p has'''
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        '''generate an iteration of position representing p's children'''
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        '''return the total number of elements in the tree.'''
        raise NotImplementedError('must be implemented by subclass')

    #conrecte methods implemented in this class 

    def is_root(self, p):
        '''return True if position p represents the root of the tree'''
        return self.root() == p 

    def is_leaf(self, p):
        '''return true if p has no children'''
        return num_children(p) == 0 
    
    def is_empty(self):
        '''return true if the tree is empty'''
        return len(self) == 0
        
        