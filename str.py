import string
from random import *

s = '''this is a multilines
string, please note the new line'''

print(s)

s = r'this is a multilines\nstring, please note the \n'

print(s)

s = 'for more information'
s.replace('or', 'er')  #'fer mere infermation'

s[0].upper()
s[0].upper() + s[1:]  #'For more information'

s.title() #'For More Information'

'_'.join(s.split(' ')) #'for_more_information'
'_'.join(s.title().split(' ')) #'For_More_Information'


# generate password
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(8, 16)))
print(password)

