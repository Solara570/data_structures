from nodes import Node

EMPTY_LIST = None


def is_empty(lyst):
    """
    Returns True if lyst is empty or False otherwise.
    """
    return lyst is EMPTY_LIST


def first(lyst):
    """
    Precondition: lyst is not empty.
    Returns the item at the head of lyst.
    Raises: ValueError if lyst is empty.
    """
    return lyst.data


def rest(lyst):
    """
    Precondition: lyst is not empty.
    Returns a list of the items after the first item of lyst.
    Raises: ValueError if lyst is empty.
    """
    return lyst.next


def cons(data, lyst):
    """
    Returns a list whose head is the data and tail is the lyst.
    """
    return Node(data, next=lyst)


def build_range(lower, upper):
    """
    Precondition: lower <= upper
    Returns a list containing the numbers from lower through upper.
    """
    if lower > upper:
        raise ValueError(f"Lower bound is larger than upper bound.")
    elif lower == upper:
        return cons(lower, EMPTY_LIST)
    else:
        return cons(lower, build_range(lower + 1, upper))


def build_from_array(array):
    """
    Just a helper for testing functions.
    """
    if len(array) == 0:
        return EMPTY_LIST
    else:
        return cons(array[0], build_from_array(array[1:]))


def remove(index, lyst):
    """
    Precondition: 0 <= index < len(lyst)
    Returns a list with the item at index removed.
    """
    if index < 0 or (index > 0 and lyst is None):
        raise IndexError("Index out of bound.")
    if index == 0:
        return rest(lyst)
    else:
        return cons(first(lyst), remove(index - 1, rest(lyst)))


def insert(index, data, lyst):
    """
    Precondition: 0 <= index < len(lyst)
    Returns a list with the data inserted at index.
    """
    if index < 0 or (index > 0 and lyst is None):
        raise IndexError("Index out of bound.")
    if index == 0:
        return cons(data, lyst)
    else:
        return cons(first(lyst), insert(index - 1, data, rest(lyst)))


def equals(lyst1, lyst2):
    """
    Returns True if items in two lists are all equal or False otherwise.
    """
    if lyst1 is EMPTY_LIST and lyst2 is EMPTY_LIST:
        return True
    elif lyst1 is EMPTY_LIST or lyst2 is EMPTY_LIST:
        return False
    elif first(lyst1) != first(lyst2):
        return False
    else:
        return equals(rest(lyst1), rest(lyst2))


def remove_all(data, lyst):
    """
    Returns a list with all the data removed in lyst.
    """
    if lyst is EMPTY_LIST:
        return EMPTY_LIST
    elif first(lyst) == data:
        return remove_all(data, rest(lyst))
    else:
        return cons(first(lyst), remove_all(data, rest(lyst)))


def lisp_map(func, lyst):
    """
    Returns a list of func acting on lyst.
    """
    if lyst is EMPTY_LIST:
        return EMPTY_LIST
    else:
        return cons(func(first(lyst)), lisp_map(func, rest(lyst)))


def lisp_filter(filter_func, lyst):
    """
    Returns a list with all the data in lyst that satisfy filter_func.
    """
    if lyst is EMPTY_LIST:
        return EMPTY_LIST
    elif filter_func(first(lyst)):
        return cons(first(lyst), lisp_filter(filter_func, rest(lyst)))
    else:
        return lisp_filter(filter_func, rest(lyst))
