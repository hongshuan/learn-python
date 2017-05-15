import json
from io import StringIO

person = { "name":"John", "age":31, "city":"New York" };
print(person)
print(json.dumps(person, indent=4))

foo = ['foo', {'bar': ('baz', None, 1.0, 2)}]
print(foo)
print(json.dumps(foo, indent=4))

io = StringIO()
json.dump({"c": 0, "b": 0, "a": 0}, io)
print(io.getvalue())

io = StringIO('{ "name":"John", "age":31, "city":"New York" }')
print(json.load(io))

