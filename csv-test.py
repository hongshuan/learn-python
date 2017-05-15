import csv

def csv_read():
    csvfile = open('eggs.csv', 'r')
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print([x.strip() for x in row])
    #end
    csvfile.close()
#end
 
def csv_write():
    csvfile = open('eggs.csv', 'a')
    writer = csv.writer(csvfile)
    writer.writerow(['Spam', 'xxyyzz', 'spam@mail.com', 1])
    csvfile.close()
#end

def csv_dict_read():
    csvfile = open('eggs.csv', 'r')
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['username'].upper(), row['email'].strip())
    #end
    csvfile.close()
#end

def csv_dict_write():
    csvfile = open('names.csv', 'w')
    fieldnames = ['username', 'password', 'email', 'active']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'username': 'Baked', 'password': '223344', 'email': 'baked@mail.com', 'active': 0})
#end

if __name__ == '__main__':
    #csv_read()
    csv_write()
    #csv_dict_read()
    #csv_dict_write()
#end
