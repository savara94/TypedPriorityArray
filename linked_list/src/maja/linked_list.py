class _Node:
    """
    Basic object in linked list
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None

class _IteratorLinkedList:
    """
    Iterator for Linked List
    """
    def __init__(self, first):
        self.current = first
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value

class _ReversedIterator:
    '''
    Reversed
    '''
    def __init__(self, first, last):
        self.curr = first
        self.first = first
        self.last = last
    def __iter__(self):
        return self
    def __next__(self):
        if self.last is None:
            raise StopIteration
        while self.curr is not None and self.curr.next != self.last:
            self.curr = self.curr.next
        value = self.last.value
        self.last = self.curr
        self.curr = self.first
        return value

class LinkedList:
    """
    Linked List implementation.
    """
    def __init__(self, *args, **kwargs):
        lenght = len(args)
        elements = []
        self.__len = 0
        self.__head = _Node()
        self.__tail = _Node()
        self.__max = kwargs.get('max_size') if "max_size" in kwargs else None
        if lenght == 1:
            obj = args[0]
            if "__iter__" in type(obj).__dict__.keys():
                elements = list(*args)
            else:
                raise ValueError("That one argument must be iterable")
        elif lenght > 1:
            elements = list(args)
        else:
            raise ValueError("You must provide one iterable object or more objects to insert")
        for i in elements:
            self.append(i)

    @property
    def length(self):
        '''
        Returns number of elements
        '''
        return self.__len

    @property
    def max_size(self):
        '''
        Returns max size of list
        '''
        return self.__max

    def _find_node(self, index):
        if index >= self.length:
            raise IndexError("Index out of range")
        if index == self.length - 1:
            return self.__tail
        curr = self.__head.next
        curr_index = 0
        while curr_index != index:
            curr = curr.next
            curr_index += 1
        return curr

    def _search(self, elem):
        for i, item in enumerate(self):
            if item == elem:
                return(i, True)
        return(-1, False)

    def _increase_len(self):
        if self.__len == self.max_size:
            raise MemoryError("Max size reached")
        self.__len += 1

    def insert(self, index, element):
        new_node = _Node(element)
        self._increase_len()
        if index >= self.length:
            self.append(element)
        elif index <= 0:
            new_node.next = self.__head.next
            self.__head.next = new_node
        else:
            current = self._find_node(index)
            new_node.next = current
            self._find_node(index-1).next = new_node

    def pop(self, index):
        node = self._find_node(index)
        if index == 0:
            self.__head.next = node.next
        else:
            node_previous = self._find_node(index-1)
            node_previous.next = node.next
            if index == self.length-1:
                self.__tail = node_previous
        node.next = None
        self.__len -= 1
        return node.value

    def index_of(self, element):
        return self._search(element)[0]

    def append(self, element):
        new_node = _Node(element)
        self._increase_len()
        if self.__len == 1:
            self.__head.next = new_node
        self.__tail.next = new_node
        self.__tail = new_node

    def __reversed__(self):
        return _ReversedIterator(self.__head.next, self.__tail)

    def inverse(self):

        inversed_llist = LinkedList(self.__reversed__(), max_size=self.__max)
        return inversed_llist

    def __contains__(self, elem):
        return self._search(elem)[1]

    def __iter__(self):
        return _IteratorLinkedList(self.__head.next)

    def __getitem__(self, index):
        if index >= self.length:
            raise IndexError("Index out of range")
        if index == self.length-1:
            return self.__tail.value
        for i, item in enumerate(self):
            if i == index:
                return item

    def __len__(self):
        return self.length

    def __str__(self):
        output = ''
        for i in self:
            output = output + str(i) + ' ' + '->' + ' '
        return output[:-4]

    def __repr__(self):
        return self.__str__
