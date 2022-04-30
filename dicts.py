from abstract_dict import Entry, AbstractDict
from arrays import Array
from array_list import ArraySortedList, ArrayList
from linked_lists import AltLinkedList
from linked_bst import LinkedBST
from nodes import Node


class ArraySortedDict(AbstractDict):
    """
    A dictionary implementation based on ArraySortedList.
    """

    # Constructor
    def __init__(self, keys=None, values=None):
        self.clear()
        AbstractDict.__init__(self, keys, values)

    # Accessors
    def __iter__(self):
        """
        Supports iteration over a view of self.
        """
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor].key
            cursor += 1

    def __getitem__(self, key):
        """
        Returns the value associated with key.
        Precondition: The key is in self.
        Raises KeyError if the key is not in self.
        """
        index = self.get_index(key)
        if index == -1:
            raise KeyError(f"Missing key: {key}")
        return self.items[index].value

    def get_index(self, key):
        """
        Helper method for finding the index of key.
        """
        left = 0
        right = len(self) - 1
        while left <= right:
            mid = (left + right) // 2
            if key == self.items[mid].key:
                return mid
            elif key > self.items[mid].key:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    # Mutators
    def clear(self):
        """
        Makes self become empty.
        """
        self.items = ArraySortedList()
        self.size = 0

    def __setitem__(self, key, value):
        """
        If the key is not in self, add a new entry with the key and value.
        Otherwise, replace the old value of key with the new value.
        """
        index = self.get_index(key)
        if index == -1:
            self.items.add(Entry(key, value))
            self.size += 1
        else:
            self.items[index].value = value

    def pop(self, key):
        """
        Removes the key and returns the value associated with key.
        Precondition: The key is in self.
        Raises KeyError if the key is not in self.
        """
        index = self.get_index(key)
        if index == -1:
            raise KeyError(f"Missing key: {key}")
        entry = self.items.pop(index)
        self.size -= 1
        return entry.value


class ArrayDict(ArraySortedDict):
    """
    A dictionary implementation based on ArrayList.
    Inherent most methods from ArraySortedDict.
    """

    # Constructor
    def __init__(self, keys=None, values=None):
        self.clear()
        AbstractDict.__init__(self, keys, values)

    # Accessors
    def get_index(self, key):
        """
        Helper method for finding the index of key.
        """
        cursor = 0
        while cursor < len(self):
            if key == self.items[cursor].key:
                return cursor
            cursor += 1
        return -1

    # Mutators
    def clear(self):
        """
        Makes self become empty.
        """
        self.items = ArrayList()
        self.size = 0


class LinkedDict(AbstractDict):
    """
    A dictionary implementation based on linked list.
    """

    # Constructor
    def __init__(self, keys=None, values=None):
        self.clear()
        AbstractDict.__init__(self, keys, values)

    # Accessors
    def __iter__(self):
        """
        Supports iteration over a view of self.
        """
        probe = self.items.head.next
        while probe is not self.items.head:
            yield probe.data.key
            probe = probe.next

    def __getitem__(self, key):
        """
        Returns the value associated with key.
        Precondition: The key is in self.
        Raises KeyError if the key is not in self.
        """
        pointer = self.get_node(key)
        if pointer is None:
            raise KeyError(f"Missing key: {key}")
        return pointer.data.value

    def get_node(self, key):
        """
        Helper method for finding the node of key.
        """
        probe = self.items.head.next
        while probe is not self.items.head:
            if key == probe.data.key:
                return probe
            probe = probe.next
        return None

    def get_index(self, key):
        """
        Helper method for finding the index of key.
        """
        probe = self.items.head.next
        index = 0
        while probe is not self.items.head:
            if key == probe.data.key:
                return index
            probe = probe.next
            index += 1
        return None

    # Mutators
    def clear(self):
        """
        Makes self become empty.
        """
        self.items = AltLinkedList()
        self.size = 0

    def __setitem__(self, key, value):
        """
        If the key is not in self, add a new entry with the key and value.
        Otherwise, replace the old value of key with the new value.
        """
        pointer = self.get_node(key)
        if pointer is None:
            self.items.insert(len(self), Entry(key, value))
            self.size += 1
        else:
            pointer.data.value = value

    def pop(self, key):
        """
        Removes the key and returns the value associated with key.
        Precondition: The key is in self.
        Raises KeyError if the key is not in self.
        """
        index = self.get_index(key)
        if index is None:
            raise KeyError(f"Missing key: {key}")
        entry = self.items.pop(index)
        self.size -= 1
        return entry.value


