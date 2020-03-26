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
            raise TypeError('You must provide either one argument representing type or more elements same type')    
        
        if all(elem in self._type.__dict__.keys() for elem in operators):
            pass      
            
        elif a_cmp!= None:
            pass
        
        else:
            raise TypeError('Type provided must have operators <, > and == or defined rule in cmp keyword')
        if len(_initial_elements) !=0:
            for i in _initial_elements:
                self.insert(i)
        

    @property
    def length(self):
        return len(self._elem)
        

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

    @staticmethod
    def Compare(element1, element2):
        if element1 > element2:
            return 1
        elif element1 < element2:
            return -1
        else:
            return 0

    def insert(self, element):
        index_element = len(self._elem)
        num = len(self._elem)
        if type(element) == self.array_type:
            if index_element != 0:
                for i in self._elem:
                    if self.reversed == False:
                       if TypedPriorityArray.Compare(i, element) > 0 or TypedPriorityArray.Compare(i, element) == 0:
                            index_element = self.index_of(i)
                            num -=1
                    else: 
                        if TypedPriorityArray.Compare(element, i) > 0 or TypedPriorityArray.Compare(element, i) == 0:
                            index_element = self.index_of(i)
                            num -=1      
            if (num == 0):
                index_element = 0
            self._elem.insert(index_element, element)
            return self._elem
        else:
            raise TypeError("Element must be {}".format(str(self.array_type))) 

 

    def pop(self, index):
        max_index = self.length - 1
        if index < max_index:
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
        return "[" + output[:-4] + "]"
        
    def __repr__(self):
        return self.__str__

    def __contains__(self, element):
        return self.contains(element)

    
    

