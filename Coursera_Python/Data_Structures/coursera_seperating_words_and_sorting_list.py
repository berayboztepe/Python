#reading a file, find all the words(only one time) and append them a list
#and sort the list

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line1 = line.split()
    for line2 in line1:
        if not line2 in lst:
            lst.append(line2)

lst.sort()
print(lst)
