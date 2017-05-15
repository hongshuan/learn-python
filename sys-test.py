import sys
import foo

#print(sys.argv)
#print(sys.path)

print(foo.filter(range(1, 11), '*, 1-10, -4, -5, -9'))
