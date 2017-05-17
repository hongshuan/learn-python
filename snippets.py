
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

