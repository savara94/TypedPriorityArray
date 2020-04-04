"""
Module containing LinkedList
"""
class Node:
        def __init__(self, value):
            self.value=value
            self.next_value = None

class LinkedList(object):
    """
    Linked list data structure.
    """
    def __init__(self, *args, **kwargs):
        #if len(args)==0
        if not args:
            raise ValueError('You must specify at least one argument.')

        self.__arg=args[0]
        self.__container = []
        self.head = self.__arg[0]
        self.head = None


        self.__reversed = False
        self.__rev = -1
        
        self.__max_size = kwargs['max_size'] if 'max_size' in kwargs else None

        if len(args) == 1:
            self.__arg[0] = self.head
            if not LinkedList.__is_iterable(self):
                raise TypeError('Use only iterable type.')
            else:
                self.__container=list(args)

        else:
            if self.__max_size is not None:
                if not isinstance(self.__max_size, int):
                    raise TypeError('Use only int type.')
                else:
                    if kwargs > self.__max_size:
                        raise MemoryError('Overflow.')
                    else:
                        self.__container=list(*args, **kwargs)
            else:
                self.__container=list(*args)        
              
            
    @property
    def length(self):
        return len(self)

    @property
    def max_size(self):
        return self.__max_size

    def iter(self):
        current_node=self.__arg[0]
        while current_node is not None:
                yield current_node.value
                current_node=current_node.next_value
        raise StopIteration

           
    """
        for i, item in enumerate(self.__arg):
            if i>=len(self.__arg):
                raise StopIteration 
    """   

    @staticmethod
    def __is_iterable(self):
        if hasattr(self, '__iter__'):
            return True
        else:
            return False
        """
        try:
            iterable=iter(self.__arg)
        except:
            return False
        """

    def __iter__(self):
        return iter(self.__arg)

   

    def insert (self, index, element):
        if index == 1:
            new_node = Node(element)
            new_node.next_value = self.head
            self.head = new_node
        i = 1
        n = self.head
        while i < index-1 and n is not None:
            n = n.next_value
            i = i+1
        if n is None:
            raise IndexError("Index out of bound")
        else: 
            new_node = Node
            new_node.next_value = n.next_value
            n.next_value = new_node

 
    
    def __str__(self):
        sign = '->' 
        return str(self.__container).replace(',', f' {sign}')

    def __repr__(self):
        return str(self)
