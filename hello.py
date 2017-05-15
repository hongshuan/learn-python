def hello():
    '''print hello, Python to console'''
    print('Hello, Python!')
#end

def test1():
    keys = ['a', 'b', 'c']
    vals = [111, 222, 333]

    d = dict(zip(keys, vals))
    print(d)

    d = {k: v for k, v in zip(keys, vals)}
    print(d)

    d = dict((k, v) for k, v in zip(keys, vals))
    print(d)

    d = dict((str(k), v) for k, v in zip(keys, vals))
    print(d)
#end

def test2():
    fo = open("foo.txt", "w") # "wb" not working
    fo.write("Name of the file: \n")
    fo.write("Closed or not : \n")
    fo.write("Opening mode : \n")
    fo.close()
#end

if __name__ == '__main__':
    print(hello.__doc__)
    hello()
    test1()
#end
