#read a file, find the line which is like 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#get the hour (09 here) and find the frequency of hours

name = input("Enter file:")
if len(name) < 1: name = "names.txt"
handle = open(name)
dic = dict()

for line in handle:
    if not line.startswith('From '):
        continue

    line1 = line.split(' ')
    for words in line1:
        if ':' in words:
            value = words.split(':')[0]
            if value in dic:
                dic[value] += 1
            else:
                dic[value] = 1

lst = []
for k, v in dic.items():
    lst.append((k, v))

lst = sorted(lst)

for val, key in lst:
    print(val, key)