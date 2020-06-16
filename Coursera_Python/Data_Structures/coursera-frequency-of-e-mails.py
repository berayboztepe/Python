#reading a file and find the greatest number of mail messages

name = input("Enter file:")
if len(name) < 1: name = "names.txt"
handle = open(name)
temp = dict()
list1 = []
b = 0
frequency_max = -1

for line in handle:
    if not line.startswith('From '):
        continue

    words = line.split()
    a = words[1]

    list1.append(a)
maxi = list1[b]

while b < len(list1):
    temp[list1[b]] = temp.get(list1[b], 0) + 1
    maxi = list1[b]
    b += 1

print(maxi, temp[maxi])