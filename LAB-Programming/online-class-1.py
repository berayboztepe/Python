import random

random.random()
print("1-100 arası random sayı = ", random.randint(1, 100))

#n tane random sayı oluşturup listeye atma(belirlenen aralıkta)
def get_n_random_numbers(n = 10, min_ = -5, max_ = 5):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(min_, max_))
    return numbers
print("random sayılar = ", get_n_random_numbers())
print("random sayılar = ", get_n_random_numbers(12, -1, 5))

print("\n\n\n")

#histogram(hangi sayıdan kaç tane var) oluşturmak için önce random gelen sayıları liste içi küçükten büyüğe sıralıyoruz
my_list=get_n_random_numbers()
print("sıralanmış hali = ", sorted(my_list))

#şimdi de histogramı oluşturduk

def my_frequency_with_dic(list):
    frequency_dict = {} # dict() = {} (ikisi de kullanılabilir)
    for item in list:
        if(item in frequency_dict):
            frequency_dict[item] = frequency_dict[item]+1
        else:
            frequency_dict[item] = 1
    return frequency_dict

print("histogram = ", my_frequency_with_dic(my_list))

print("\n\n\n")

#liste yapısıyla hash tablosu yaptık

def frequency_with_list_of_tuples(my_list1):
    frequency_list = []
    for a in range(len(my_list1)):
        s = False
        for j in range(len(frequency_list)):
            if(my_list1[a] == frequency_list[j][0]):
                frequency_list[j][1] = frequency_list[j][1]+1
                s = True
        if(s==False):
            frequency_list.append([my_list1[a], 1])
    return frequency_list

my_list1=[2,3,2,5,8,2,4,3,3,2,8,5,2,4,4,4,4,4]
result_1 = frequency_with_list_of_tuples(my_list1)
result_2 = my_frequency_with_dic(my_list1)
print("tuple histogramı = ", result_1)
print("liste histogramı = ", result_2)

print("\n\n\n")

#modun(en çok tekrar edilen sayıyı) bulma(en baştaki sayı moddur)
my_list2=get_n_random_numbers(5,-2,2)
my_hist_d=my_frequency_with_dic(my_list2)
my_hist2=frequency_with_list_of_tuples(my_list2)
print("liste histogramı = ", my_hist_d, "tuple histogramı = ", my_hist2)

#histogram dictte ise mod bulma en altta ilk yazılan sayımız mod, ikinci yazılan ise kaç kere tekrar edildiği
def frequency_mode():
    frequency_max = -1
    mode = -1
    for key in my_hist_d.keys():
        #print(key, my_hist_d[key])
        if my_hist_d[key] > frequency_max:
            frequency_max = my_hist_d[key]
            mode = key
    return mode, frequency_max

print("mod = ", frequency_mode())

print("\n\n\n")

#tuple list üzerinden mod bulma
my_list_2=get_n_random_numbers(5,-2,2)
my_hist_list=frequency_with_list_of_tuples(my_list_2)
print("tuple histogramı = ", my_hist_list)

def frequency_mode_with_tuple(my_hist_list):
    frequency_max1 = -1
    mode1 = -1
    for item, frequency in my_hist_list:
        #print(item, frequency)
        if frequency > frequency_max1:
            frequency_max1 = frequency
            mode1 = item
    return mode1, frequency_max1

print("mod = ", frequency_mode_with_tuple(my_hist_list))

print("\n\n\n")

#liste üzerinde lineer arama yapma eğer (-1, -1) verirse o sayı o listede yoktur

def my_linear_search(list1, item_search):
    found = (-1, -1)
    n = len(list1)
    for indis in range(n):
        if list1[indis] == item_search:
            found = (list1[indis], indis)
            # break uncomment edilirse aranan sayıyı ilk bulduğu anda döngüyü kırar. aksi takdirde en son bulduğundaki indisi yazar
    return found

list1=get_n_random_numbers(5, -10, 10)
print("liste = ", list1)
print("aradığınız sayı şurada ve sayınız şu = ", my_linear_search(list1, 3))
print("eğer cevap (-1,-1) ise aradığınız sayı listede yoktur")

print("\n\n\n")

#mean(ortalama) bulma s = listedeki eleman sayısı, t = elemanların toplamı

def find_mean(list):
    s, t = 0, 0
    for item in list:
        s = s+1
        t = t+item
    mean = t/s
    return mean

print("liste = ", list1)
print("ortalama = ", find_mean(list1))

print("\n\n\n")

#liste sıralama(bubble sort)

def bubble_sort(list1):
    n=len(list1)
    for iq in range (n-1, -1, -1): #listenin son elemanını tutuyoruz önce
        for jq in range(0, iq):
            if not (list1[jq] < list1[jq+1]):
                #swap yapılıyor
                temp = list1[jq]
                list1[jq] = list1[jq+1]
                list1[jq+1] = temp
    return list1
print("liste = ", list1)
print("sıralanmış hali = ", bubble_sort(list1))

print("\n\n\n")

#sıralanmış bir listeye ikili arama yapmak

def my_binary_search(list1, item_search):
    found = (-1, -1)
    low = 0
    high = len(list1)-1

    while low <= high:
        mid = (high+low) // 2

        if list1[mid] == item_search:
            return list1[mid], mid
        elif list1[mid] > item_search:
            high = mid-1
        else:
            low = mid+1

    return found

print("liste = ", list1)
print("sıralanmış hali = ", bubble_sort(list1))
print("aradığınız sayı şuna eşittir ve şuradadır = ", my_binary_search(list1, 5))
print("eğer cevap (-1,-1) ise aradığınız sayı listede yoktur")

print("\n\n\n")

#listeye kendimiz boyut atıyoruz ve program bize bir liste oluşturuyor

size = int(input("dizinin boyutunu girin:"))
list2 = get_n_random_numbers(size)
print("dizinin boyutunu kendiniz girdiğiniz liste = ", list2)

print("\n\n\n")


#dizinin medyanını(ortancasını) bulan program

list3 = get_n_random_numbers(7, -10, 10)
print(list3)

def find_median(list3):
    list3 = bubble_sort(list3)  # listeye bubble_sort yaptık
    print("sıralanmış liste = ", list3)
    n=len(list3)

    if n%2 == 1: #listenin eleman sayısı tek sayı ise
        middle = int(n/2)
        median = list3[middle]
        #print(median)

    else:
        middle_1 = list3[int(n/2)]
        middle_2 = list3[int(n/2) - 1]
        median = (middle_1 + middle_2) / 2
        #print(median)

    return median

print("medyan değeri = ", find_median(list3))



