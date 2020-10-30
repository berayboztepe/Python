import random
from itertools import chain, combinations
#ödevi yaparken kullandığım ders notları = https://github.com/berayboztepe/LAB-Programming-Py-/blob/master/online-class-5.py
#https://github.com/berayboztepe/LAB-Programming-Py-/blob/master/online-class-6.py
#https://github.com/berayboztepe/LAB-Programming-Py-/blob/master/online_class_1.py
#Bu ödevi yaparken internetten, arkadaşlarımdan vb. yerlerden yardım almadım. Sadece yukarıda belirttiğim ders notlarından yararlandım

#yetişmeyen programlama labaratuvarı ödevi. üzerine teslim gününden sonra yeniden uğraşıldı.

#öncelikle listeye atadığım değerler için bir class oluşturdum ve bu değerleri classlarla tuttum
class  Item(object):
    def __init__(self, n, minv, maxv):
        self.name = n
        self.minv = minv
        self.maxv = maxv
    def getName(self):
        return self.name
    def getMinv(self):
        return self.minv
    def getMaxv(self):
        return self.maxv
    def __str__(self):
        result = '<' + (self.name) + ', ' + str(self.minv) + ', ' + str(self.maxv) + '>'
        return result
#a şıkkı için oluşturulan değerler class yardımıyla alınır ve listeye atılır.(items) ve liste bu fonksiyondan döndürülür
#a şıkkı
list1 = [] #oluşturulan max ve min değerlerini kişiye göre o indekste tutan liste
names = ['ahmet', 'mehmet', 'ayşe', 'ali', 'fatma']
def listeyi_olusturma(counter, maxv):
    items = []
    for i in range(counter):
        max = random.randint(1, maxv)
        min = random.randint(1, maxv)
        while min > max and min != max:
            min = random.randint(1, maxv)
        list1.append((min, max))
        items.append(Item(names[i], min, max))
    return items
list2 = []#okunan tüm sayfaları kapsayan liste
#değerlerin yazdırılması
# bu kısımda ise değerleri ekrana yazdırırken okunan sayfaların kaç kere okunduğunu bulmak için list2'ye bu okunan sayfaları atıyoruz
def ekrana_yazdirma():
    items = listeyi_olusturma(5, 250)
    for i in range(5):
        print(i+1, ". kişi = ", items[i])
    for i in range(len(list1)):
        for j in range(list1[i][0], list1[i][1]+1):
            list2.append(j)


print("-------------")
print("\n\n\n")
print("---------------A ŞIKKI---------------\n")
ekrana_yazdirma()#kişiler ve okudukları sayfa aralıklarını ekrana yazdırıyorum
print("\n\n\n")
print("-------------")
print("\n\n\n")
"""print(list1)         #okudukları sayfa aralıklarını temsil eden liste
print("\n\n\n")
print("-------------")
print("\n\n\n")"""
#b şıkkı
# bu kısımda okunan sayfaların kaç kere okunduğunu bir sözlüğe atıyoruz ve döndürüyoruz.
def tekrar_edenler_dict(list):
    frequency = {}
    for item in list:
        if (item in frequency):
            frequency[item] = frequency[item] + 1
        else:
            frequency[item] = 1

    return frequency
#bu kısımda en çok tekrar eden sayfaları buluyoruz ve listeye ekliyoruz. ayrıca kaçar kere okunduklarını da döndürüyoruz.
list = [] #en çok okunan sayfaları içinde bulunduran liste
def en_cok_okunan_sayfalar():
    max = tekrar_edenler_dict(list2).get(list2[0])
    for key in tekrar_edenler_dict(list2).values():
        if key > max:
            max = key
    for key in tekrar_edenler_dict(list2).keys():
        if tekrar_edenler_dict(list2)[key] == max:
            list.append(key)

    return max
print("---------------B ŞIKKI---------------\n")
print("okunan sayfaların kaç kere tekrar edildiği = ", tekrar_edenler_dict(list2))#okunan sayfaların toplam kaç kişi tarafından okunduğunu göteren dict yapısı
print("en çok okunan sayfanın kaç kere okunduğu = ", en_cok_okunan_sayfalar(), "\t" ,"bu sayfalar = ", list)#en çok okunan sayfaların yazılması ve bu sayfaların kaç kişi tarafından okunduğunu gösteren fonksiyon
print("\n\n\n")
print("-------------")
print("\n\n\n")

#c şıkkı
#bu kısımda ortak okunan sayfaları olmayan kişilerin indekslerini bulup listeye atıyoruz ve bu listeyi döndürüp en fazla okunmayan
#sayfa sayısını buluyoruz.
ortak_yok = []
toplam_list = []
def ortak_okunmayan_sayfalar(list1):
    for i in range(len(list1)):
        for j in range(i+1, len(list1)):
            if list1[i][0] > list1[j][0] and (list1[j][0] < list1[i][1]) and (list1[i][0] < list1[j][1]):
                max = list1[i][0]
                if list1[j][1] >= max and list1[i][1] < max:
                    min = list1[j][1]
                elif list1[j][1] >=max and list1[j][1] < list1[i][1]:
                    min = list1[j][1]
                else:
                    min = list1[i][1]
            elif list1[i][0] < list1[j][0] and ((list1[j][0] < list1[i][1]) and (list1[i][0] < list1[j][1])):
                max = list1[j][0]
                if list1[j][1] >= max and list1[i][1] < max:
                    min = list1[j][1]
                elif list1[j][1] >=max and list1[j][1] < list1[i][1]:
                    min = list1[j][1]
                else:
                    min = list1[i][1]
            elif list1[i][0] == list1[j][0]:
                max = list1[i][0]
                if list1[j][1] >= max and list1[i][1] < max:
                    min = list1[j][1]
                elif list1[j][1] >=max and list1[j][1] < list1[i][1]:
                    min = list1[j][1]
                else:
                    min = list1[i][1]
            elif list1[i][1] == list1[j][1]:
                min = list1[i][1]
                if list1[j][0] <= min and list1[i][0] < min:
                    max = list1[j][0]
                elif list1[j][0] >=min and list1[j][0] > list1[i][0]:
                    max = list1[j][0]
                else:
                    max = list1[i][0]
            else:
                print(i+1, ".", "kişi", names[i], "ve", j+1, ".", "kişi", names[j],"'in ortak noktaları yok")
                ortak_yok.append((i+1, j+1))
                toplam_list.append((list1[i][1] - list1[i][0]) + (list1[j][1] - list1[j][0]))

