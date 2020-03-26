"""
Module containing TypedPriorityArray
"""

class TypedPriorityArray(object):
    """
    Typed data structure that keeps elements in order.
    """
    def __init__(self, *args, **kwargs):
        self.arg = list(args)
        self.kwarg = kwargs

        #self.my_list = list(self.arg)
        #raise NotImplementedError

    @property
    def length(self):
        return self.__len__()
        #return len(self.my_list)
        #raise NotImplementedError

    @property
    def array_type(self):
        return type(self.arg)
        #raise NotImplementedError

    @property
    def reversed(self):
        raise NotImplementedError

    @reversed.setter
    def reversed(self, descending):
        raise NotImplementedError

    def insert(self, element):
        raise NotImplementedError

    def pop(self, index):
        #self.arg = self.arg[:index] + self.arg[index+1:]
        return self.arg.pop(index)

    def contains(self, element):
        return self.__contains__(element)
        #raise NotImplementedError

    def index_of(self, element):
        return self.__getitem__(element)
        #ne vraca -1
        #raise NotImplementedError

    def __contains__(self, element):
        cont = element in self.arg
        return cont
        #raise NotImplementedError

    def __iter__(self):
        i = self.arg.__iter__()
        return i
        #raise NotImplementedError

    def __getitem__(self, key):
        index = self.arg.index(key)
        return index
        # ne vraca -1
        #raise NotImplementedError

    def __len__(self):
        return self.arg.__len__()
        #raise NotImplementedError

    def __str__(self):
        if reversed == True:
            return '<='.join(str(x) for x in self.arg)
        else:
            return '=>'.join(str(x) for x in self.arg)
        #raise NotImplementedError

    def __repr__(self):
        return self.__str__()
        #raise NotImplementedError
