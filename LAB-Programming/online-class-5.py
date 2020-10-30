#bir hırsızın belirli bir ağırlık taşıma kapasitesine göre çalabileceği mallardan en fazla ne kadar para kaldırabileceğini bulmaya çalışıyoruz.
from pprint import pprint as pp
from itertools import chain, combinations
#javadaki gibi class ve constructor yapısı ile isim, para değeri ve ağırlık değerlerini atıyoruz.
class  Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + (self.name) + ', ' + str(self.value)  + ', ' + str(self.weight) + '>'
        return result

def value(item):
    return item.getValue()

def weightInverse(item):
    return 1.0/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()
#istenilen size'a göre olabilecek tüm senaryoları bulan fonksiyon
def greedy(items, maxWeight, keyFunction):
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    result = []
    totalValue, totalWeight = 0.0, 0.0

    for i in range(len(itemsCopy)):
        if(totalWeight + itemsCopy[i].getWeight()) <= maxWeight:
            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getWeight()
            totalValue += itemsCopy[i].getValue()
    return(result, totalValue)
#değerleri atıyoruz
def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    #values = [175, 90, 20, 50, 10, 200]
    values = [23, 4, 112, 66, 186, 56]
    #weights = [10, 9, 4, 2, 1, 20]
    weights = [10, 1, 15, 13, 17, 12]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items
#değerleri yazdırıyoruz
def testGreedy(items, maxWeight, keyFunction):
    taken, val = greedy(items, maxWeight, keyFunction)
    print("Total value of this taken is = ", val)#toplam para değerini yazdırıyoruz
    for item in taken:
        print('  ', item)

#değerleri yazdırmak için testgreedy'e gönderiyoruz
def testGreedys(maxWeight = 10):#maxWeight = 20
    items = buildItems()
    print("Use greedy by value to fill knapsack of size = ", maxWeight)#para değerine en yüksek tutarak
    testGreedy(items, maxWeight, value)
    print("\nUse greedy by weight to fill knapsack of size = ", maxWeight)#ağırlığı en az tutarak
    testGreedy(items, maxWeight, weightInverse)
    print("\nUse greedy by density to fill knapsack of size = ", maxWeight)#para/ağırlık yani density'e göre
    testGreedy(items, maxWeight, density)

print(testGreedys())

#knapsack optimal with brute force
#en iyi ihtimali aralarında seçiyor
def chooseBest(pset, maxWeight, getVal, getWeight):
    bestVal = 0.0
    bestSet = None
    for items in pset:
        itemsVal = 0.0
        itemsWeight = 0.0
        for item in items:
            itemsVal += getVal(item)
            itemsWeight += getWeight(item)
        if itemsWeight <= maxWeight and itemsVal > bestVal:
            bestVal = itemsVal
            bestSet = items
    return (bestSet, bestVal)

#en iyi ihtimali yazdırıyor(en fazla para kazanılacak ihtimal)
def testBest(maxWeight = 10):#maxWeight = 20
    items = buildItems()
    pset = genPowerset(items)
    taken, val = chooseBest(pset, maxWeight, Item.getValue, Item.getWeight)
    print("Total value of items taken is = ", val)
    for item in taken:
        print(item)
#sayıların tüm kombinasyonlarını buluyor
def genPowerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3), (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

print(testBest())

pset = set(genPowerset({1, 2, 3}))
#for set_1 in pset:#hepsini ayrı ayrı yazdırıyor
   # print(set_1)
pp(set(genPowerset({1, 2, 3})))#tek seferde hepsini yazdırıyor