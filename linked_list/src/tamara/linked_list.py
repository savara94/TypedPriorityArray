class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedListIterator(object):
    def __init__(self, linked_list, bool_reversed):
        self.linked_list = linked_list
        self.reversed = bool_reversed
        if bool_reversed:
            self.index = len(linked_list) - 1
        else:
            self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.linked_list) or self.index<0:
            raise StopIteration
        data = self.linked_list[self.index]
        if self.reversed:
            self.index = self.index - 1
        else:
            self.index = self.index + 1
        return data


class LinkedList(object):
    def __init__(self, *args, **kwargs):
        args_count = len(args)
        self.head = None
        self.__max_size__ = None
        self.__count__ = 0
        if 'max_size' in kwargs:
            if isinstance(kwargs['max_size'], int):
                self.__max_size__ = kwargs['max_size']
            else:
                raise TypeError('Max_size must be integer.')
        if args_count == 1:
            if '__iter__' in dir(args[0]):
                    self.append(args[0])
        elif args_count > 1:
            for arg in args:
                self.append(arg)

    @property
    def max_size(self):
        return self.__max_size__

    @property
    def __max_size__(self):
        return self.__max_size

    @__max_size__.setter
    def __max_size__(self, value):
        self.__max_size = value

    @property
    def length(self):
        return self.__count__

    @property
    def __count__(self):
        return self._count_

    @__count__.setter
    def __count__(self, value):
        self._count_ = value

    def append(self, element):
        if self.length >= self.max_size:
            raise MemoryError('Collection length exceeded maximum size.')
        if self.length == 0:
            self.head = Node(element)
        else:
            node = self.__get_node__(self.length - 1)
            node.next_node = Node(element)
        self.__count__ = self.__count__ + 1

    def insert(self, index, element):
        if self.length >= self.max_size:
            raise MemoryError('Collection length exceeded maximum size.')
        new_node = Node(element)
        if index == 0:
            new_node.next_node = self.head
            self.head = new_node
        elif index == self.length:
            self.append(element)
        else:
            current_node = self.__get_node__(index)
            new_node.next_node = current_node
            previous_node = self.__get_node__(index-1)
            previous_node.next_node = new_node
        self.__count__ = self.__count__ + 1

    def pop(self, index):
        node_to_erase = self.__get_node__(index)
        element = node_to_erase.data
        if index == 0:
            self.head = self.__get_node__(1)
        else:
            previous_node = self.__get_node__(index-1)
            previous_node.next_node = node_to_erase.next_node
        self.__count__ = self.__count__ - 1
        return element

    def __get_node__(self, index):
        if index > self.length:
            raise IndexError('Index out of range')
        current_node = self.head
        i = 0
        while i < self.length:
            if i == index:
                return current_node
            current_node = current_node.next_node
            i = i + 1

    def index_of(self, element):
        i = 0
        while i < self.length:
            if self[i] == element:
                return self[i]
            i = i + 1    
        return -1   

    def __contains__(self, item):
        current_node = self.head
        i = 0
        while i < self.length :
            if current_node.data == item:
                return True
            else:
                current_node = current_node.next_node
                i = i + 1
        return False

    def __getitem__(self, index):
        node = self.__get_node__(index)
        return node.data

    def __len__(self):
        return self.length

    def __iter__(self):
        return LinkedListIterator(self, False)

    def __reversed__(self):
        return LinkedListIterator(self, True)

    def __str__(self):
        return '=>'.join(map(str, self))

    def __repr__(self):
        return '=>'.join(map(str, self))
