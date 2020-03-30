"""
Module containing TypedPriorityArray
"""
import inspect

class IteratorTypedPriorityArray():
    '''
    Iterator for class
    '''
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

class TypedPriorityArray():
    """
    Typed data structure that keeps elements in order.
    """
    def __init__(self, *args, **kwargs):
        length = len(args)
        operators = ["__eq__", "__lt__", "__gt__"]
        a_cmp = None
        a_reversed = False
        _initial_elements = []
        self._elem = []

        if 'cmp' in kwargs:
            a_cmp = kwargs.get('cmp')
        self.cmp = a_cmp
        if 'reversed' in kwargs:
            a_reversed = kwargs.get('reversed')
        self.reversed = a_reversed
        if length == 1 and (isinstance(args[0], type) or inspect.isclass(args[0])):
            self._type = args[0]
        elif length > 1 and all(isinstance(x, type(args[0])) for x in args):
            self._type = type(args[0])
            _initial_elements = [i for i in args]

        else:
            raise TypeError('Provide one argument representing type or more elements same type')
        if all(elem in self._type.__dict__.keys() for elem in operators):
            pass
        elif a_cmp is not None:
            pass
        else:
            raise TypeError('Type provided must have operators <, > and == or cmp keyword')
        if len(_initial_elements) != 0:
            for i in _initial_elements:
                self.insert(i)

    @property
    def length(self):
        '''
        Returns number of elements
        '''
        return len(self._elem)

    @property
    def array_type(self):
        '''
        Returns type of elements
        '''
        return self._type

    @property
    def reversed(self):
        '''
        Returns value of reversed.
        '''
        return self._reversed

    @reversed.setter
    def reversed(self, descending):
        if isinstance(descending, bool):
            if hasattr(self, 'reversed') and descending != self.reversed:
                self._elem = [i for i in reversed(self._elem)]
            self._reversed = descending
        else:
            raise TypeError("Reversed value must be bool")


    def compare(self, element1, element2):
        '''
        Compares two elements
        '''
        if self.cmp is None:
            if element1 > element2:
                return 1
            if element1 < element2:
                return -1
            return 0
        return self.cmp(element1, element2)


    def insert(self, element):
        '''
        Inserts new element in tpa
        '''
        index_element = len(self._elem)
        num = len(self._elem)
        if isinstance(element, self.array_type):
            for i in self._elem:
                if not self.reversed:
                    if self.compare(i, element) > 0 or self.compare(i, element) == 0:
                        index_element = self._elem.index(i)
                        num -= 1
                else:
                    if self.compare(element, i) > 0 or self.compare(element, i) == 0:
                        index_element = self._elem.index(i)
                        num -= 1
            if num == 0:
                index_element = 0
            self._elem.insert(index_element, element)
            print(index_element)
            return self._elem
        raise TypeError("Element must be {}".format(str(self.array_type)))


    def pop(self, index):
        '''
        Returns and removes element on this index.
        '''
        max_index = self.length - 1
        if index < max_index:
            return self._elem.pop(index)
        raise IndexError("Index out of range, max index is {}".format(str(max_index)))

    def index_of(self, element):
        '''
        Returns index of an element. Returns -1 if element not found.
        '''
        if self.contains(element):
            return self._elem.index(element)
        return -1

    def contains(self, element):
        '''
        Returns index of an element. Returns -1 if element not found.
        '''
        return self._elem.__contains__(element)

    def __iter__(self):
        return IteratorTypedPriorityArray(self)

    def __getitem__(self, key):
        return self._elem[key]

    def __len__(self):
        return self.length

    def __str__(self):
        znak = '<='
        if self.reversed:
            znak = '>='
        output = ''
        for i in self._elem:
            output = output + str(i) + ' ' + znak + ' '
        return "[" + output[:-4] + "]"

    def __repr__(self):
        return self.__str__

    def __contains__(self, element):
        return self.contains(element)
