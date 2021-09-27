class Array(object):
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        self.fill_value = fill_value
        self.logical_size = 0
        self.capacity = capacity
        for k in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        valid_items = [self.items[k] for k in range(self.size())]
        return str(valid_items)

    # This should base on logical size, not physical size
    # def __iter__(self):
    #     return iter(self.items)

    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError(f"Array index {index} out of range.")
        return self.items[index]

    def __setitem__(self, index, new_item):
        if index < 0 or index >= len(self):
            raise IndexError(f"Array assignment index {index} out of range.")
        self.items[index] = new_item

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if self.size() != other.size():
            return False
        for k in range(self.logical_size):
            if self.items[k] != other.items[k]:
                return False
        return True

    def size(self):
        return self.logical_size

    def grow(self):
        for k in range(len(self)):
            self.items.append(self.fill_value)

    def shrink(self):
        new_size = max(self.capacity, len(self) // 2)
        for k in range(len(self) - new_size):
            self.items.pop()

    def insert(self, k, new_item):
        if self.size() == len(self) - 1:
            self.grow()
        if k > self.size():
            self.items[self.size()] = new_item
        else:
            k = max(k, 0)
            for ind in range(self.size() - 1, k - 1, -1):
                self.items[ind + 1] = self.items[ind]
            self.items[k] = new_item
        self.logical_size += 1

    def append(self, new_item):
        return self.insert(self.size(), new_item)

    def pop(self, k):
        if k < 0 or k >= self.size():
            raise IndexError(f"Array pop index {index} out of range.")
        data = self.items[k]
        for ind in range(k, self.size()):
            self.items[ind] = self.items[ind + 1]
        self.items[self.size() - 1] = self.fill_value
        self.logical_size -= 1
        if self.logical_size < len(self) // 4 and len(self) >= 2 * self.capacity:
            self.shrink()
        return data

    # Test methods
    def initialize(self):
        for k in range(len(self)):
            self.items[k] = k + 1
        self.logical_size = len(self)
