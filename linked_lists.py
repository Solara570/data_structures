from nodes import Node, TwoWayNode
from abstract_list import AbstractList
from linked_list_iterator import LinkedListIterator


class LinkedList(object):
    def __init__(self, array):
        head = None
        for item in array:
            head = Node(item, next=head)
        self.head = head

    def get_head(self):
        return self.head

    def traverse(self):
        probe = self.head
        while probe is not None:
            print(probe.data)
            probe = probe.next

    def length(self):
        list_length = 0
        probe = self.head
        while probe is not None:
            probe = probe.next
            list_length += 1
        return list_length

    def search(self, target):
        probe = self.head
        while probe is not None and target != probe.data:
            probe = probe.next
        if probe is not None:
            print(f"Target {target} found.")
            return probe
        else:
            print(f"Target {target} not found.")
            return None

    def replace(self, target, new_item):
        probe = self.head
        has_replacement = False
        while probe is not None:
            if target == probe.data:
                probe.data = new_item
                has_replacement = True
            probe = probe.next
        return has_replacement

    def replace_at(self, k, new_item):
        probe = self.head
        i = 0
        while i < k:
            probe = probe.next
            i += 1
        if probe is not None:
            probe.data = new_item
        return probe

    def insert_at_head(self, new_item):
        new_node = Node(new_item, self.head)
        self.head = new_node

    def insert_at_tail(self, new_item):
        new_node = Node(new_item, None)
        if self.head is None:
            self.head = new_node
        else:
            probe = self.head
            while probe.next is not None:
                probe = probe.next
            probe.next = new_node

    def delete_at_head(self):
        if self.head is None:
            return
        deleted_data = self.head.data
        self.head = self.head.next
        return (self.head, deleted_data)

    def delete_at_tail(self):
        if self.head is None:
            return
        elif self.head.next is None:
            deleted_data = self.head.data
            self.head = None
            return deleted_data
        else:
            probe = self.head
            while probe.next.next is not None:
                probe = probe.next
            deleted_data = probe.next.data
            probe.next = None
            return deleted_data

    def insert_at(self, k, new_item):
        if self.head is None or k < 0:
            self.head = Node(new_item, self.head)
        else:
            probe = self.head
            i = 0
            while i < k and probe.next is not None:
                probe = probe.next
                i += 1
            if probe.next is None:
                probe.next = Node(new_item, None)
            else:
                new_node = Node(new_item, probe.next)
                probe.next = new_node
        return self.head

    def delete_at(self, k):
        if self.head is None or self.head.next is None or k <= 0:
            return self.delete_at_head()
        else:
            probe = self.head
            i = 0
            while i < k - 1 and probe.next.next is not None:
                probe = probe.next
                i += 1
            deleted_data = probe.next.data
            if probe.next.next is not None:
                probe.next = probe.next.next
            else:
                probe.next = None
            return self.head, (deleted_data)

    def insert(self, k, new_item):
        # Rename
        return self.insert_at(k, new_item)

    def pop(self, k):
        # Rename
        return self.delete_at(k)


class TwoWayLinkedList(LinkedList):
    def __init__(self, ll_head):
        # Special case
        if ll_head is None:
            self.head = None
            self.tail = None
            return
        # Initialize from a one-way linked list
        sentinel = TwoWayNode(None, None)
        prev_head = sentinel
        while ll_head != None:
            new_node = TwoWayNode(ll_head.data, prev=prev_head, next=None)
            prev_head.next = new_node
            ll_head = ll_head.next
            prev_head = prev_head.next
        self.head = sentinel.next
        self.tail = prev_head
        # Drop sentinel node
        self.head.prev = None
        del sentinel

    # Many methods need to be rewrite though...
    def get_tail(self):
        return self.tail


# Linked List in Chapter 9
class AltLinkedList(AbstractList):
    """
    A link-based list implementation.
    """

    # Constructor
    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the
        contents of source_collection, if it's present.
        """
        # Uses a circular structure with a sentinel node `head`.
        self.head = TwoWayNode(None)
        self.head.prev = self.head.next = self.head
        super().__init__(source_collection)

    # Accessors
    def __iter__(self):
        cursor = self.head.next
        while cursor != self.head:
            yield cursor.data
            cursor = cursor.next

    def get_node(self, i):
        """
        Helper method: returns node at position i
        Doesn't check the index though.
        """
        if i == len(self):
            return self.head
        if i == len(self) - 1:
            return self.head.prev
        probe = self.head.next
        while i > 0:
            probe = probe.next
            i -= 1
        return probe

    def __getitem__(self, i):
        """
        Preconditions: 0 <= i <= len(self)-1
        Returns the item at position i.
        Raises: IndexError if i is out of bound.
        """
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range.")
        return self.get_node(i).data

    # Mutators
    def __setitem__(self, i, item):
        """
        Preconditions: 0 <= i <= len(self)-1
        Replaces the item at position i.
        Raises: IndexError if i is out of bound.
        """
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range.")
        self.get_node(i).data = item

    def insert(self, i, data):
        """
        Inserts the item at position i.
        """
        if i < 0:
            i = 0
        elif i > len(self):
            i = len(self)
        curr_node = self.get_node(i)
        new_node = TwoWayNode(data, prev=curr_node.prev, next=curr_node)
        curr_node.prev.next = new_node
        curr_node.prev = new_node
        self.size += 1
        self.inc_mod_count()

    def list_iterator(self):
        """
        Returns a list iterator.
        """
        return LinkedListIterator(self)
