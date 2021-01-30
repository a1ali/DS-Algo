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

'''
binary tree has at most two children left and right 
bianrytree class will inherit from the tree class above
'''
class BinaryTree(Tree):
    '''abstract base class representing a binary tree structure'''

    #additional abstract methods
    def left(self, p):
        '''return a position representing p' left child 
        return none if it does not have a left chiild'''
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        '''return a position representing p's right child'''
        '''reutrn none if it does not have a right child'''
        raise NotImplementedError('must be implemented by sublcass')

    
    #concrete methods implemented in this class 
    def sibling(self, p):
        '''return a position representing p'sibling none if no sibling'''
        parent = self.parent(p) #get the parent of p 
        if parent  is None: # p is the root 
            return None 

        else:
            if p == self.left(parent): #p is the left sibling 
                return self.right(parent) #return the right sibling
            else:
                return self.left(parent) #p is the right sibling 
    
    def children(self, p):
        '''generate an iteration of position representing p' children'''
        if self.left(p) is not None: #get left child if it exists 
            yield self.left(p)
        if self.right(p) is not None: #get right child if it exits 
            yield self.right(p)


'''
we can represent binary trees using linked like nodes 
a node will contain a reference to the left child, right child, parent, and it's element
'''

class LinkedBinaryTree(BinaryTree):
    '''linked representation of a binary tree structure'''

    class _Node: #lightweigh non public class for storing a node
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent= None, left=None, right=None): #initially creates root 
            self._element = element
            self._parent = parent 
            self._left = left 
            self._right = right 

    class Position(BinaryTree.Position):
        '''an abstraction representing the location of a single element'''
        def __init__(self, container, node):
            '''contructor should not be invoked by user.'''
            self._container = container
            self._node = node 

        def element(self):
            '''return the element stored at this position'''
            return self._node._element
        def __eq__(self, other):
            '''return True if other is a Position representing the same location.'''
            return type(other) is type(self) and other._node is self._node #both same type and same node

    
    def _validate(self, p):
        '''return associated node, if position is valid'''
        if not isinstance(p, self.Position):
            '''isinstance returns True if the specified object is of teh specfied type'''
            return TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node: #convention for deprecated nodes 
            raise ValueError('p is no longer valid')
        return p._node 
    
    def _make_position(self, node):
        '''return Position instance for given node or none if no node'''
        return self.Position(self, node) if node is not None else None 

    #constructor for the binary tree
    def __init__(self):
        '''create an initially empty binary tree.'''
        self._root = None
        self._size = 0 

    #public accessors 
    def __len__(self):
        '''return the total number of elements in the tree'''
        return self._size 

    def root(self):
        '''return the root position of the tree or none if the tree is empty'''
        return self._make_position(self._root)

    def parent(self, p):
        '''return the position of p's parent or None if p is root'''
        node = self._validate(p) #check if p is a vlid node
        return self._make_position(node._parent)

    def left(self, p):
        '''return the position of p's left child or none if no left child'''
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        '''return the position of p's right child or none if no right child'''
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        '''return the number of children of Position p.'''
        node = self._validate(p)
        count = 0 
        if node._left is not None:
            count += 1 
        if node._right is not None:
            count += 1 
        return count 

    def _add_root(self, e):
        '''place element e at the root of an empty tree and return new position
        raise valueerror if tree not empty'''
        if self._root is not None: raise ValueError('Root exists')
        self._size = 1 
        self._root = self._Node(e)
        return self._make_position(self._root)
    
    def _add_left(self, p, e):
        '''create a new left child for position p storing element e
        return the position of new node 
        rasie value error if position p is invalid or p already has a left child'''
        node = self._validate(p)
        if node._left is not None: raise ValueError('left child exists')
        self._size += 1
        node._left = self._Node(e , node) #e element node = parent 
        return self._make_position(node._left) 

    def _add_right(self, p, e):
        '''create a new right child for position p storing element e
        return the position of new node
        raise value error if position p is invalid or p already has a right child.'''
        
        node = self._validate(p)
        if node._right is not None: raise ValueError('right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        '''replace the element at position p with e, and return old element'''
        node = self._validate(p)
        olf = node._element
        node._element = e 
        return old 

    def _delete(self, p):
        '''delte the node at position p, and replace it with its child if any 
        return the element that had been stored at Position p.
        Raise value error if position p is invalid or p has two children '''

        node = self._validate(p)
        if self._num_children(p) == 2: raise ValueError('p has two children')
        child = node._left if node._left else node._right #still might be none 
        if child is not None:
            child._parent = node._parent #child grandparent becomes parent 
        if node is self._root: #if the delteing node is the root 
            self._root = child #child becomes the root 
        else:
            parent = node._parent #it has no children 
            if node is parent._left:
                parent._left = child #will be none 
            else:
                parent._right = child 
        self._size -= 1 
        node._parent = node #convention for deprecated node 
        return node._element

    def _attach(self, p , t1, t2):
        '''attach tree t1 and t2 as left and right subtrees of external p.'''
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2): #all 3 tree must be same type
            raise TypeError('Trees types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty(): #attack t1 as left subtree of node 
            t1._root._parent = node 
            node._left = t1._root 
            t1._root = None #set t1 to become empty 
            t1._size = 0 
        if not t2.is_empty(): #attack t2 as right subtree of node 
            t2._root._parent = node 
            node._right = t2._root 
            t2._root = None #set t2 to become empty 
            t2._size = 0 
        




    


    



    


