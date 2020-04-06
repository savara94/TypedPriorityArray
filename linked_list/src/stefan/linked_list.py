class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def check_for_max_size(method):
    def run_with_checked_size(*args):
        obj = args[0]
        if obj.max_size is not None:
            if len(obj) == obj.max_size - 1:
                raise MemoryError('Linked list does not allow more elements.')
        return method(*args)
    return run_with_checked_size

class LinkedList:
    @staticmethod
    def _is_iterable(obj):
        try:
            iter(obj)
        except TypeError:
            return False
        return True

    def __init__(self, *args, **kwargs):
        self.__max_size = kwargs['max_size'] if 'max_size' in kwargs else None
        self.__head = None
        self.__tail = None
        self.__length = 0

        initial_iterable = args
        if len(args) == 0:
            raise ValueError('You need to provide at least one argument.')
        if len(args) == 1:
            if not LinkedList._is_iterable(args[0]):
                raise ValueError('Argument needs to be iterable.')

            initial_iterable = args[0]
        for x in initial_iterable:
            self.append(x)

    @property
    def length(self):
        return len(self)

    @property
    def max_size(self):
        return self.__max_size
    
    @check_for_max_size
    def insert(self, index, element):
        if index >= len(self):
            # append is incrementing length itself
            self.append(element)
            return
        elif index <= 0:
            tmp = self.__head
            self.__head = Node(element)
            self.__head.next = tmp
        else:
            before = self._node_at_index(index - 1)
            after = before.next
            tmp = Node(element)
            before.next = tmp
            tmp.next = after

        self.__length += 1

    @check_for_max_size
    def append(self, element):
        new_node = Node(element)
        if self.__length == 0:
            self.__head = new_node
            self.__tail = new_node
        else:
            tmp = self.__tail
            self.__tail = new_node
            tmp.next = self.__tail

        self.__length += 1

    def pop(self, index):
        if index < 0 or index >= len(self):
            raise IndexError()

        tmp = self._node_at_index(index)
        after = tmp.next
        if index == 0:
            self.__head = tmp.next
        else:
            before = self._node_at_index(index - 1)
            before.next = after
            if index == len(self) - 1:
                self.__tail = before
        
        self.__length -= 1
        return tmp.value

    def index_of(self, element):
        for i, x in enumerate(self):
            if x == element:
                return i

        return -1

    def inverse(self):
        return LinkedList(reversed(self), max_size=self.max_size)

    def __len__(self):
        return self.__length

    def __str__(self):
        return ' -> '.join([str(x) for x in self])

    def __repr__(self):
        return str(self)

    def __getitem__(self, key):
        if key >= len(self) or key < 0:
            raise IndexError()

        for i, x in enumerate(self):
            if i == key:
                return x

    def __contains__(self, element):
        return self.index_of(element) != -1

    def __reversed__(self):
        tmp = [x for x in self]
        
        for x in reversed(tmp):
            yield x

    def _node_at_index(self, index):
        for i, x in enumerate(self._iterator(False)):
            if i == index:
                return x

    def _iterator(self, value=True):
        curr = self.__head
        while curr is not None:
            rv = curr.value if value else curr
            yield rv
            curr = curr.next

    def __iter__(self):
        return self._iterator()+