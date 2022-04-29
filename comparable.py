class Comparable(object):
    def __init__(self, data, priority=1):
        self.data = data
        self.priority = priority

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.priority == other.priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __ge__(self, other):
        return self.priority >= other.priority

    def get_data(self):
        return self.data

    def get_priority(self):
        return self.priority