class HashDict(AbstractDict):
    """
    A dictionary implementation based on hashing
    with bucket/chaining to resolve collisions.
    """

    # Class Variable
    DEFAULT_CAPACITY = 29

    # Constructor
    def __init__(self, keys=None, values=None, capacity=None):
        self.capacity = HashDict.DEFAULT_CAPACITY if capacity is None else capacity
        self.array = Array(self.capacity)
        self.found_node = self.prior_node = None
        self.index = -1
        AbstractDict.__init__(self, keys, values)

    # Accessors
    def __contains__(self, key):
        """
        Returns True if key is in self, or False otherwise.
        """
        self.index = abs(hash(key)) % len(self.array)
        self.prior_node = None
        self.found_node = self.array[self.index]
        while self.found_node is not None:
            if key == self.found_node.data.key:
                return True
            self.prior_node = self.found_node
            self.found_node = self.found_node.next
        return False

    def __iter__(self):
        """
        Supports iteration over a view of self.
        """
        for index in range(len(self.array)):
            node = self.array[index]
            while node is not None:
                yield node.data.key
                node = node.next

    def __getitem__(self, key):
        """
        Returns the value associated with key.
        Precondition: The key is in self.
        Raises KeyError if the key is not in self.
        """
        if key in self:
            return self.found_node.data.value
        else:
            raise KeyError(f"Missing key: {key}")

    def load_factor(self):
        """
        Returns the load factor of self.
        """
        return self.size / self.capacity

    # Mutators
    def clear(self):
        self.array = Array(self.capacity)
        self.found_node = self.prior_node = None
        self.index = -1
        self.size = 0

    def __setitem__(self, key, value):
        """
        If the key is not in self, add a new entry with the key and value.
        Otherwise, replace the old value of key with the new value.
        Rehash the dict if the load factor is over 0.5.
        """
        if key in self:
            self.found_node.data.value = value
        else:
            new_node = Node(Entry(key, value), self.array[self.index])
            self.array[self.index] = new_node
            self.size += 1
        while self.load_factor() > 0.5:
            self.rehash()

    def pop(self, key):
        """
        Removes the key and returns the value associated with key.
        Precondition: The key is in self.
        Raises KeyError if the key is not in self.
        """
        if key in self:
            value = self.found_node.data.value
            if self.prior_node is None:
                self.array[self.index] = None
            else:
                self.prior_node.next = self.found_node.next
            self.size -= 1
            return value
        else:
            raise KeyError(f"Missing key: {key}")

    def rehash(self):
        """
        Increases the capacity by 2 and reload all entries.
        """
        # Extract all entries
        entries = []
        for index in range(len(self.array)):
            node = self.array[index]
            while node is not None:
                entries.append(node.data)
                node = node.next
        # Increase capacity and clear self.
        self.capacity *= 2
        self.clear()
        # Add entries back to self.
        for entry in entries:
            self[entry.key] = entry.value


class TreeSortedDict(AbstractDict):
    """
    A dictionary implementation based on linked BST.
    Inherent most methods from TreeSortedBag.
    Inherent set-specific methods from AbstractSet.
    """

    # Constructor
    def __init__(self, keys=None, values=None):
        self.clear()
        AbstractDict.__init__(self, keys, values)

    # Accessor methods
    def __contains__(self, key):
        # Create a probe entry for easy checking
        item = Entry(key, None)
        return item in self.items

    def __iter__(self):
        """
        Supports iteration over a view of self.
        """
        return iter(map(lambda node: node.key, self.items.inorder()))

    def __getitem__(self, key):
        """
        Returns the value associated with key.
        Precondition: The key is in self.
        Raises KeyError if the key is not in self.
        """
        entry = Entry(key, None)
        if entry not in self.items:
            raise KeyError(f"Missing key: {key}")
        return self.items.find(entry).value

    # Mutator methods
    def clear(self):
        self.items = LinkedBST()
        self.size = 0

    def __setitem__(self, key, value):
        entry = Entry(key, value)
        if key in self:
            self.items.replace(entry, entry)
        else:
            self.items.add(entry)
            self.size += 1

    def pop(self, key):
        """
        Removes the key and returns the value associated with key.
        Precondition: The key is in self.
        Raises KeyError if the key is not in self.
        """
        if key not in self:
            raise KeyError(f"Missing key: {key}")
        else:
            value = self.items.remove(Entry(key, None))
            self.size -= 1
            return value
