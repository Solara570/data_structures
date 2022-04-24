class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        class_name = str(type(self).__name__)
        return class_name + "(" + str(self.data) + ")"

    def __repr__(self):
        """
        Returns the string representation of a non-empty lisp list.
        """
        def build_string(lyst):
            s = ""
            while lyst is not None:
                s += str(lyst.data) + " "
                lyst = lyst.next
            return s.strip()
        return "(" + build_string(self) + ")"


class TwoWayNode(Node):
    def __init__(self, data, prev=None, next=None):
        Node.__init__(self, data, next=next)
        self.prev = prev


class BSTNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
