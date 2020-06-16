#input a txt file and find all the lines which starts with X-DSPAM-Confidence:
#get the numbers as float numbers
#find their avg

counter = 0
temp = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    counter = counter + 1
    line1 = line.find(":")
    value = line[line1 + 1:]
    value = value.strip()

    temp = temp + float(value)

print("Average spam confidence:", temp / counter)
