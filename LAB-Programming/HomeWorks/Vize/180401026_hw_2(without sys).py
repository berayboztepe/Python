f = open("input_hw_2.csv", "r")
freqs = []
month = {}

def hist():
    for i in f:
        freqs.append(int(i.split(";")[3].split("-")[1]))

    for item in freqs:
        if(item in month.keys()):
            month[item] = month[item] + 1
        else:
            month[item] = 1
    return month


print("histogram = ", hist())

def sortValues(month):
    sortedhist = sorted(month.items(), key = lambda t:t[1])
    return sortedhist

print("sorted histogram = ", sortValues(month))


def median():
    monthMedian = sortValues(month)
    n = len(monthMedian)
    if n % 2 == 1:
        middle = int(n / 2)
        return monthMedian[middle][1]


    else:
        middle_1 = monthMedian[int(n / 2)][1]
        middle_2 = monthMedian[int(n / 2) - 1][1]
        median = (middle_1 + middle_2) / 2
        return median



#print("medyan = ", median())

def average():
    monthAverage = list(month.values())
    sum = 0
    counter = 0
    for i in range(len(month)):
        sum = sum + monthAverage[i]
        counter += 1
    return sum / counter

#print("ortalama = ", average())

def output(average, median):
    fnew = open("180401026_hw_2_output.txt", "w")
    fnew.write("Medyan = ")
    fnew.write(str(median))
    fnew.write("\n")
    fnew.write("Ortalama = ")
    fnew.write(str(average))
    f.close()

output(average(), median())
