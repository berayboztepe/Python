import time, random
#istenilen fib sayısını rec olarak döndüren fonksiyon(1588888995.1284537 ns)
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1

    return fib(n-1) + fib(n-2)


print(fib(20))
print(time.time())
print("\n\n\n")
print("-----------------")
print("\n\n\n")

#sonucu bulup memoya aktarıyoruz. bu sayede aynı değeri birden fazla çağırmaktan kaçınıyoruz ve işlemimiz daha kısa sürüyor(1588888972.5178578 ns)
#mesela fib(5)ten sonra fib(4)+fib(3) geliyor. fib(4)ten sonra da fib(3)+fib(2) geliyor. fib(3)ü iki kere hesaplamak yerine memoya kaydediyoruz.
def fib2(n, memo=None):
    if memo is None:
        memo = {}
    if n == 1 or n == 2:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fib2(n-1, memo) + fib2(n-2, memo)
        memo[n] = result
        return result
print(fib2(20, None))
#print(time.time())
print("\n\n\n")
print("-----------------")
print("\n\n\n")

#hırsız çantasına, çantanın genişliğine göre, eşya koyacak. en fazla 5 genişliğinde(biz belirliyoruz) item ile en fazla alabileceğimiz değer kaç olur
#toconsider = tüm itemlerı toplayan liste, avail ise genişlik
#<c, 8, 2>
#<b, 7, 3>
#Total value of items taken =  15 çıktı

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

def maxValue(Toconsider, avail):
    if Toconsider == [] or avail == 0:
        result = (0, ())
    elif Toconsider[0].getWeight() > avail:
        result = maxValue(Toconsider[1:], avail)
    else:
        nextItem = Toconsider[0]
        withVal, withToTake = maxValue(Toconsider[1:], (avail - nextItem.getWeight()))
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = maxValue(Toconsider[1:], avail)
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)

    return result

def smalTest():
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    #vals = [1, 4, 8, 10]
    weights = [3, 3, 2, 5]
   # weights = [1, 3, 4, 12]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    val, taken = maxValue(Items, 5)
    #val, taken = maxValue(Items, 7)
    for item in taken:
        print(item)
    print("Total value of items taken = ", val)

smalTest()
print("\n\n\n")
print("-----------------")
print("\n\n\n")
#farklı örneklerle fonksiyonumuzu çağırırsak
#Items taken
#<3, 7, 6>      4.item, genişlik = 6, değer = 7
#<2, 5, 4>      3.item, genişlik = 4, değer = 5         en fazla 10 genişlik ve en fazla 10 değere kadar rastgele sayılar ürettik
#<1, 4, 7>      2.item, genişlik = 7, değer = 4         toplam genişliği en fazla 40 atadık ve değerlerin toplam genişliği = 26
#<0, 3, 9>      1.item, genişlik = 9, değer = 3         bu sayede tüm değerleri alabildik
                                                  #Total value of items taken =  19

def buildmanyItems(numItems, maxVal, maxWeight):
    items = []
    for i in range(numItems):
        items.append(Item(str(i), random.randint(1, maxVal), random.randint(1, maxWeight)))
    return items

def bigTest(numItems):
    items = buildmanyItems(numItems, 10, 10)
    val, taken = maxValue(items, 40)
    print("Items taken")
    for item in taken:
        print(item)
    print("Total value of items taken = ", val)

bigTest(4)
#print(time.time()) #1588891882.6675391
print("\n\n\n")
print("-----------------")
print("\n\n\n")


#aynı şeyleri daha hızlı(memo ile)yapmak istersek
def maxValue2(Toconsider, avail, memo=None):
    if memo is None:
        memo = {}
    if (len(Toconsider), avail) in memo:
        result = memo[(len(Toconsider), avail)]
    elif Toconsider == [] or avail == 0:
        result = (0, ())
    elif Toconsider[0].getWeight() > avail:
        result = maxValue2(Toconsider[1:], avail, memo)
    else:
        nextItem = Toconsider[0]
        withVal, withToTake = maxValue2(Toconsider[1:], (avail - nextItem.getWeight()), memo)
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = maxValue2(Toconsider[1:], avail, memo)
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)

    memo[(len(Toconsider), avail)] = result
    return result

def bigTest2(numItems):
    items = buildmanyItems(numItems, 10, 10)
    val, taken = maxValue2(items, 40)
    print("Items taken")
    for item in taken:
        print(item)
    print("Total value of items taken = ", val)

bigTest2(4)
#print(time.time())#1588891956.369461