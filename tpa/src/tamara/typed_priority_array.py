"""
Module containing TypedPriorityArray
"""
import inspect
 
class TypedPriorityArray(object):
    """
    Typed data structure that keeps elements in order.
    """
    def __init__(self, *args, **kwargs):
        argCount = len(args)
        if argCount == 0:
            raise Exception("No parameters were passed to class initializator.")
        self.__elements__ = []
        self.reversed = False
        self._cmp_func = self.__compare__
        if argCount == 1:
            self.array_type = args[0]
        elif argCount > 1:
            self.array_type = type(args[0])
            for arg in args:
                self.insert(arg)
        if 'reversed' in kwargs:
            self.reversed = kwargs['reversed']
        if 'cmp' in kwargs:
            self.__cmp_func__ = kwargs['cmp']
 
    def __compare__(self, first, second):
        if first < second:
            return -1
        elif first == second:
            return 0
        elif first > second:
            return 1
 
    @property
    def __cmp_func__(self):
        return self._cmp_func
 
    @__cmp_func__.setter
    def __cmp_func__(self, value):
        if callable(value):
            self._cmp_func = value
 
    @property
    def length(self):
        return len(self.__elements__)
 
    @property
    def array_type(self):
        return self.__array_type
 
    @array_type.setter
    def array_type(self,  array_type_val):
        if inspect.isclass(array_type_val):
            comparison_methods = ["__eq__", "__ne__", "__lt__", "__gt__"]
            if all(elem in comparison_methods for elem in dir(array_type_val)):
                self.__array_type = array_type_val
            else:
                raise TypeError('{} is not comparable.'.format(array_type_val))
 
    @property
    def reversed(self):
        return self._reversed
 
    @reversed.setter
    def reversed(self, descending):
        if type(descending) == bool:
            self._reversed = descending
 
    def insert(self, element):
        if isinstance(element, self.array_type):
            inserted = False
            for index, elem in enumerate(self.__elements__, start=1):
                if self.reversed:
                    if self._cmp_func(elem, element) >= 0:
                        self.__elements__.insert(index - 1, element)
                        inserted = True
                        break
                else:
                    if self._cmp_func(elem, element) <= 0:
                        self.__elements__.insert(index - 1, element)
                        inserted = True
                        break;
            if not inserted:
                self.__elements__.append(element)
        else:
            raise TypeError('{0} is not of type {1}.'.format(element, self.array_type))
 
    def pop(self, index):
        self.__elements__.pop(index)
 
    def index_of(self, element):
        return self.__elements__.index(element)
 
    def contains(self, element):
        return element in self.__elements__
 
    def __iter__(self):
        return iter(self.__elements__)
 
    def __getitem__(self, key):
        return self.__elements__[key]
 
    def __len__(self):
        return len(self.__elements__)
 
    def __str__(self):
        chain = self[0]
        for i in self:
            chain = chain + '<=' + str(i)
        return chain
 
    def __repr__(self):
        return repr(self.__elements__)
