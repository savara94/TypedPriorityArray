'''
    Module Containing Linked List
'''
class LinkedList(object):
    '''
        Linked List data structure
    '''
    def __init__(self, *args, **kwargs):
        if not args:
            raise ValueError('You must specify arguments')

        self.__max_size = kwargs['max_size'] if 'max_size' in kwargs else 5
        self.__linked_list = []

        if iter(args):
            for x in args:
                self._append_all(x)

    def _append_all(self, collection):
        for element in collection:
            self.append(element)

    @property
    def length(self):
        ''' Returns length of linked_list '''
        return len(self)

    @property
    def max_size(self):
        ''' Returns max size of linked_list '''
        return self.__max_size

    def insert(self, index, element):
        ''' Is not implemented '''
        raise NotImplementedError

    def pop(self, index):
        ''' Removes element from linked list at specified index '''
        self.__linked_list.pop(index)

    def index_of(self, element):
        ''' Returns index of requested element '''
        return self.__linked_list.index(element)

    def append(self, element):
        ''' Appends element to linked_list '''
        self.__linked_list.append(element)

    def inverse(self):
        ''' Not implemented '''
        raise NotImplementedError

    def __reversed__(self):
        raise NotImplementedError

    def __contains__(self, element):
        return element in self.__linked_list

    def __iter__(self):
        return iter(self.__linked_list)

    def __getitem__(self, key):
        return self.__linked_list[key]

    def __len__(self):
        return len(self.__linked_list)

    def __str__(self):
        return ' -> '.join(str(x) for x in self.__linked_list)

    def __repr__(self):
        return str(self)
