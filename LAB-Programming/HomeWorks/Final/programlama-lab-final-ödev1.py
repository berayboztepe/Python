import random
#Öncelikle bu ödevi kimseden yardım almadan, kendi ders notlarımı kullanarak kendim yaptım. Sadece bu derste değil diğer derslerdeki
# birikimlerimden de yararlandım.

chars = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's',
         'ş', 't', 'u', 'ü', 'v', 'y', 'z']
#öncelikle random atayacağım harfleri bir diziye atadım.

#burada bir enumtype classı oluşturuyorum ve girilen orientation değerine göre bu classtan değer döndürülüyor.
class EnumtypeOri(enumerate):
    soldansaga = 0
    sagdansola = 1
    asagidanyukari = 2
    yukarikanasagi = 3

#bu fonksiyon 1. şıkkın cevabıdır. Bu fonksiyonda, kullanıcının verdiği satır ve sütun sayısına göre random harf değerleri atanıp bir matris
#oluşturuluyor ve bu matris döndürülüyor.
def matris_olustur(m, n):
    matris = [[chars[random.randint(0, len(chars)-1)] for i in range(m)] for i in range(n)]

    return matris


#print(matris_olustur(10, 10))
#Bu fonksiyon 2. şıkkın cevabıdır. Bu fonksiyonda, öncelikle yine kullanıcının girdiği satır ve sütundaki parametreler
#önce indeks haline getiriliyor sonra bu kısımdaki değer bulunuyor.
# Daha sonra  verilen orientation değerine göre bulunun değerden başlayarak kullanıcıdan alınan string değeri ekrana sıralanmış bir şekilde yazdırılıyor.
#Eğer başlanan indeks ile matris sonu arasının uzunluğu, girilen kelimenin uzunluğundan küçükse girilen kelimenin tamamı yazdırılmaz
#0: soldan sağa,
#1: sağdan sola
#2: aşağıdan yukarıya
#3: yukarıdan aşağıya

def writebyorientation(m, n, myword, orientation):
    stri = ''
    kelimelist = []
    control = False
    counter = -1
    icounter = -1
    sayac = 0
    for i in myword:
        kelimelist.append(i)


    #soldan sağa
    if orientation == EnumtypeOri.soldansaga:
        for i in a:
            counter += 1
            icounter += 1
            if m-1 == counter:
                control = True
                for j in range(n-1, len(i)):
                    a[icounter][j] = kelimelist[sayac]
                    sayac += 1
                    if sayac == len(kelimelist):
                        break
            elif control == True:
                for j in range(len(i)):
                    a[icounter][j] = kelimelist[sayac]
                    sayac += 1
                    if sayac == len(kelimelist):
                        break

            if sayac == len(kelimelist):
                break
        for i in range(len(a)):
            for j in range(len(a[0])):
                stri += a[i][j]
                stri += ' '

        print(stri)
    #sağdan sola
    if orientation == EnumtypeOri.sagdansola:
        for i in a:
            counter += 1
            icounter += 1
            if m - 1 == counter:
                control = True
                for j in range(n - 1, -1, -1):
                    a[icounter][j] = kelimelist[sayac]
                    sayac += 1
                    if sayac == len(kelimelist):
                        break
        if not sayac == len(kelimelist):
            if control == True:
                for j in range(m - 2, -1, -1):
                    for k in range(len(a[0]) - 1, -1, -1):
                        a[j][k] = kelimelist[sayac]
                        sayac += 1
                        if sayac == len(kelimelist):
                            break
                    if sayac == len(kelimelist): break


        for i in range(len(a)):
            for j in range(len(a[0])):
                stri += a[i][j]
                stri += ' '
        print(stri)
    #aşağıdan yukarıya
    if orientation == EnumtypeOri.asagidanyukari:
        for i in a:
            counter += 1
            if m - 1 == counter:
                control = True
                for j in range(n - 1, n):
                    for k in range(m - 1, -1, -1):
                        a[k][j] = kelimelist[sayac]
                        sayac += 1
                        if sayac == len(kelimelist):
                            break
                    if sayac == len(kelimelist): break
        if not sayac == len(kelimelist):
            if control == True:
                for j in range(n - 2, -1, -1):
                    for k in range(len(a) - 1, -1, -1):
                        a[k][j] = kelimelist[sayac]
                        sayac += 1
                        if sayac == len(kelimelist):
                            break
                    if sayac == len(kelimelist): break

        for i in range(len(a)):
            for j in range(len(a[0])):
                stri += a[i][j]
                stri += ' '
            stri += '\n'
        print(stri)
    #yukarıdan aşağıya
    if orientation == EnumtypeOri.yukarikanasagi:
        for i in a:
            counter += 1
            if m - 1 == counter:
                control = True
                for j in range(n - 1, n):
                    for k in range(m - 1, len(a)):
                        a[k][j] = kelimelist[sayac]
                        sayac += 1
                        if sayac == len(kelimelist):
                            break
                    if sayac == len(kelimelist): break
        if not sayac == len(kelimelist):
            if control == True:
                for j in range(n, len(a[0])):
                    for k in range(len(a)):
                        a[k][j] = kelimelist[sayac]
                        sayac += 1
                        if sayac == len(kelimelist):
                            break
                    if sayac == len(kelimelist): break

        for i in range(len(a)):
            for j in range(len(a[0])):
                stri += a[i][j]
                stri += ' '
            stri += '\n'
        print(stri)

