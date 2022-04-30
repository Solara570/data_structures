from abstract_collection import AbstractCollection


class Entry(object):
    """
    Represents a dictionary entry.
    Supports comparisons by key.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key}: {self.value}"

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self.key == other.key

    def __lt__(self, other):
        if type(self) != type(other):
            return False
        return self.key < other.key

    def __le__(self, other):
        if type(self) != type(other):
            return False
        return self.key <= other.key


class AbstractDict(AbstractCollection):
    """
    An abstract dictionary implementation.
    Only contains common data and method implementations for dictionaries.
    """

    # Constructor
    def __init__(self, keys, values):
        """
        Will copy entries to the dictionary
        from keys and values if they are present.
        """
        super().__init__()
        if keys and values:
            for key, value in zip(keys, values):
                self[key] = value

    # Accessors
    def __str__(self):
        return "{" + ", ".join(map(str, self.entries())) + "}"

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other):
            return False
        if len(self) != len(other):
            return False
        for key in self:
            if key not in other or self[key] != other[key]:
                return False
        return True

    def keys(self):
        """
        Returns an iterator on the keys in self.
        """
        return iter(self)

    def values(self):
        """
        Returns an iterator on the values in self.
        """
        return map(lambda key: self[key], self)

    def entries(self):
        """
        Returns an iterator on the entries in self.
        """
        return map(lambda key: Entry(key, self[key]), self)

    def get(self, key, default_value=None):
        """
        Returns the value associated with key is key is present in self,
        or default_value otherwise.
        """
        return self[key] if key in self else default_value

    def unzip(self):
        """
        Returns a tuple containing the keys and values in self.
        """
        return (list(self.keys()), list(self.values()))

    # Mutators
    def __add__(self, other):
        """
        Returns a dictionary containing the contents
        of both self and other.
        """
        result = type(self)(self.keys(), self.values())
        for key in other:
            result[key] = other[key]
        return result
