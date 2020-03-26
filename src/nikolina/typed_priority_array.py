import math
class TypedPriorityArray:
    _reversed=False
    def __init__(self,*args,**kwargs):
        try:
            self._l=[]
            if(len(args)==0):
                raise TypeError
            if "reversed" in kwargs:
                if(kwargs["reversed"]==True):
                    self._reversed=True
            if(len(args)==1):
                if "__eq__" in args[0].__dict__.keys():
                    self._type=args[0]
                else:
                    raise TypeError
            else:
                self._type=type(args[0])
                for _arg in args:
                    if(type(_arg)!=self._type):
                        raise TypeError
                    self.insert(_arg)
            self.index=0
        except AttributeError:
            raise TypeError
    def get_length(self):
        return len(self._l)
    length = property(get_length)
    def get_type(self):
        return self._type
    array_type=property(get_type)
    def get_reversed(self):
        return self._reversed
    def set_reversed(self,x):
        if(self._reversed!=x):
            self._l=self._l[::-1]
            self._reversed=x
    reversed=property(get_reversed,set_reversed)
    def insert(self,x):
        if(self._type!=type(x)):
            raise TypeError
        if(len(self._l)==0):
            self._l.append(x)
        else:
            if(self._reversed==True):
                if(x>(self._l[0])):
                    self._l.insert(0,x)
                elif(x<self._l[len(self._l)-1]):
                    self._l.append(x)
                else:
                    l1=0
                    l2=len(self._l)-1
                    while(l2>=l1):
                        m=math.floor((l1+l2)/2)
                        if(self._l[m]<x):
                            l1=m+1
                            if(l2==1):
                                if(self._l[l1]<x):
                                    self._l.insert(l1,x)
                                    break
                                else:
                                    self._l.insert(l1+1,x)
                                    break
                        elif(self._l[m]>x):
                            l2=m-1
                            if(l2<=l1):
                                if(self._l[l1]<x):
                                    self._l.insert(l1,x)
                                    break
                                else:
                                    self._l.insert(l1+1,x)
                                    break
                        else:
                            self._l.insert(m,x)
                            break
            else:
                if(x<(self._l[0])):
                    self._l.insert(0,x)
                elif(x>self._l[len(self._l)-1]):
                    self._l.append(x)
                else:
                    l1=0
                    l2=len(self._l)-1
                    while(l1<=l2):
                        m=math.floor((l1+l2)/2)
                        if(self._l[m]<x):
                            l1=m+1
                            if(l1==l2):
                                if(self._l[l1]>x):
                                    self._l.insert(l1,x)
                                    break
                                else:
                                    self._l.insert(l1+1,x)
                                    break
                        elif(self._l[m]>x):
                            l2=m-1
                            if(l2<=l1):
                                if(self._l[l1]>x):
                                    self._l.insert(l1,x)
                                    break
                                else:
                                    self._l.insert(l1+1,x)
                                    break
                        else:
                            self._l.insert(m,x)
                            break             
    def pop(self,x):
        return self._l.pop(x)
    def contains(self,x):
        return x in self._l      
    def index_of(self,x):
        if(self._l.contains(x)):
            return self._l.index(x)
        else:
            return -1
    def __contains__(self,x):
        return self.contains(x)
    def __iter__(self):
        return iter(self._l)
    def next(self):
        if self.index >= len(self._l):
            raise StopIteration
        x=self._l[self.index]
        self.index+=1
        return x
    def __getitem__(self,x):
        return self._l[x]
    def __len__(self):
        return len(self._l)
    def __str__(self):    
        _str="["+str(self._l[0])
        x=1
        y=" <= "
        if(self._reversed==True):
            y=" >= "
        while(x<len(self._l)):
            _str+=y + str(self._l[x])
            x+=1
        return _str+"]"
    def __repr__(self):
        return self.__str__()

    
                    
