import re

fh = open('names.txt', 'r')
sum1 = 0
for file in fh:
    valuelist = re.findall('[0-9]+', file)

    if len(valuelist) == 0: continue
    print(valuelist)
    for i in valuelist:
        sum1 += int(i)
print(sum1)
