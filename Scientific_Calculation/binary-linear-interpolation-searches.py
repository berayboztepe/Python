
list =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


secim = int(input("Bulmak istediğiniz sayıyı yazın(1-10 arası): "))
secim1 = int(input("Bu sayıyı hangi arama yöntemi ile bulmak istiyorsunuz?\n"
                   "1- Linear\n"
                   "2- Binary\n"
                   "3- Interpolation\n"
                   ": "))



def linear(x):
    counter = 0
    for i in list:
        counter += 1
        if i == x:
            return counter
    return False

def binary(secim):
    ilk = 0
    son = len(list) - 1
    counter = 0


    while ilk <= son:
        orta = (ilk+son) // 2
        counter += 1
        if list[orta] > secim:
            son = orta - 1
        elif list[orta] < secim:
            ilk = orta + 1
        else: return counter

    return False

#orta = 8 + ((9-12) * (3)) //4
#8, 12
def interpolation(secim):
    ilk = 0
    son = len(list) - 1
    counter = 0

    while ilk <= son:
        counter += 1
        orta = ilk + ((secim - list[ilk]) * (son - ilk)) // (list[son] - list[ilk])
        if list[orta] > secim:
            son = orta - 1
        elif list[orta] < secim:
            ilk = orta + 1
        else: return counter

    return False

if secim1 == 1:
    print(linear(secim), ". denemede bulundu")

elif secim1 == 2:
    print(binary(secim), ". denemede bulundu")
else:
    print(interpolation(secim), ". denemede bulundu")
