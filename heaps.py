from array_list import ArrayList
from abstract_collection import AbstractCollection


class ArrayHeap(AbstractCollection):
    """
    A minimal heap implementation based on list.
    """

    # Constructor
    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the
        contents of source_collection, if it's present.
        """
        self.heap = ArrayList()
        super().__init__(source_collection)

    # Accessors
    def __len__(self):
        return len(self.heap)

    def __iter__(self):
        """
        Support (sorted) iteration using a backup list.
        """
        self_copy = ArrayList(self.heap)
        result_list = []
        while not self.heap.is_empty():
            result_list.append(self.pop())
        self.heap = self_copy
        self.size = len(self.heap)
        return iter(result_list)

    def __str__(self):
        def str_helper(position, level):
            result = ""
            if position < len(self):
                result += str_helper(2 * position + 2, level + 1)
                result += "| " * level
                result += str(self.heap[position]) + "\n"
                result += str_helper(2 * position + 1, level + 1)
            return result
        return str_helper(0, 0)

    def __contains__(self, item):
        cursor = 0
        while cursor < len(self):
            curr_item = self.heap[cursor]
            if item < curr_item:
                return False
            left_cursor = 2 * cursor + 1
            right_cursor = 2 * cursor + 2
        return False

    def __add__(self, other_heap):
        """
        Support addition operation.
        """
        result_heap = ArrayHeap(self.heap)
        for item in other_heap:
            result_heap.add(item)
        return result_heap

    def __eq__(self, other):
        """
        Check if two objects are equal.
        """
        if type(self) != type(other):
            return False
        if len(self) != len(other):
            return False
        for k in range(len(self)):
            if self.heap[k] != other.heap[k]:
                return False
        return True

    def peek(self):
        """
        Precondition: heap is not empty.
        Returns the top item of the heap.
        Raises: AttributeError if heap is empty.
        """
        if self.is_empty():
            raise AttributeError("The heap is empty.")
        return self.heap[0]

    def add(self, item):
        """
        Add the item to the appropriate place in the heap.
        """
        # Add the item to the end first
        self.heap.add(item)
        self.size += 1
        # Then adjust its position.
        # It either reaches the top, or is bigger than its parent.
        cursor = len(self.heap) - 1
        while cursor > 0:
            parent_cursor = (cursor - 1) // 2
            parent_item = self.heap[parent_cursor]
            if item < parent_item:
                self.heap[cursor] = parent_item
                self.heap[parent_cursor] = item
                cursor = parent_cursor
            else:
                break

    def pop(self):
        """
        Precondition: heap is not empty.
        Returns and removes the top item of the heap.
        Raises: AttributeError if heap is empty.
        """
        if self.is_empty():
            raise AttributeError("The heap is empty.")
        # Retrieve the top item for the return value.
        top = self.heap[0]
        bottom = self.heap.pop(len(self) - 1)
        self.size -= 1
        if len(self) == 0:
            # Special case: nothing left - no further adjustments needed.
            return top
        else:
            # Regular case : move the last item to the top, and then adjust its position.
            self.heap[0] = bottom
            cursor = 0
            last_cursor = len(self) - 1
            while True:
                # Find its two childs, move the smaller one to the top.
                left_cursor = 2 * cursor + 1
                right_cursor = 2 * cursor + 2
                # Case 1: no childs, it reaches the end - break immediately.
                if left_cursor > last_cursor:
                    break
                # Case 2: only left child - record the position of the left child.
                elif right_cursor > last_cursor:
                    swap_cursor = left_cursor
                # Case 3: both childs exist - record the position of the minimal one.
                else:
                    left_child = self.heap[left_cursor]
                    right_child = self.heap[right_cursor]
                    swap_cursor = left_cursor if left_child < right_child else right_cursor
                # Swap if neccesary.
                swap_item = self.heap[swap_cursor]
                if swap_item < bottom:
                    self.heap[swap_cursor] = bottom
                    self.heap[cursor] = swap_item
                    cursor = swap_cursor
                else:
                    break
            return top
