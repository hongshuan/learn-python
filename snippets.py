
{ x**2 for x in range(10) }

a_set = set(range(20))

{ x**2 for x in a_set }

{ x for x in a_set if x % 2 == 0 }

# swap key and value
a_dict = { 'a': 1, 'b': 2, 'c': 3 }

{ value:key for key, value in a_dict.items() }

[ f for f in glob.glob('*.xml') ]
[ f for f in glob.glob('*.xml') if os.stat(f).st_size > 6000 ]

[ os.path.realpath(f) for f in glob.glob('*.xml') ]

# urllib.parse.parse_qs()
query = 'username=pilgrim&password=PapayaWhip&email=pilgrim@mail.com'
a_list = query.split('&')
a_list_of_lists = [ v.split('='), 1) for v in a_list ]
a_dict = dict(a_list_of_lists)

def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b
    #end
#end

for n in fib(1000):
    print(n, end=' ')

list(fib(1000))


