class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        class_name = str(type(self).__name__)
        return class_name + "(" + str(self.data) + ")"

    def __repr__(self):
        return str(self)


class TwoWayNode(Node):
    def __init__(self, data, prev=None, next=None):
        Node.__init__(self, data, next=next)
        self.prev = prev