#Bu fonksiyon 3. şıkkın cevabıdır. Öncelikle matristeki harfler bir listeye atanıyor. Daha sonra bu liste gönderilen değerliden (örneğin 5'erliden)
# başlamak üzere kendi uzunluğuna kadar gruplara ayrılıyor ve bu gruba alınan stringin kendisi ile tersinin tamamen aynı olup
# olmadığı(palindrom) tespit ediliyor.
# eğer palindrom ise tut(sol, sağ, yuk, asa. nasıl arandığına göre değişiyor.) adı verilen listeye ekleniyor
# ve harflerin gruplara ayrıldıktan sonra atandığı string temizleniyor.
#öncelikle soldan sağa ve sağdan sola olan palindromlar aranıyor, daha sonra aşağıdan yukarıya ve yukarıdan aşağıya olan palindormlar aranıyor..
#ve son olarak eğer varsa, bulunan palindromlar döndürülüyor
#palindrom aranılacak matris, ilk oluşturulan matrisin bir üst kısımda orientation yapılarak değiştirilmiş halidir!!!!
def palindrome(pal, palind):
    matrislist1 = []#soldan sağa değerler atandı
    matrislist2 = []#yukarıdan aşağı için degerler atandı.
    for i in range(len(pal)):
        for j in range(len(pal[i])):
            matrislist1.append(pal[i][j])

    for i in range(len(pal[0])):
        for j in range(len(pal)):
            matrislist2.append(pal[j][i])

    #matrislist1 = ['b','c','d','e','f','f','e','d','c','b', 'a', 'z', 'g', 'a', 'c', 'd', 'g', 'f', 'h', 'y', 'h', 'f', 'g', 'd', 'c', 'a']
    #bu listeyi test etmek için ben atadım.
    maximum = palind-1#
    #en az kullanıcıdan girilen sayılı grup olacaktır. .
    # örneğin 10 girilmiş ise 0-9, 1-10, 2-11 diye devam ediliyor(10arlı).
    #daha sonra ise 0-10, 0-11....vb. diye devam ediliyor! (11erli, 12lerli... vb.)
    tutsol = []
    tutsag = []
    tutasa = []
    tutyuk = []
    while (len(matrislist1) != maximum):
        max = maximum
        min = 0
        str = ''
        while (max != len(matrislist1)):

            for j in range(min, max+1):
                str += matrislist1[j]
            if str == str[::-1]:
                tutsol.append(str)
            str = ''
            min += 1
            max += 1
        maximum += 1

    maximum = palind - 1
    matrislist = matrislist1[::-1]#sağdan sola için değerler atandı
    while (len(matrislist) != maximum):
        max = maximum
        min = 0
        str = ''
        while (max != len(matrislist)):

            for j in range(min, max+1):
                str += matrislist[j]
            if str == str[::-1]:
                tutsag.append(str)
            str = ''
            min += 1
            max += 1
        maximum += 1

    maximum = palind - 1
    while (len(matrislist2) != maximum):
        max = maximum
        min = 0
        str = ''
        while (max != len(matrislist2)):

            for j in range(min, max + 1):
                str += matrislist2[j]
            if str == str[::-1]:
                tutyuk.append(str)
            str = ''
            min += 1
            max += 1
        maximum += 1


    maximum = palind - 1
    matrislist3 = matrislist2[::-1]#aşağıdan yukarı için değerler atandı
    while (len(matrislist3) != maximum):
        max = maximum
        min = 0
        str = ''
        while (max != len(matrislist3)):

            for j in range(min, max + 1):
                str += matrislist3[j]
            if str == str[::-1]:
                tutasa.append(str)
            str = ''
            min += 1
            max += 1
        maximum += 1
    return tutsol, tutsag, tutasa, tutyuk
