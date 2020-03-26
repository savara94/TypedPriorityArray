"""
Module containing TypedPriorityArray
"""
class TypedPriorityArray:
    """
    Typed data structure that keeps elements in order.
    """
    _reversed = False
    def __init__(self, *args, **kwargs):
        try:
            self._l = []
            if len(args) == 0:
                raise TypeError
            if "reversed" in kwargs:
                if kwargs["reversed"]:
                    self._reversed = True
            if len(args) == 1:
                if "__eq__" in args[0].__dict__.keys():
                    self._type = args[0]
                else:
                    raise TypeError
            else:
                self._type = type(args[0])
                for _arg in args:
                    if type(_arg) != self._type:
                        raise TypeError
                    self.insert(_arg)
            self.index = 0
        except AttributeError:
            raise TypeError
    def get_length(self):
        """ Return number of items in collection """
        return len(self._l)
    length = property(get_length)
    def get_type(self):
        """ Return type of collection """
        return self._type
    array_type = property(get_type)
    def get_reversed(self):
        """ Return True if collection is reversed """
        return self._reversed
    def set_reversed(self, _x):
        """ Reversed collection """
        if self._reversed != _x:
            self._l = self._l[::-1]
            self._reversed = _x
    reversed = property(get_reversed, set_reversed)
    def insert(self, _x):
        """ Insert item in collection """
        if self._type != type(_x):
            raise TypeError
        if len(self._l) == 0:
            self._l.append(_x)
        else:
            if self._reversed:
                if _x > (self._l[0]):
                    self._l.insert(0, _x)
                elif _x < self._l[len(self._l) - 1]:
                    self._l.append(_x)
                else:
                    _l1 = 0
                    _l2 = len(self._l) - 1
                    while _l2 >= _l1:
                        _m = (_l1 + _l2) // 2
                        if self._l[_m] < _x:
                            _l1 = _m + 1
                            if _l2 == 1:
                                if self._l[_l1] < _x:
                                    self._l.insert(_l1, _x)
                                else:
                                    self._l.insert(_l1 + 1, _x)
                                break
                        elif self._l[_m] > _x:
                            _l2 = _m - 1
                            if _l2 <= _l1:
                                if self._l[_l1] < _x:
                                    self._l.insert(_l1, _x)
                                else:
                                    self._l.insert(_l1 + 1, _x)
                                break
                        else:
                            self._l.insert(_m, _x)
                            break
            else:
                if _x < (self._l[0]):
                    self._l.insert(0, _x)
                elif _x > self._l[len(self._l) - 1]:
                    self._l.append(_x)
                else:
                    _l1 = 0
                    _l2 = len(self._l) - 1
                    while _l1 <= _l2:
                        _m = (_l1 + _l2) // 2
                        if self._l[_m] < _x:
                            _l1 = _m + 1
                            if _l1 == _l2:
                                if self._l[_l1] > _x:
                                    self._l.insert(_l1, _x)
                                else:
                                    self._l.insert(_l1 + 1, _x)
                                break
                        elif self._l[_m] > _x:
                            _l2 = _m - 1
                            if _l2 <= _l1:
                                if self._l[_l1] > _x:
                                    self._l.insert(_l1, _x)
                                else:
                                    self._l.insert(_l1 + 1, _x)
                                break
                        else:
                            self._l.insert(_m, _x)
                            break
    def pop(self, _x):
        """ Remove item x from collection """
        return self._l.pop(_x)
    def contains(self, _x):
        """ If item x is in collestion return True, else return False """
        return _x in self._l
    def index_of(self, _x):
        """ Return index of item x if item x is in collection """
        if self._l.contains(_x):
            return self._l.index(_x)
        return -1
    def __contains__(self, _x):
        """ If item x is in collestion return True, else return False """
        return self.contains(_x)
    def __iter__(self):
        """ Return iterator """
        return iter(self._l)
    def next(self):
        """ Return a next item """
        if self.index >= len(self._l):
            raise StopIteration
        _x = self._l[self.index]
        self.index += 1
        return _x
    def __getitem__(self, _x):
        return self._l[_x]
    def __len__(self):
        return len(self._l)
    def __str__(self):
        if self.length == 0:
            return "[]"
        _str = "[" + str(self._l[0])
        _x = 1
        _y = " <= "
        if self._reversed:
            _y = " >= "
        while _x < len(self._l):
            _str += _y + str(self._l[_x])
            _x += 1
        return _str + "]"
    def __repr__(self):
        return self.__str__()
        