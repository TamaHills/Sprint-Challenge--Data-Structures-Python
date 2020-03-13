
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        elif value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            return True

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right:
            return self.right.get_max()
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    def delete(self, value):
        if self.contains(value) is True:
            if value == self.value:
                if self.left:
                    left_node = self.left
                    max_value = left_node.get_max()
                    self.value = max_value
                    left_node.delete(max_value)
                elif self.right:
                    right_node = self.right
                    self.value = right_node.value
                    right_node.delete(right_node.value)
                else:
                    return True
            elif value > self.value:
                delete = self.right.delete(value)
                if delete:
                    self.right = None
            else:
                delete = self.left.delete(value)
                if delete:
                    self.left = None

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)
        
        print(self.value)

        if self.right:
            self.right.in_order_print(self.right)
    

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        print(self.value)

        if self.left:
            self.left.pre_order_dft(self.left)
        
        if self.right:
            self.right.pre_order_dft(self.right)
            
        

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left:
            self.left.post_order_dft(self.left)
        
        if self.right:
            self.right.post_order_dft(self.right)
            
        print(self.value)