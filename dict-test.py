
def test_dict():
    d = {
        'username': 'hsli',
        'password': 'andi.88'
    }

    if 'username' in d:
        print(d['username'])
    #end

    if 'password' in d:
        print(d['password'])
    #end

    try:
        print(d['email'])
    except(KeyError):
        print('error')
    #end
#end

if __name__ == '__main__':
    #test_dict()
#end
