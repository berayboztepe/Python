#parametre olarak alınan index ile  çocuklarını karşılaştırıp aralarından en küçüğünü bulan ve bunları sıralayan recursive işlem(minimum heapify)
#parametre olarak bir dizi alır
def min_heapify(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1
    smallest = i

    if left <= length and array[i] > array[left]:
        smallest = left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array, smallest)

#sırayla, parametre olarak gönderilen dizideki tüm elemanlara heapify uygular ve o diziyi heap haline getirir.(en sondan)
def build_min_heap(array):
    for i in reversed(range(len(array)//2)): #tersten başlamak için reversed
        min_heapify(array, i)

my_array = [8,10,3,4,7,15,1,2,16]
#new_array = [2, 323, 4234, 11, 23, 55, 3431, 42, 0, 2992]

build_min_heap(my_array)
print("min heap yapılmış dizi = ", my_array)
print("\n")
print("-----------------")
print("\n")

#https://www.cs.usfca.edu/~galles/visualization/Heap.html heap oluşmasını simule etmek için örnek site



#heapsort algoritması, heapify ve build_heap ile dizi sıralamak için kullanılır
#gönderilen dizideki kök ile son elemanın yeri değişir, son eleman yeni listeye eklenir, eski listeden silinir ve heapify yapılır.
#bu sayede liste küçükten büyüğe sıralanıp fonksiyondan döndürülür
def heapsort(array):
    array = array.copy()
    build_min_heap(array)
    sorted_array = []
    for i in range (len(array)):
        array[0], array[-1] = array[-1], array[0]
        sorted_array.append(array.pop())
        min_heapify(array, 0)
    return sorted_array

#print("heapsort yapılmış dizi = ", heapsort(my_array))
#print("\n")
#print("-----------------")
#print("\n")



#parametre olarak gönderilen diziye, yine parametre olarak gönderilen değeri ekleyen fonksiyon
#eğer gönderilen değer listede varsa yeniden eklenmeyerek uyarı mesajı gözükecek ve liste aynı şekilde geri döndürülecek
#eğer ekleme yapıldıysa dizi yeniden heap haline getirilip geri döndürülecek
def insertitemToHeap(my_heap, item):
    for i in range(len(my_heap)):
        if my_heap[i] == item:
            print("Bu sayı zaten heapde mevcut, listeye yeni eleman eklenemedi")
            return my_heap
    my_heap.append(item)
    build_min_heap(my_heap)
    return my_heap
    #return heapsort(my_heap) eğer liste sıralanmış döndürülmek isteniyorsa


print("Gönderilen sayının heape eklenmiş hali = ", insertitemToHeap(my_array, 7))#sayı dizide olduğu için liste değişmeyecek
print("\n")
print("Gönderilen sayının heape eklenmiş hali = ", insertitemToHeap(my_array, 5))
print("\n")
print("-----------------")
print("\n")



#parametre olarak aldığı diziye heapsort yaparak sıralar. köküyle en son elemanının yerini değiştirir ve en küçük elemanı silerek heap dizisini yeniden oluşturur.
#ve önce heap haline getirir, sonra yeniden sıralanmış halde geri döndürür.
def removeitemFrom(my_heap):
    new_arr = heapsort(my_heap)
    #print(new_arr)
    new_arr[0], new_arr[-1] = new_arr[-1], new_arr[0]
    new_arr.pop()
    build_min_heap(new_arr)
    return new_arr
    #return heapsort(new_arr)eğer liste sıralanmış döndürülmek isteniyorsa


print("ilk elemanı silinmiş dizi = ", removeitemFrom(my_array))
