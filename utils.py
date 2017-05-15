import re
import os
import os.path;
from datetime import datetime;

def filter(all, pat):
    include = []
    exclude = []

    sections = pat.replace(' ', '').split(',')

    for s in sections:
        if re.match('\d+-\d+', s):
            start, end = s.split('-')
            include.extend(range(int(start), int(end)+1))
        elif s == '*':
            include = list(all)
        else:
            v = int(s)
            if v > 0:
                include.append(v)
            elif v < 0:
                exclude.append(abs(v))
            #end
        #end
    #end

    #print(include)
    #print(exclude)
    #print(list(set(include) - set(exclude)))

    return list(set(include) - set(exclude))
#end

def backup(filename):
    if not os.path.exists(filename):
        print('file not found')
        return
    #end

    filetime = os.path.getmtime(filename)
    fname, ext = os.path.splitext(filename)
    dt = datetime.fromtimestamp(filetime).strftime('-%Y%m%d-%H%M%S')
    os.rename(filename, fname + dt + ext)
#end

if __name__ == '__main__':
    print(filter(range(1,11), '*, 1-10, -4, -5, -9'))
    backup('../test.js')
#end
