class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: int
    # item: int
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size:
            return self
        if left_size > ind and self.left is not None:
            return self.left.select(ind)
        if left_size < ind and self.right is not None:
            return self.right.select(ind-(left_size+1))
        return None


    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    def search(self, key):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None
    

    '''
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    '''
    def insert(self, key):
        if self.key is None:
            self.key = key
        elif self.key > key: 
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
            self.size += 1
        elif self.key < key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.right.insert(key)
            self.size += 1
        return self

    
    ####### Part b #######

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 
    '''
    def rotate(self, direction, child_side):
        # Your code goes here
        #split into two categories, when the child subtree is on L side, and when its on R side 
        if child_side == 'L' and self.left is not None: 
            # split into directions, L and R 
            if direction == 'L':
                # assign the variables to their subtrees from the original tree before rotation  
                x = self.left
                y = self.left.right
                A = self.left.left
                B = self.left.right.left
                C = self.left.right.right 
                # reassign the tree values to reflect the change in the position of y, x, and B 
                self.left = y 
                self.left.left = x 
                self.left.left.right = B 
                # size of y and x have changed -- reassign the size of y and x: 
                # size of y (self.left.size) is now equal to the old size of x  
                self.left.size = x.size 
                # check if A and B are empty subtrees 
                if A is not None and B is not None:
                    # size of x (self.left.left.size) is equal to the size of it's subtrees + 1  
                    self.left.left.size = A.size + B.size + 1
                # check all of the other cases when one is an empty subtree and the other isnt
                elif A is not None: 
                    self.left.left.size = A.size + 1
                elif B is not None: 
                    self.left.left.size = B.size + 1
                else: 
                    self.left.left.size = 1
                return self

            if direction == 'R': 
                # assign the variables to their subtrees from the original tree before rotation
                x = self.left.left
                y = self.left
                A = self.left.left.left
                B = self.left.left.right
                C = self.left.right
                # reassign the tree values to reflect the change in the position of y, x, and B
                self.left = x 
                self.left.right = y 
                self.left.right.left = B 
                # size of y and x have changed -- reassign the size of y and x: 
                # size of x (self.left.size) is now equal to the old size of y
                self.left.size = y.size
                # check if B and C are empty subtrees 
                if B is not None and C is not None:
                    # size of y (self.left.right.size) is equal to the size of it's subtrees + 1 
                    self.left.right.size = B.size + C.size + 1
                # check all of the other cases when one is an empty subtree and the other isnt
                elif B is not None:
                    self.left.right.size = B.size + 1
                elif C is not None:
                    self.left.right.size = C.size + 1
                else: 
                    self.left.right.size = 1 

                return self

        if child_side == 'R' and self.right is not None:
            if direction == 'L':
                # assign the variables to their subtrees from the original tree before rotation
                x = self.right 
                y = self.right.right 
                A = self.right.left  
                B = self.right.right.left 
                C = self.right.right.right
                # reassign the tree values to reflect the change in the position of y, x, and B 
                self.right = y 
                self.right.left = x 
                self.right.left.right = B 
                # size of y and x have changed -- reassign the size of y and x: 
                # size of y (self.right.size) is now equal to the old size of x
                self.right.size = x.size
                # check if A and B are empty subtrees 
                if A is not None and B is not None: 
                    # size of x (self.right.left.size) is equal to the size of it's subtrees + 1
                    self.right.left.size = A.size + B.size + 1
                # check all of the other cases when one is an empty subtree and the other isnt
                elif A is not None: 
                    self.right.left.size = A.size + 1
                elif B is not None: 
                    self.right.left.size = B.size + 1
                else: 
                    self.right.left.size = 1
                return self 

            if direction == 'R':
                # assign the variables to their subtrees from the original tree before rotation
                y = self.right 
                x = self.right.left 
                A = self.right.left.left 
                B = self.right.left.right  
                C = self.right.right
                # reassign the tree values to reflect the change in the position of y, x, and B  
                self.right = x 
                self.right.right = y 
                self.right.right.left = B 
                # size of y and x have changed -- reassign the size of y and x: 
                # size of x (self.right.size) is now equal to the old size of y
                self.right.size = y.size
                # check if B and C are empty subtrees
                if B is not None and C is not None:
                    # size of y (self.right.right.size) is equal to the size of it's subtrees + 1
                    self.right.right.size = B.size + C.size + 1
                # check all of the other cases when one is an empty subtree and the other isnt 
                elif B is not None: 
                    self.right.right.size = B.size + 1
                elif C is not None: 
                    self.right.right.size = C.size + 1
                else: 
                    self.right.right.size = 1

                return self 
                
        return self
                

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self