#input a txt file and convert all the keys to upper keys


fname = input("Enter file name: ")
fh = open(fname)

for file in fh:
    file = file.strip()
    file = file.upper()
    print(file)