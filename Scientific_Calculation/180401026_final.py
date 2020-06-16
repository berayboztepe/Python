#Emre Beray BOZTEPE 180401026

from sympy import Symbol

file = open("veriler.txt", "r")
datas = []

x = Symbol('x')

for i in file:#okunan dosyadaki değerleri bir diziye atandı
    datas.append(int(i))
#print(datas)

n = len(datas)#dizinin eleman sayısı
yitoplam = sum(datas)#dizideki elemanların toplamı

#burada x^12'ye kadar olan x üs toplamları bulunup bir listeye atandı ve o liste döndürüldü.
def kullanilacakxdegerleri(list, n):
    xdegerleri = []
    for i in range(13):
        x = 0
        for k in range(n):
            x += (k+1)**i
        xdegerleri.append(x)
    return xdegerleri

#burada ise x^6*y'ye kadar olan x üs*y toplamları bulunup bir listeye atandı ve o liste döndürüldü.
def xiyitoplamlari(list, n):
    xiyidegerleri = []
    for i in range(7):
        xiyi = 0
        for k in range(n):
            xiyi += ((k+1)**i)*(list[k])
        xiyidegerleri.append(xiyi)
    return xiyidegerleri

#bu kısımda gönderilen matris çözümleniyor.
def gausselemeyontemi(degerler, n):
    n = len(degerler)

    for i in range(0, n):
        # sütundaki en yüksek değer arandı, bu değer maxdegere atandı ve bu değerin satırı enbuyuksatıra atandı.
        # abs methodu ile verilen parametrenin değeri olduğu gibi işleme alındı.
        maxdeger = abs(degerler[i][i])
        enbuyuksatir = i
        for k in range(i + 1, n):
            if abs(degerler[k][i]) > maxdeger:
                maxdeger = abs(degerler[k][i])
                enbuyuksatir = k

        # maxdegerdeki değer ile temple tutulan satırdaki değerin yeri değiştirildi.
        for k in range(i, n + 1):
            temp = degerler[enbuyuksatir][k]
            degerler[enbuyuksatir][k] = degerler[i][k]
            degerler[i][k] = temp

        # şuanda tutulan(k ile) sütunun altındaki tüm değerler 0 yapıldı.
        for k in range(i + 1, n):
            c = -degerler[k][i] / degerler[i][i]
            for j in range(i, n + 1):
                if i == j:
                    degerler[k][j] = 0
                else:
                    degerler[k][j] += c * degerler[i][j]

    # üst üçgensel matris halindeki matrise göre denklem çözüldü ve bu matris döndürüldü.
    sonmatris = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        sonmatris[i] = degerler[i][n] / degerler[i][i]
        for k in range(i - 1, -1, -1):
            degerler[k][n] -= degerler[k][i] * sonmatris[i]
    return sonmatris

#bu kısımda değerleri 1-6 derece arası polinomlara yaklaştırıldı ve katsayılar bulunup bir listeye aktarıldı, liste döndürüldü.
def cozumlerilistele(list, n):
    cozum = []
    for i in range(2, 8):#1. derece polinomda 2 bilinmeyen olduğu için döngü 2den başlatıldı.
        degerlerlistesi = []
        for j in range(i):
            degerlerlistesi.append([])
            for k in range(i):#liste i kadar döndürülürken öncelikle x değerleri ve en son xiyi değeri bir listeye o indekse ekleniyor.
                degerlerlistesi[j].append(kullanilacakxdegerleri(list, n)[k + j])
            degerlerlistesi[j].append(xiyitoplamlari(list, n)[j])
            if j == i - 1:#son eleman da eklendikten sonra matris çözümlenip liste sıfırlanıyor. matris çözümüyle bulunan katsayılar cozum dizisine ekleniyor.
                cozum.append(gausselemeyontemi(degerlerlistesi, n))
                degerlerlistesi.clear()
    return cozum

#bu kısımda st değerini formüle göre bulunuyor.
def stdeger(x, datas, n, yitoplam):
    yort = yitoplam / n
    st = 0
    for i in range(n):
        st += (datas[i] - yort) ** 2
    return st
#bu fonksiyonda sr değeri formüle göre bulunuyor ve daha önce bulunan st değeri ile bulunan korelasyon katsayısı döndürülüyor.
def korelasyonvesrdegeri(x, datas, n, yitoplam):
    sr = 0
    for i in range(n):
        hesaplama = 0
        hesaplama += x[0]
        for j in range(1, len(x)):
            hesaplama += x[j] * (i + 1) ** j
        sr += (datas[i] - hesaplama) ** 2

    return ((stdeger(x, datas, n, yitoplam) - sr) / stdeger(x, datas, n, yitoplam)) ** (1/2)
