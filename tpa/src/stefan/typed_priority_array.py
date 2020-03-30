"""
Module containing TypedPriorityArray
"""

class TypedPriorityArray(object):
    """
    Typed data structure that keeps elements in order.
    """
    def __init__(self, *args, **kwargs):
        if not args:
            raise ValueError('You must specify at least one argument.')

        first_arg = args[0]
        self.__cmp = kwargs['cmp'] if 'cmp' in kwargs else None
        self.__reversed = False
        self.__rev = -1
        self.__array_type = first_arg if isinstance(first_arg, type) else type(first_arg)
        self.__container = []

        self.reversed = kwargs['reversed'] if 'reversed' in kwargs else False

        if self.__cmp is None:
            if not TypedPriorityArray._is_valid_class_type(self.__array_type):
                raise TypeError("You must either specify class \
                     with <, >, == operator or cmp argument.")
            self.__cmp = lambda x, y: self.__rev if x > y else (-self.__rev if x < y else 0)

        if len(args) == 1:
            if not isinstance(first_arg, type):
                raise TypeError('Use only one *args if you specify type.')
        else:
            if not self._is_args_valid(args):
                raise TypeError('All elements must be of the same type.')
            self._insert_all(args)

    def _insert_all(self, collection):
        for element in collection:
            self.insert(element)

    def _is_args_valid(self, args):
        for element in args:
            if type(element) != self.__array_type:
                return False

        return True

    def _bin_search(self, element):
        length = self.length
        max_bound = length - 1
        min_bound = 0
        index = 0
        while min_bound <= max_bound:
            index = (max_bound + min_bound) // 2
            curr = self.__container[index]
            if self.__cmp(element, curr) == 0:
                return (index, True)
            elif self.__cmp(element, curr) > 0:
                min_bound = index + 1
            else:
                max_bound = index - 1

        if length >= 1:
            if self.__cmp(element, self.__container[index]) > 0:
                index = index + 1

        return (index, False)

    @staticmethod
    def _is_valid_class_type(class_type):
        try:
            dummy = class_type
            results = [
                class_type.__lt__(dummy, dummy),
                class_type.__gt__(dummy, dummy),
                class_type.__eq__(dummy, dummy),
            ]
            if NotImplemented in results:
                return False
        except TypeError:
            return True
        except:
            return False

        return True

    @property
    def length(self):
        return len(self)

    @property
    def array_type(self):
        return self.__array_type

    @property
    def reversed(self):
        return self.__reversed

    @reversed.setter
    def reversed(self, descending):
        if self.__reversed != descending:
            self.__container.reverse()

        self.__reversed = descending
        self.__rev = -1 if descending else 1

    def insert(self, element):
        '''for i, curr in enumerate(self.__container):
            if self.__cmp(curr, element) >= 0:
                self.__container.insert(i, element)
                return
        self.__container.append(element)
        '''
        index, _contains = self._bin_search(element)
        self.__container.insert(index, element)

    def pop(self, index):
        return self.__container.pop(index)

    def index_of(self, element):
        return self.__container.index(element)

    def contains(self, element):
        return element in self

    def __iter__(self):
        return iter(self.__container)

    def __getitem__(self, key):
        return self.__container[key]

    def __len__(self):
        return len(self.__container)

    def __str__(self):
        sign = '>=' if self.__reversed else '<='
        return str(self.__container).replace(',', f' {sign}')

    def __repr__(self):
        return str(self)

    def __contains__(self, element):
        return self._bin_search(element)[1]