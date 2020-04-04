from collections.abc import Iterable
class _Node:
    '''Node object in Linked List'''
    def __init__(self, data):
        self.item = data
        self.next = None
class LinkedList:
    '''Linked List implementation'''
    def __init__(self, *args, **kwargs):
        if len(args) == 0:
            raise ValueError("List cann't be empty!")
        self.__head = None
        self.__max_size = kwargs["max_size"] if "max_size" in kwargs else None
        self.__inversed = False
        if len(args) == 1:
            if not isinstance(args[0], Iterable):
                raise ValueError
            i = 0
            if self.__max_size != None and len(args[0]) > self.__max_size:
                raise MemoryError
            for item in args[0]:
                self.insert(i, item)
                i += 1
        else:
            if self.__max_size != None and len(args) > self.__max_size:
                raise MemoryError
            i = 0
            for _arg in args:
                self.insert(i, _arg)
                i += 1
    def insert(self, index, element):
        if index <= 0:
            __new_node = _Node(element)
            __new_node.next = self.__head
            self.__head = __new_node
            return
        current = self.__head
        i = 0
        while i < index:
            prev = current
            current = current.next
            i += 1
        
        __new_node = _Node(element)
        __new_node.next = current
        prev.next = __new_node
        
    def pop(self, index):
        if self.__head == None:
            return
        temp = self.__head
        if index == 0:
            prev = self.__head
            self.__head = temp.next
            temp = None
            return prev.item
        for _i in range(index - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        prev = temp.next
        next = temp.next.next
        temp.next = None
        temp.next = next
        return prev.item

    def append(self, element):
        self.insert(len(self), element)

    def index_of(self, element):
        __index = 0
        current = self.__head
        while current is not None:
            if current.item == element:
                return __index
            current = current.next
            __index += 1
        return -1
    def inverse(self):
        self.__inversed = True
        return self
    def __reversed__(self):
        self.__inversed = True
        return iter(self)
    def __iter__(self):
        if self.__inversed:
            self.indexIter = len(self) - 1
        else:
            self.indexIter = 0
        return self
    def __next__(self):
        if self.__inversed:
            if self.indexIter < 0:
                raise StopIteration
            item = self[self.indexIter]
            self.indexIter -= 1
            return item
        else:
            if self.indexIter >= len(self):
                raise StopIteration
            item = self[self.indexIter]
            self.indexIter += 1
            return item
    def __len__(self):
        if self.__head is None:
            return 0
        current = self.__head
        length = 0
        while current is not None:
            length += 1
            current = current.next
        return length
    def __contains__(self, element):
        current = self.__head
        while current is not None:
            if current.item == element:
                return True
            current = current.next
        return False
    def __getitem__(self, index):
        i = 0
        current = self.__head
        while current is not None:
            if i == index:
                return current.item
            current = current.next
            i += 1
    def __str__(self):
        ll = ""
        current = self.__head
        while current is not None:
            if current.next != None:
                ll += str(current.item) + ' -> '
            else:
                ll += str(current.item)
            current = current.next
        return ll
    @property
    def length(self):
        return len(self)
    @property
    def max_size(self):
        return self.__max_size
    #treba return iterator
    #da ide u rikverc