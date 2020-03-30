"""
Module containing TypedPriorityArray
"""

class TypedPriorityArray(object):
    """
    Typed data structure that keeps elements in order.
    """
    def __init__(self, *args, **kwargs):
        self.tpaList=[]

        if length==1:
            self.tpaList=args[0]
            if isinstance(self, array_type)
                return true
        else: length>1:
            if reversed in kwargs and isinstance(reversed, bool)
                return self.reversed
            if cmp in kwargs

    @property
    def length(self):
        return len(self.tpaList)

    @property
    def array_type(self):
        if isinstance (self.tpaList, int):
            return int
        elif isinstance(self.tpaList, list):
            return list
        else:
            return object 

    @property
    def reversed(self):
        return self.tpaList.reverse

    @reversed.setter
    def reversed(self, descending):
        descending=self.reversed

    def insert(self, element):
        raise NotImplementedError

    def pop(self, index):
        return self.tpaList.pop(index)

    def index_of(self, element):
        if self.contains(element):
            return self.tpaList.index(element)
    #else:
    def contains(self, element):
        return self.tpaList.__contains__(element)        
#===============================================================
    def append(self, element):
        self.tpaList.append(element)
#===============================================================
    def __iter__(self):
        raise NotImplementedError

    def __getitem__(self, key):
        return self.tpaList[key]

    def __len__(self):
        return self.length

    def __str__(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

    def __contains__(self, element):
        return element in self.tpaList


a=TypedPriorityArray()
a.append(10)
a.append(20)
a.append(30)
a.append(90)
a.append(70)
a.append(50)
a.__getitem__(2)
a.contains(30)
a.index_of(30)
a.pop(2)
a.reversed

print(a.__len__())
print(a.array_type())
print(a[4])
print(a.__getitem__(2))
print( 40 in a)
print(a.index_of(30))
print(a.pop(2))
print(a.__getitem__(0))
print(a.__getitem__(1))
print(a.__getitem__(2))
print(a.__getitem__(3))
print(a.reversed)