def uclu_kombinasyon_ekle(ortak_yok):
    for i in range(len(ortak_yok)):
        for j in range(i+1, len(ortak_yok)):
            if ortak_yok[i][1] == ortak_yok[j][0]:
                a = ortak_yok[j][1]
                ortak_yok.append((ortak_yok[i][0], ortak_yok[i][1], ortak_yok[j][1]))
                toplam_list.append(toplam_list[i] + ((list1[a-1][1] - list1[a-1][0]) + 1))

    return ortak_yok
def dortlu_kombinasyon_ekle(ortak_yok):
    ortak_yok = uclu_kombinasyon_ekle(ortak_yok)
    for i in range(len(ortak_yok)):
        if len(ortak_yok[i]) > 2:
            for j in range(i, ortak_yok[0][0], -1):
                if ortak_yok[i][2] == ortak_yok[j][0]:
                    a = ortak_yok[j][1]
                    ortak_yok.append((ortak_yok[i][0], ortak_yok[i][1], ortak_yok[i][2], ortak_yok[j][1]))
                    toplam_list.append(toplam_list[i] + ((list1[a-1][1] - list1[a-1][0]) + 1))

    return ortak_yok
def besli_kombinasyon_ekle(ortak_yok):
    ortak_yok = dortlu_kombinasyon_ekle(ortak_yok)
    for i in range(len(ortak_yok)):
        if len(ortak_yok[i]) > 3:
            for j in range(i, ortak_yok[0][0], -1):
                if ortak_yok[i][3] == ortak_yok[j][0]:
                    a = ortak_yok[j][1]
                    ortak_yok.append((ortak_yok[i][0], ortak_yok[i][1], ortak_yok[i][2], ortak_yok[i][3], ortak_yok[j][1]))
                    toplam_list.append(toplam_list[i] + ((list1[a - 1][1] - list1[a - 1][0]) + 1))

    return ortak_yok


print("---------------C ŞIKKI---------------\n")
ortak_okunmayan_sayfalar(list1)
print("hiç ortak elemanları olmayan kişiler = ", besli_kombinasyon_ekle(ortak_yok))
print("en çok okunmayan sayfa = ", (max(toplam_list)+2))
print("\n\n\n")
print("-------------")
print("\n\n\n")
#d şıkkı
# bu fonksiyon ile attığım list1'in olası tüm kombinasyonlarını döndürmek için itertools'u kullandım.
def genPowerset(iterable):
    s = iterable
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
list5 = []#en fazla okunmamış sayfa sayısını buluyoruz, bunları okumayan kişileri buraya yazdırıyoruz
#bu fonksiyonda döndürdüğümüz kombinasyonları pset'e atıyoruz ve ve bu değerlerin içerdiği sayfa numaralarını list6ya atıyoruz.
#eğer aynı indeksin farklı değerlerinde aynı sayfa numarası varsa list6 clearlanır ve döngü kırılır. Eğer yoksa list6 boş liste değilse
#list6 nın eleman sayısı max olur, list5 ise bu list6 nın değerlerini alır. Devam eden döngülerde eğer list6 eleman sayısı max'tan fazlaysa
#max değeri ve list5 değişir. En son ise en fazla değer döndürülür.
def brute_force():
    pset = set(genPowerset(list1))
    max =  0
    for p_set in pset:
        list6= []
        #print(p_set)
        for j in range(len(p_set)):
            if len(p_set)  == 1:#eğer kombinasyon tek kişinin okuduğu sayfaları içeriyorsa döngüye girmez. Karşılaştırma en az iki kişi arasında yapılır.
                break
            for i in range(p_set[j][0], p_set[j][1]+1):
                if i in list6:
                    list6.clear()
                    break
                else:
                    list6.append(i)
            if len(list6) == 0:
                break
        if not len(list6) == 0:
            if len(list6) > max:
                max = len(list6)
                list5.clear()
                list5.append(p_set)
            #print(list6)
    return max
#bu kısımda ise bu max sayfaları okuyan kişiler isimleri ile birlikte döndürülür. Eğer hiç ortak nokta yoksa uyarı mesajı yazılır
def d_sikki_yazdirma():
    print("---------------D ŞIKKI---------------\n")
    if brute_force() == 0:
        print("Hiç ortak okunmayan sayfa yoktur!")
    else:
        print(" en fazla ortak okunmamış sayfa sayısı(birleşim) = ", brute_force(),"\n", "bu sayfaları okumayan kişiler: ")
        for i in range(len(list5[0])):
            if list5[0][i] in list1:
                for j in range(len(list1)):
                    if list1[j] == list5[0][i]:
                        break
            print("\t\tokuduğu sayfalar = ", list5[0][i],"\tisim = ", names[j])
        print(" bu kişilerin sayısı(k) = ", len(list5[0]))

d_sikki_yazdirma()
print("\n\n\n")
print("-------------")
print("\n\n\n")
