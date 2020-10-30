file = open("input.txt", "r", encoding="utf-8")
file1 = open("1.txt", "r")
kelimeListe = {}
kelimeListeFrekans = {}
artGelenKelime = ""
enCokKey=0

def keySirala(kelimeListe):
    global enCokKey
    dictCounter = 0
    for key, value in kelimeListe.items():
        if (dictCounter == 0):
            enCokKey = key
            enCokVal = value
            dictCounter = dictCounter + 1
        if (enCokVal <= value):
            enCokVal = value
            enCokKey = key
    return enCokKey


def frekansDondur(file1):
    for frekansSatir in file1:
        list = frekansSatir.split()
        for i in list:
            if i in kelimeListeFrekans.keys():
                kelimeListeFrekans[i] = kelimeListeFrekans[i] + 1
            else:
                kelimeListeFrekans[i] = 1
    dictCounter = 0
    for key, value in kelimeListeFrekans.items():
        if (dictCounter == 0):
            enCokKey = key
            enCokVal = value
            dictCounter = dictCounter + 1
        if (enCokVal <= value):
            enCokVal = value
            enCokKey = key
    return enCokKey


for i in file:
    listInput = i.split()
    if(len(listInput)<=5):
         fileCounter=1
         while(fileCounter<=10):
             fileString = str(fileCounter)+".txt"
             file = open(fileString, "r")
             for k in file:
                 listData=k.split()
                 inputCounter = 0
                 if(len(listInput)>0 and len(listInput)> inputCounter):
                     for listDataIndex in range(len(listData)):
                             if artGelenKelime in kelimeListe.keys():
                                kelimeListe[artGelenKelime] = kelimeListe[artGelenKelime] + 1
                                artGelenKelime=""
                             else:
                                if(artGelenKelime!=""):
                                    kelimeListe[artGelenKelime] = 1
                                    artGelenKelime=""

                             if(inputCounter==len(listInput)):
                                 break

                             if listData[listDataIndex] == listInput[inputCounter]:
                                 inputCounter=inputCounter+1
                                 if(inputCounter==len(listInput)):
                                     listDataIndex=listDataIndex+1
                                     artGelenKelime=listData[listDataIndex]
                                     inputCounter=0

             fileCounter=fileCounter+1

    f = open("output.txt", "a")

    if(len(kelimeListe)==0):
        if(len(listInput)>=5):
            f.write(i+" - hatalı giriş : en fazla 5 kelime girmelisiniz"+'\n')
        else:
            frekVal = frekansDondur(file1)
            f.write(i[0:(len(i) - 1)] + " " + frekVal+'\n')

    if(len(kelimeListe)!=0):
        f.write(i[0:(len(i) - 1)] + " " +keySirala(kelimeListe)+'\n')
        kelimeListe = dict()

    f.close()