#döndürülen korelasyon sayıları bir liste haline getiriliyor.
def korelasyonlist(korelasyondegerleri, datas, n, yitoplam):
    rdegerleri = []
    for i in korelasyondegerleri:
        rdegerleri.append(korelasyonvesrdegeri(i, datas, n, yitoplam))
    return rdegerleri

#liste haline getirilen kolerasyon sayılarından 1'e en yakın olan sayı bulunuyor ve o sayının kaçıncı parabole göre bulunduğu ve
# korelasyon değeri döndürülüyor.
def bireenyakindeger(korelasyondegerleri, datas, n, yitoplam):
    a = korelasyonlist(korelasyondegerleri, datas, n, yitoplam)
    ilk = 150
    list = []
    for i in range(len(a)):
        deger = abs(1-a[i])
        if int(deger) < 0:
            deger *= -1
        if deger < ilk:
            ilk = deger
            list.clear()
            list.append((i+1, a[i]))
    return list

#bu fonkisyonda en uygun polinom çağrılır ve fonksiyon haline getirilir. Gelecek olan x değerine göre fonksiyonun çözümü döndürülür.
def fx(x):
    fonksiyon = 0
    a = bireenyakindeger(cozumlerilistele(datas, n), datas, n, yitoplam)[0][0]
    for i in cozumlerilistele(datas, n):
        if len(i) == a + 1:
            t = 0
            for j in range(0, a+1):
                fonksiyon += i[t]*(x**j)
                t += 1
    return fonksiyon

#bu kısımda a = okul numaramın son rakamı, b = satır sayısı(toplam eleman sayısı) olarak alınır ve kendimizin belirleyeceği delta değerine göre
    #bulunmuş olan en uygun polinomun integrali döndürülür.
def integral1():
    a = 180401026 % 10
    b = len(datas)
    deltax = 0.1
    integral = 0

    n = int((b - a) / deltax)
    denklem = fx(x)
    for i in range(n):
        integral += deltax * (denklem.subs({x:a}) + denklem.subs({x:a + deltax}) ) / 2
        a += deltax

    return integral

#bu kısımda a = okul numaramın son rakamı, b = satır sayısı(toplam eleman sayısı) olarak alınır ve kendimizin belirleyeceği delta değerine göre
    #veriler dosyasından okuğumuz değerlerin integrali döndürülür.
def integral2():
    a = 180401026 % 10
    b = len(datas)
    deltax = 1
    integral = 0

    n = int((b - a) / deltax)

    for i in range(n-1):
        integral += deltax * (datas[a] + datas[a + deltax]) / 2
        a += deltax

    return integral

def yazdirma():
    # en_uygun_polinom(datas, n, yitoplam)
    print("--------------------------------------------------------------")
    print("\n\n")
    print("En Uygun Polinom =", bireenyakindeger(cozumlerilistele(datas, n), datas, n, yitoplam)[0][0],
          ". Dereceden Polinomdur.")
    print("\nBulunan denklem:")
    print(fx(x))  # denklem haline getirilmiş fonksiyon yazılır.
    print("\n\n")
    print("--------------------------------------------------------------")
    print("\n\n")
    print("En uygun polinomun integrali = ", integral1())  # en uygun polinomun integrali yazılır
    print("\n\n")
    print("--------------------------------------------------------------")
    print("\n\n")
    print("Polinom olmadan bulunan integral = ", integral2())  # dosyadan okunan veriler kullanılarak bulunan integral yazılır
    fnew = open("180401026-yorum.txt", 'w', encoding='UTF8')
    fnew.write("Deltax(dikdörtgenin eni) değerini ne kadar küçültürsek bulacağımız değer o kadar gerçeğe yakın olur.\n")
    fnew.write("Bunun nedeni: integrali, polinomu küçük dikdörtgenler haline getirip bu dikdörtgenlerin alanlarını toplayarak bulmamızdır.\n")
    fnew.write("Yani, deltax ne kadar küçültülürse, işleme katılacak alan sayısı artar ve gerçeğe daha yakın değerler elde edilir.\n")
    fnew.write("Ancak işlem daha uzun sürer.\n")
    fnew.write("Polinomsuz hesapta bir polinomdan değil, elimizdeki verilerden yararlanıyoruz ve deltax'i 1 aldığımız için dikdörtgeni daha küçük parçalara bölemiyoruz.\n")
    fnew.write("Bu sebepten dolayı, polinom ile bulduğumuz integral, polinomsuz bulduğumuza göre daha doğru bir sonuç verecektir.")

yazdirma()
