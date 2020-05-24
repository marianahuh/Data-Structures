"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if empty
        if value is None:
            return
        # if empty then assigin new node value
        elif self.value is None:
            self.value = BSTNode(value)
        # check if new value is less than current node
        elif value < self.value:
            # and if there is no left value
            if not self.left:
                # the assign new left node as new node value
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        # otherwise if it is greater than current node
        else:
            # if there is no right value
            if not self.right:
                # assign new right node as new value
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if initial value is target value
        if self.value == target:
            return True
        # if value is greater than target then look left
        if self.value > target:
            # if is on the left return True
            if self.left:
                return self.left.contains(target)
        # if value is less than target the look right
        elif self.value < target:
            # if is on the right return True
            if self.right:
                return self.right.contains(target)
        # otherwise if not found then return False
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # if there is no value to the right return current value as the highest
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
