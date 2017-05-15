import re

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

if __name__ == '__main__':
    print(filter(range(1,11), '*, 1-10, -4, -5, -9'))
#end
