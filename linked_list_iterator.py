from abstract_collection import AbstractCollection
from nodes import TwoWayNode

class LinkedListIterator(object):
    """
    Represents the list iterator for an linked list.
    """

    def __init__(self, backing_store):
        """
        Set the initial state of the list iterator.
        """
        self.backing_store = backing_store
        self.mod_count = backing_store.get_mod_count()
        self.first()

    # Navigators
    def first(self):
        """
        Resets the cursor to the beginning of the backing store.
        """
        self.cursor = self.backing_store.head.next
        self.last_access_node = None

    def last(self):
        """
        Resets the cursor to the end of the backing store.
        """
        self.cursor = self.cursor = self.backing_store.head
        self.last_access_node = None

    def has_next(self):
        """
        Returns True if the iterator has a next item or False otherwise.
        """
        return self.cursor != self.backing_store.head

    def next(self):
        """
        Preconditions: has_next() returns True.
        The list hasn't been modified except by this iterator's mutators.
        Returns the current item and advances the cursor to the next item.
        Raises: ValueError if there're no next items.
        """
        if not self.has_next():
            raise ValueError("No next item in the list iterator")
        if self.mod_count != self.backing_store.get_mod_count():
            raise AttributeError("Illegal modification of the backing store.")
        self.last_access_node = self.cursor
        self.cursor = self.cursor.next
        return self.last_access_node.data

    def has_prev(self):
        """
        Returns True if the iterator has a previous item or False otherwise.
        """
        return self.cursor.prev != self.backing_store.head

    def prev(self):
        """
        Preconditions: has_prev() returns True.
        The list hasn't been modified except by this iterator's mutators.
        Returns the current item and moves the cursor to the previous item.
        Raises: ValueError if there're no previous items.
        """
        if not self.has_prev():
            raise ValueError("No previous item in the list iterator")
        if self.mod_count != self.backing_store.get_mod_count():
            raise AttributeError("Illegal modification of the backing store.")
        self.cursor = self.cursor.prev
        self.last_access_node = self.cursor
        return self.last_access_node.data

    # Mutators
    def replace(self, new_data):
        """
        Preconditions: the current position is defined.
        The list hasn't been modified except by this iterator's mutators.
        Replaces the current position by `item`.
        Raises: AttributeError if the current position is undefined.
        """
        if self.last_access_node is None:
            raise AttributeError("The current position is undefined.")
        if self.mod_count != self.backing_store.get_mod_count():
            raise AttributeError("Illegal modification of the backing store.")
        self.last_access_node.data = new_data
        self.last_access_node = None

    def insert(self, new_data):
        """
        Preconditions: the list hasn't been modified except by this iterator's mutators.
        Inserts a new item at the current position.
        """
        if self.mod_count != self.backing_store.get_mod_count():
            raise AttributeError("Illegal modification of the backing store.")
        if self.last_access_node is None:
            # Cursor is not defined, simply add the item to the end.
            self.backing_store.add(new_data)
        else:
            new_node = TwoWayNode(new_data, prev=self.cursor.prev, next=self.cursor)
            new_node.prev.next = new_node
            new_node.next.prev = new_node
            self.backing_store.size += 1
            self.backing_store.inc_mod_count()
        self.last_access_node = None
        self.mod_count += 1

    def remove(self):
        """
        Preconditions: the current position is defined.
        The list hasn't been modified except by this iterator's mutators.
        Removes the item at the current position.
        Raises: AttributeError if the current position is undefined.
        """
        if self.last_access_node is None:
            raise AttributeError("The current position is undefined.")
        if self.mod_count != self.backing_store.get_mod_count():
            raise AttributeError("Illegal modification of the backing store.")
        # If the item removed was obtained via previous, move cursor forward IN ADVANCE.
        if self.last_access_node == self.cursor:
            self.cursor = self.cursor.next
        self.last_access_node.prev.next = self.last_access_node.next
        self.last_access_node.next.prev = self.last_access_node.prev
        self.backing_store.size -= 1
        self.backing_store.inc_mod_count()
        self.last_access_node = None
        self.mod_count += 1
