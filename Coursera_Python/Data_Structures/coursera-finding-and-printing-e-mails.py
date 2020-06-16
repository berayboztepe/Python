#reading a file, finding all of the e-mails
#and printing them and counts


fname = input("Enter file name: ")
if len(fname) < 1: fname = "names.txt"

fh = open(fname)
count = 0

for line in fh:
    if not line.startswith('From '):
        continue

    line1 = line.split()
    count += 1
    print(line1[1])

print("There were", count, "lines in the file with From as the first word")