#bu matrisin satır, sütun değerlerini biz belirliyoruz!
a = matris_olustur(6, 6)
pal = a
#bu fonksiyon ise 4. şıkkın cevabıdır. üstteki fonksiyonların çalışmasını test etmek için oluşturulmuştur.
def yazdirma():
    print("--------------------------------------------------------")
    print("*****************************A-Şıkkı*****************************")
    print("\n\n")
    #yazdırırken değerlerin daha rahat ve anlaşılır gözükmesi için matrisi bir string haline getiriyorum ve string halinde döndürüyorum!
    stri = ''
    for i in range(len(a)):
        for j in range(len(a[i])):
            stri += a[i][j]
            stri += ' '
        stri += '\n'
    print("Random Harfler ile Üretilen Matris =")
    print(stri)

    print("\n\n")
    print("--------------------------------------------------------")
    print("*****************************B-Şıkkı*****************************")
    print("\n\n")
    #2. şık için belirttiğim hücre (2, 3) ten itibaren yazdırıyor. ancak burada gönderilen (2, 3) değeri indeks değildir!!!!
    #örneğin [['ö', 'r', 'r'], ['ö', 'ç', 't'], ['h', 'i', 'o'], ['ı', 'f', 'e']] verilen bu matriste işaret ettiğim kısım ['ö', 'ç', 't']
    #bu kısımdaki 't' harfidir. Yani gönderilen değerler bir indeks değil, matrisin orjinal değerleridir.
    #Örneğin, 5x5'lik matrisin başlangıcını matris[1][1]-bitişini matris[5][5] olarak düşünüp ona göre parametre göndermemiz gerekir.
    #değerlerin gönderildiği fonksiyonda bu değerler indeks haline getiriliyor ve ona göre işlem yapılıyor.
    #bu satır ve sütün değerleri yine bizim tarafımızdan belirleniyor!
    myword = str(input("Bir kelime girin:"))
    orientationnum = int(input("0: soldan sağa, \n1: sağdan sola, \n2: aşağıdan yukarıya, \n3: yukarıdan aşağıya\nIstediğiniz orientation sayısını girin:"))
    if orientationnum == 0:
        print("\n\n")
        print("Belirtilen Indeksten Soldan Sağa Yazım = ")
        writebyorientation(1, 4, myword, 0)
    elif orientationnum == 1:
        print("\n\n")
        print("Belirtilen Indeksten Sağdan Sola Yazım = ")
        writebyorientation(4, 1, myword, 1)
    elif orientationnum == 2:
        print("\n\n")
        print("Belirtilen Indeksten Aşağıdan Yukarıya Yazım = ")
        writebyorientation(4, 4, myword, 2)
    elif orientationnum == 3:
        print("\n\n")
        print("Belirtilen Indeksten Yukarıdan Aşağıya Yazım = ")
        writebyorientation(2, 3, myword, 3)

    print("\n\n")
    print("--------------------------------------------------------")
    print("*****************************C-Şıkkı*****************************")
    print("\n\n")
    palind = int(input("Görmek Istediğiniz Palindrom Uzunluğunu Giriniz:"))
    #Eğer boş küme ise bu matriste palindrom yoktur!
    print("Bu Dizinin Soldan Palindrom(u)ları = ", palindrome(a, palind)[0])
    print("Bu Dizinin Sağdan Palindrom(u)ları = ", palindrome(a, palind)[1])
    print("Bu Dizinin Aşağıdan Palindrom(u)ları = ", palindrome(a, palind)[2])
    print("Bu Dizinin Yukarıdan Palindrom(u)ları = ", palindrome(a, palind)[3])


yazdirma()
