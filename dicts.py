from abstract_dict import Entry, AbstractDict
from array_list import ArraySortedList, ArrayList
from linked_lists import AltLinkedList


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
