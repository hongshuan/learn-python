class Fib:
    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1
    #end

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self
    #end

    def __next__(self):
        fib = self.a

        if fib > self.max:
            raise StopIteration
        #end

        self.a, self.b = self.b, self.a + self.b

        return fib
    #end
#end

fib = Fib(100)
for i in range(10):
    print(next(fib), end=' ')
