from math import log
from nodes import BSTNode
from stacks import ArrayStack
from queues import LinkedQueue
from array_list import ArrayList
from abstract_collection import AbstractCollection


class LinkedBST(AbstractCollection):
    """
    A link-based binary search tree implementation.
    """

    def __init__(self, source_collection=None):
        self.root = None
        AbstractCollection.__init__(self, source_collection)

    # Accessors
    def __str__(self):
        """
        Returns a string representation with the tree rotated
        90-degree counterclockwise.
        """
        # Helper function
        def recurse(node, level):
            s = ""
            if node is not None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s

        return recurse(self.root, 0)

    def __iter__(self):
        """
        Returns the preorder traveral of self in the form of iterator using a stack.
        """
        stack = ArrayStack()
        stack.push(self.root)
        while not stack.is_empty():
            top_node = stack.pop()
            yield top_node.data
            right_node = top_node.right
            left_node = top_node.left
            if right_node is not None:
                stack.push(right_node)
            if left_node is not None:
                stack.push(left_node)

    def __contains__(self, item):
        if len(self) == 0:
            return False
        node = self.root
        while node is not None:
            if node.data == item:
                return True
            elif node.data > item:
                node = node.left
            else:
                node = node.right
        return False

    def height(self):
        """
        Returns the height of the tree.
        Empty tree has a height of -1 by definition.
        """
        # Helper function
        def recurse(node):
            if node is None:
                return -1
            return 1 + max([recurse(node.left), recurse(node.right)])

        return recurse(self.root)

    def is_balanced(self):
        """
        Returns True if the height is less than 2*log_2(size) or False otherwise.
        """
        if self.is_empty():
            return True
        return self.height() < 2 * log(len(self) + 1, 2) - 1

    def find(self, item):
        """
        Returns data if item is found or None otherwise
        """
        # Helper function
        def recurse(node):
            if node is None:
                return None
            elif node.data == item:
                return node.data
            elif node.data > item:
                return recurse(node.left)
            else:
                return recurse(node.right)
        return recurse(self.root)

    def predecessor(self, item):
        """
        Returns the largest data that is less than the given item,
        or None if there're none.
        """
        pred = None
        for data in self.inorder():
            if data < item:
                pred = data
        return pred

    def successor(self, item):
        """
        Returns the smallest data that is greater than the given item,
        or None if there're none.
        """
        succ = None
        for data in self.inorder():
            if data > item:
                succ = data
                break
        return succ

    def range_find(self, lower, upper):
        """
        Returns a sorted list of all elements between lower and upper bounds.
        """
        range_list = ArrayList()
        for data in self.inorder():
            if lower <= data <= upper:
                range_list.add(data)
        return range_list

    def preorder(self):
        """
        Returns the preorder traveral of self in the form of iterator.
        """
        helper_list = list()

        def recurse(node):
            if node is not None:
                helper_list.append(node.data)
                recurse(node.left)
                recurse(node.right)

        recurse(self.root)
        return iter(helper_list)

    def inorder(self):
        """
        Returns the inorder traveral of self in the form of iterator.
        """
        # Helpers
        helper_list = list()

        def recurse(node):
            if node is not None:
                recurse(node.left)
                helper_list.append(node.data)
                recurse(node.right)

        recurse(self.root)
        return iter(helper_list)

    def postorder(self):
        """
        Returns the postorder traveral of self in the form of iterator.
        """
        helper_list = list()

        def recurse(node):
            if node is not None:
                recurse(node.left)
                recurse(node.right)
                helper_list.append(node.data)

        recurse(self.root)
        return iter(helper_list)

    def levelorder(self):
        """
        Returns the levelorder traveral of self in the form of iterator using a queue.
        """
        queue = LinkedQueue()
        queue.add(self.root)
        while not queue.is_empty():
            front_node = queue.pop()
            yield front_node.data
            left_node = front_node.left
            right_node = front_node.right
            if left_node is not None:
                queue.add(left_node)
            if right_node is not None:
                queue.add(right_node)

    # Mutators
    def clear(self):
        self.root = None
        self.size = 0

    def add(self, item):
        """
        Adds the item to the tree.
        """
        # Helper function to search for item's position

        def recurse(node):
            if item < node.data:
                if node.left is None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            elif node.right is None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)

        if self.is_empty():
            self.root = BSTNode(item)
        else:
            recurse(self.root)
        self.size += 1

    def remove(self, item):
        """
        Precondition: item is in self.
        Raises: KeyError if item is not in self.
        Postcondition: item is removed from self.
        """
        # Check if the item is in the tree.
        if item not in self:
            raise KeyError("Item is not in the tree.")
        # Find the node that to be removed, the data inside, its parent node and the direction.
        return_data = None
        curr_node = self.root
        root_backup = BSTNode(None, left=curr_node)
        parent = root_backup
        direction = "L"
        while curr_node is not None:
            if curr_node.data == item:
                return_data = curr_node.data
                break
            elif curr_node.data > item:
                parent = curr_node
                curr_node = curr_node.left
                direction = "L"
            else:
                parent = curr_node
                curr_node = curr_node.right
                direction = "R"
        # Case 1: The node only have a right subtree.
        #         Replace this node by its right subtree.
        if curr_node.left is None:
            if direction == "L":
                parent.left = curr_node.right
            else:
                parent.right = curr_node.right
        # Case 2: The node only have a left subtree.
        #         Replace this node by its left subtree.
        elif curr_node.right is None:
            if direction == "L":
                parent.left = curr_node.left
            else:
                parent.right = curr_node.left
        # Case 3: The node have both subtrees.
        #         Replace this node by the rightmost node on the left tree.
        else:
            # Find the rightmost node and its parent
            parent = curr_node
            rightmost_node = curr_node.left
            while rightmost_node.right is not None:
                parent = rightmost_node
                rightmost_node = rightmost_node.right
            # Replace the data
            curr_node.data = rightmost_node.data
            # Tree cleanup with a sneaky condition check
            if parent is curr_node:
                parent.left = rightmost_node.left
            else:
                parent.right = rightmost_node.left
        # Final: Reduce the size, restore the tree
        self.size -= 1
        if self.is_empty():
            self.root = None
        else:
            self.root = root_backup.left
        return return_data

    def replace(self, item, new_item):
        """
        Replaces the item with new_item.
        Though you can't simply replace the value, since it has to be a BST,
        so actually it's a two-step procedure: removal and addition.
        """
        self.remove(item)
        self.add(new_item)

    def rebalance(self):
        """
        Rebalance the tree by using the inorder traversal.
        """
        # Record the data
        data_list = list(self.inorder())
        # Setup the new tree

        def setup_tree(data_list):
            if len(data_list) == 0:
                return None
            if len(data_list) == 1:
                return BSTNode(data_list[0])
            mid_ind = len(data_list) // 2
            new_node = BSTNode(
                data_list[mid_ind],
                left=setup_tree(data_list[:mid_ind]),
                right=setup_tree(data_list[mid_ind + 1:])
            )
            return new_node

        self.root = setup_tree(data_list)


if __name__ == '__main__':
    import random
    random.seed(30)
    num_list = random.sample(list(range(1, 101)), 20)
    tree = LinkedBST(num_list)
    print(tree)
    print("Height =", tree.height())
    print("Is balanced:", tree.is_balanced())
    print("Predecessor of 28 =", tree.predecessor(28))
    print("Predecessor of 0 =", tree.predecessor(0))
    print("Successor of 28 =", tree.successor(28))
    print("Successor of 127 =", tree.successor(127))
    print("Range find (10, 50) =", tree.range_find(10, 50))
