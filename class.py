class Foo:
    # static variable
    static = 123

    # constructor method
    def __init__(self):
        print('__init__')
    #end

    # normal method
    def hello(self):
        print('hello')
    #end

    @staticmethod
    def greeting(who):
        print('greeting to ' + who)
    #end

    @classmethod
    def MyClassMethod(clazz):
        pass
    #end
#end

'''
foo = Foo()
foo.hello()
print(Foo.static)
print(foo.static)

Foo.static = 222
print(Foo.static)
print(foo.static)

Foo.greeting('John')
print(Foo.__dict__)
'''
# http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python

class A(object):
    def foo(self,x):
        print("executing foo(%s, %s)"%(self,x))
    #end

    @classmethod
    def class_foo(cls,x):
        print("executing class_foo(%s, %s)"%(cls,x))
    #end

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)"%x)
    #end
#end

a=A()

a.foo(123)
print()

a.class_foo(123)
A.class_foo(123)
print()

a.static_foo(123)
A.static_foo('hi')
print()

print(a.foo)
print(a.class_foo)
print(a.static_foo)
print(A.static_foo)
print()
