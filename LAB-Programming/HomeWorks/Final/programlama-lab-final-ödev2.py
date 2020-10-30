import random
#Öncelikle bu ödevi kimseden yardım almadan, kendi ders notlarımı kullanarak kendim yaptım.

#Bu fonksiyon 1. şıkkın cevabıdır. Bu fonksiyonda, verilen n değeri uzunluğunda bir vektör döndürülür.
#Bu vektörün aldığı değerler (-10) - 10 aralığında olup random bir sayıdır.
def vektor_olustur(n):
    vect = []
    [vect.append(random.randint(-10, 10)) for i in range(n)]
    return vect

#Bu fonksiyon 2. şıkkın cevabıdır. Bu fonksiyonda, parametre olarak gönderilen hem 2 farklı vektörün skaler çarpımı yeni bir vektör olarak döndürülür
#hem de bu skaler çarpımın değeri(döndürülen vektör dizisinin indeksleri toplamı) döndürülür
def skaler_carp(vect1, vect2):
    carpim = []

    for i in range(len(vect1)):
        xiyicarpim = vect1[i]*vect2[i]
        carpim.append(xiyicarpim)

    return carpim, sum(carpim)

#Bu fonksiyon 3. şıkkın cevabıdır. Bu fonksiyonda, kendisine parametre olarak gönderilen m değeri kadar 2'li vektör oluşturuyor(n boyutlu)
# ve bu vektörlerin skaler çarpımından dönen yeni vektörü(diziyi) matris elemanı olarak atar.
#bu fonksiyonda yeni bir vektör oluşturmak için a şıkkı fonksiyonunu kullanıyoruz ve matrisin index değerlerini atamak için
#b şıkkındaki fonksiyonu kullanıyoruz.

def matris_olustur(m, n):

    matris = []
    for i in range(m):
        vect1 = vektor_olustur(n)
        vect2 = vektor_olustur(n)

        matris.append(skaler_carp(vect1, vect2)[0])
    return matris

#Bu fonksiyon 4. şıkkın cevabıdır. Bu fonksiyon, kendisine c şıkkından oluşturulmuş 2 farklı matrisi parametre olarak alır.
#Öncelikle ilk matrisin sütunu ile ikinci matrisin satırının eşitliği kontrol edilir. Eğer eşitlik yoksa çarpım yapılamayacağı için bunun uyarısını
#verir. Daha sonra ilk matrisin n. satırı ile ikinci matrisin n. sütununu iki farklı dizi olarak alır ve bu dizilerdeki değerlerin skaler çarpımını
#(2. şık için oluşturduğumuz fonksiyondan dönen skaler değeri kullanarak) bulur ve matrisin n. indexine tüm çarpımları ekler.
#Fonksiyon içinde fonksiyon olarak kullandığım retcoloumn fonksiyonu ile ilk matrisin n. satırına denk gelen ikinci matris sütunu değerlerini
#alıp bir dizi halinde döndürüyoruz. En sonda ise bu oluşturulan matris(bu iki matrisin çarpımından elde edilen değerler*) döndürülür.
def matris_carpim(m1, m2):

    if len(m1[0]) != len(m2):
        return 0
    def retcoloumn(m2,col):
        coloumn = []
        for i in m2:
            for j in range(len(i)):
                if (j == col):
                    coloumn.append(i[j])
        return coloumn

    carpim = []
    for r in range(len(m1)):
        carpim.append([])
        for c in range(len(m2[0])):
            m1row = m1[r]
            m2coloumn = retcoloumn(m2, c)
            scalarproduct = skaler_carp(m1row, m2coloumn)[1]
            carpim[r].append(scalarproduct)
    return carpim

#Bu kısım 5.şıkkın cevabıdır. Önceki yazılan fonksiyonları test etmemiz için oluşturuldu.
#oluşturulan vektörün n değeri ve oluşturulan matrislerin m, n değerleri bizim tarafımızdan belirlendi.
def yazdirma():
    vect1 = vektor_olustur(4)
    vect2 = vektor_olustur(4)
    print("--------------------------------------------------------")
    print("*****************************A Şıkkı*****************************")
    print("\n\n")
    print("Olusturulan 1. vektör = ", vect1, "\nOluşturulan 2. vektör = ", vect2)

    print("\n\n")
    print("--------------------------------------------------------")
    print("*****************************B Şıkkı*****************************")
    print("\n\n")
    print("Oluşturulan bu iki vektörün çarpımından elde edilen vektör = ", skaler_carp(vect1, vect2)[0],
          "\nBu vektörden elde edilen toplam = ", skaler_carp(vect1, vect2)[1])
    print("\n\n")
    print("--------------------------------------------------------")
    print("*****************************C Şıkkı*****************************")
    #bu matrisin satır ve sütun değerleri bizim tarafımızdan belirleniyor.
    a = matris_olustur(4, 5)
    b = matris_olustur(5, 6)
    print("Oluşturulan 1. matris = ", a, "\nOluşturulan 2. matris = ", b)
    print("\n\n")
    print("--------------------------------------------------------")
    print("*****************************D Şıkkı*****************************")
    if matris_carpim(a, b) == 0:
        print("Bu iki matris çarpılamaz!")
    else:
        print("Az önce oluşturulan a ve b matrisinin çarpımı = ", matris_carpim(a, b))

yazdirma()
