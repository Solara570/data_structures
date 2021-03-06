from abstract_bag import AbstractBag
from nodes import Node
from linked_bst import LinkedBST


class LinkedBag(AbstractBag):
    """
    A bag implementation based on linked list.
    """

    # Constructor
    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the
        contents of source_collection, if it's present.
        """
        self.items = None
        self.prev_pointer = None    # Points to the node before the item node
        self.curr_pointer = None    # Points directly to the item node
        AbstractBag.__init__(self, source_collection)
        # super().__init__(source_collection)

    # Accessor methods
    def __iter__(self):
        """
        Supports iteration over a view of self.
        """
        cursor = self.items
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next

    def __contains__(self, item):
        self.prev_pointer = None
        self.curr_pointer = self.items
        while self.curr_pointer is not None:
            if self.curr_pointer.data == item:
                return True
            self.prev_pointer = self.curr_pointer
            self.curr_pointer = self.curr_pointer.next
        self.prev_pointer = None
        self.curr_pointer = None
        return False

    def __eq__(self, other):
        """
        Returns true if the contents in self equals the contents in other,
        or False otherwise.
        """
        if type(self) != type(other):
            return False
        if len(self) != len(other):
            return False
        for item in other:
            if self.count(item) != other.count(item):
                return False
        return True

    def count(self, item):
        """
        Returns the number of instances of item in self.
        """
        total = 0
        for bag_item in self:
            if item == bag_item:
                total += 1
        return total

    # Mutator methods
    def clear(self):
        """
        Void self.
        """
        self.items = None
        self.size = 0

    def add(self, item):
        """
        Add an item to self.
        """
        self.items = Node(item, self.items)
        self.size += 1

    def remove(self, item):
        """
        Remove an item from self.
        Raise KeyError if item is not in self.
        """
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        # If it's the first to be removed
        if self.curr_pointer == self.items:
            self.items = self.items.next
        else:
            self.prev_pointer.next = self.curr_pointer.next
        self.size -= 1


class TreeSortedBag(AbstractBag):
    """
    A bag implementation based on linked BST.
    """

    # Constructor
    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the
        contents of source_collection, if it's present.
        Rebalance the bag if it's not balanced.
        """
        self.items = LinkedBST()
        AbstractBag.__init__(self, source_collection)
        if not self.items.is_balanced():
            self.items.rebalance()

    # Accessor methods
    def __iter__(self):
        """
        Supports iteration over a view of self using inorder traversal.
        """
        return self.items.inorder()

    def __contains__(self, item):
        return (item in self.items)

    def __eq__(self, other):
        """
        Returns true if the contents in self equals the contents in other,
        or False otherwise.
        """
        if type(self) != type(other):
            return False
        if len(self) != len(other):
            return False
        for item in other:
            if self.count(item) != other.count(item):
                return False
        return True

    def count(self, item):
        """
        Returns the number of instances of item in self.
        """
        total = 0
        for bag_item in self:
            if item == bag_item:
                total += 1
        return total

    # Mutator methods
    def clear(self):
        """
        Void self.
        """
        self.size = 0
        self.items.clear()

    def add(self, item):
        """
        Add an item to self.
        """
        self.items.add(item)
        self.size += 1

    def remove(self, item):
        """
        Remove an item from self.
        Raise KeyError if item is not in self.
        """
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        # If it's the first to be removed
        self.items.remove(item)
        self.size -= 1
