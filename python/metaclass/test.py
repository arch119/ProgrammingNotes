#!/usr/bin/env python3


def create_class():
    class_name = "Foo"
    class_parents = (object,)
    class_body = """
def __init__(self, name):
    self.name = name

def print_name(self):
    print(self.name)
    """
    # a new dict is used as local namespace
    class_dict = {}

    #the body of the class is executed using dict from above as local 
    # namespace 
    exec(class_body, globals(), class_dict)

    # final step of class creation
    Foo = type(class_name, class_parents, class_dict)
    return Foo


class DocMeta(type):
    def __init__(self, name, bases, attrs):
        for key, value in attrs.items():
            print(key)
            # skip special and private methods
            if key.startswith("__"): continue
            # skip any non-callable
            if not hasattr(value, "__call__"): continue
            # check for a doc string. a better way may be to store 
            # all methods without a docstring then throw an error showing
            # all of them rather than stopping on first encounter
            if not getattr(value, '__doc__'):
                raise TypeError("%s must have a docstring" % key)
        type.__init__(self, name, bases, attrs)

class MyClass(metaclass=DocMeta):
    def __init__(self, a):
        self.a = a
    
    def print_a(self):
        ''' prints the value of a'''
        print(a)

if __name__=='__main__':
    #Dynamically creating classes
    my_class = create_class()
    a = my_class('hello')
    a.print_name()


    #Custom Metaclass