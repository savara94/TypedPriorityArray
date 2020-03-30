"""
Module containing TypedPriorityArray
"""

class TypedPriorityArray(object):
    """
    Typed data structure that keeps elements in order.
    """
    def __init__(self, *args, **kwargs):
        raise NotImplementedError

    @property
    def length(self):
        raise NotImplementedError

    @property
    def array_type(self):
        raise NotImplementedError

    @property
    def reversed(self):
        raise NotImplementedError

    @reversed.setter
    def reversed(self, descending):
        raise NotImplementedError

    def insert(self, element):
        raise NotImplementedError

    def pop(self, index):
        raise NotImplementedError

    def index_of(self, element):
        raise NotImplementedError

    def contains(self, element):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __getitem__(self, key):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

    def __contains__(self, element):
        raise NotImplementedError
