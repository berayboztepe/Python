#Emre Beray BOZTEPE 180401026
#Bilimsel hesaplama dersi için verilmiş vize ödevi çözümüm. Verilen verileri 1-6 dereceden polinomalara yaklaştırarak en uygun polinomu seçme
#daha sonra bu veri gruplarını 10'arlı gruplara ayırarak aynı işlemi tekrar yapma

file = open("veriler.txt", "r")
datas = []

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

"""print(kullanilacakxdegerleri(datas))
print(xiyitoplamlari(datas))
print(yitoplam)"""

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
#print(cozumlerilistele())
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

#print(bireenyakindeger(cozumlerilistele()))
#tüm veriler için önce bulunan katsayılar ve korelasyon sayıları yazdırılıyor, sonra en uygun polinom yazdırılıyor.
def yazdirma():
    filenew = open("sonuc.txt", "w+")
    filenew.write("*******************TUM DEGERLER ICIN*******************" + "\n\n\n")
    a = 0
    for i in cozumlerilistele(datas, n):
        filenew.write("\t\t"+ str(a+1) + ". derece"+ "\n")
        b = 0
        for k in i:
            filenew.write(str(b+1) + ". deger = " + str(k)+"\n")
            b += 1
        filenew.write("Korelasyon = " + str(korelasyonlist(cozumlerilistele(datas, n), datas, n, yitoplam)[a])+"\n")
        a += 1
    filenew.write("\n\t***Tum degerler icin en uygun polinom ve korelasyon degeri = " + str(
        bireenyakindeger(cozumlerilistele(datas, n), datas, n, yitoplam)[0]) + "***\n\n\n")

#10arlı gruplar oluşturuluyor ve bu gruplar listelere atanıyor. daha sonra bu listelerdeki değerlere göre korelasyon değerleri bulunup yazdırılıyor.
    #bu gruplar 1-10, 2-11, 3-12..., 37-46 olarak oluşturuldu

    for j in range(len(datas)):
        a = 0
        newlist = []
        if(j + 10 > len(datas)):
            break
        for l in range(j, j+10):
            newlist.append(datas[l])
        filenew.write("*******************" + str(j+1) + " ile " + str(j+10) + " arasindaki degerler icin*******************")
        filenew.write("\n\t***Bu araliktaki degerler icin en uygun polinom ve korelasyon degeri = " + str(
            bireenyakindeger(cozumlerilistele(newlist, len(newlist)), newlist, len(newlist), sum(newlist))[0]) + "***\n\n\n")
#10arlı gruplar oluşturuluyor. 0-9, 10-19..., 30-39 olarak oluşturuldu!
    bas = 1
    bit = 10
    a = 0
    for j in range(len(datas)):
        newlist = []
        if ((bit*a)+10 > len(datas)):
            break
        for l in range((bas*a*10), bit*a + 9):
            newlist.append(datas[l])
        filenew.write(
            "*******************" + str(bas*a*10) + " ile " + str(bit*a + 9) + " arasindaki degerler icin*******************")
        filenew.write("\n\t***Bu araliktaki degerler icin en uygun polinom ve korelasyon degeri = " + str(
            bireenyakindeger(cozumlerilistele(newlist, len(newlist)), newlist, len(newlist), sum(newlist))[0]) + "***\n\n\n")
        a += 1
    filenew.close()
yazdirma()


