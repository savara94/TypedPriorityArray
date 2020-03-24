"""
Module containing TypedPriorityArray
"""
import inspect


class IteratorTypedPriorityArray(object):
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        rv = self.data[self.index]
        self.index += 1
        return rv

class TypedPriorityArray(object):
    """
    Typed data structure that keeps elements in order.
    """
    def __init__(self, *args, **kwargs):
        
        length = len(args)
        operators = ["__eq__", "__lt__", "__gt__"]
        a_cmp = None
        a_reversed = False
        _elements = []
        if 'cmp' in kwargs:
            a_cmp = kwargs.get('cmp')
        if 'reversed' in kwargs:
            a_reversed = kwargs.get('reversed')
        if length == 1 and (isinstance(args[0], type) or inspect.isclass(args[0])):
            self._type = args[0]
            self._count = 0
        elif length > 1 and all(isinstance(x, type(args[0])) for x in args):
            self._type = type(args[0])
            self._count = len(args)
            _elements = [i for i in args]
        else:
            raise TypeError('You must provide either one argument representing type or more elements same type')    
        
        if all(elem in self._type.__dict__.keys() for elem in operators): 
            pass       
            
        elif a_cmp!= None:
            pass
        
        else:
            raise TypeError('Type provided must have operators <, > and == or defined rule in cmp keyword')
        #raise NotImplementedError

        self.cmp = a_cmp
        self._elem = _elements
        self.reversed = a_reversed

    @property
    def length(self):
        return self._count
        

    @property
    def array_type(self):
        return self._type

    @property
    def reversed(self):
        return self._reversed

    @reversed.setter
    def reversed(self, descending):
        if isinstance(descending, bool):
            if hasattr(self, 'reversed') and descending != self.reversed:
                self._elem = [i for i in reversed(self._elem)]
            
            self._reversed = descending
        else:
            raise TypeError("Reversed value must be bool")
        

    def insert(self, element):
        raise NotImplementedError

    def pop(self, index):
        max_index = self.length - 1
        if index < max_index:
            self._count = self._count - 1
            return self._elem.pop(index)
        else:
            raise IndexError("Index out of range, max index is {}".format(str(max_index)))

    def index_of(self, element):
        if self.contains(element):
            return self._elem.index(element)
        return -1

    def contains(self, element):
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
        return output[:-4]
        
    def __repr__(self):
        return self.__str__

    def __contains__(self, element):
        return self.contains(element)

    
    

