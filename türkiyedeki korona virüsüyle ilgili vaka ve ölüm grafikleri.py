import matplotlib.pyplot as plt
import sympy as sym

corona = open("günler_korona.txt", "r")
# ; o gün ve öncesindeki toplam vaka sayısı ; o gün ve öncesindeki toplam ölüm sayısı

deaths = []
diagnose = []

def günlerdeki_toplam_vaka_ve_ölüm_sayısı():
    for i in corona:
        deaths.append(int(i.split(";")[2]))
        diagnose.append(int(i.split(";")[1]))

    print("Vakaların listesi", diagnose)
    print("\n")
    print("Ölümlerin Listesi", deaths)
    print("\n")


def günlerdeki_toplam_vaka_sayısı_grafiği():
    x_values, y_values = [], []
    print("Günlere göre toplam vaka")
    for i in range(0, len(diagnose)):
        x_values.append(i+1)
        y_values.append(diagnose[i])
        print(i+1, y_values[i])

    plt.plot(x_values, y_values)
    plt.show()

def günlerdeki_toplam_ölüm_sayısı_grafiği():
    x_values, y_values = [], []
    print("Günlere göre toplam ölüm")
    for i in range(0, len(deaths)):
        x_values.append(i + 1)
        y_values.append(deaths[i])
        print(i + 1, y_values[i])

    plt.plot(x_values, y_values)
    plt.show()

def sadece_o_gün_içindeki_vaka_sayısı_grafiği():
    x_values, y_values = [], []
    counter = 1
    print("Günlere göre sadece o günde yaşanan vaka")
    y_values.append(1)
    x_values.append(counter)
    for i in range(0, len(diagnose)):
        if i+1 >= len(diagnose):
            break
        else:
            counter += 1
            x_values.append(counter)
            y = (diagnose[i+1] - diagnose[i])
            y_values.append(y)
    counter1 = 0
    for i in range(len(diagnose)):
        if counter1 >= len(diagnose):
            break
        print("gün = ", counter1 + 1, "vaka = ", y_values[counter1])
        counter1 += 1
    #print(y_values)
    #print(x_values)
    plt.plot(x_values, y_values)
    plt.show()

def sadece_o_gün_içindeki_ölüm_sayısı_grafiği():
    x_values, y_values = [], []
    counter = 1
    print("Günlere göre sadece o günde yaşanan ölüm")
    y_values.append(0)
    x_values.append(counter)
    for i in range(0, len(deaths)):
        if i + 1 >= len(deaths):
            break
        else:
            counter += 1
            x_values.append(counter)
            y = (deaths[i + 1] - deaths[i])
            y_values.append(y)
    counter1 = 0
    for i in range(len(deaths)):
        if counter1 >= len(deaths):
            break
        print("gün = ", counter1 + 1, "ölüm = ", y_values[counter1])
        counter1 += 1
    #print(x_values)
    plt.plot(x_values, y_values)
    plt.show()

def toplam_ölüm_sayısının_toplam_vaka_sayısına_oranı():
    x_values, y_values = [], []
    print("Bölümün günlere göre sonuçları")
    for i in range(0, len(deaths)):
        y = deaths[i] / diagnose[i]
        y_values.append(y)
        x_values.append(i+1)
        print(i+1, y)
    plt.plot(x_values, y_values)
    plt.show()


print("1-Toplam vakaların günlere göre grafiği \n")
print("2-Toplam ölümlerin günlere göre grafiği \n")
print("3-Sadece bir günde yaşanan vakaların grafiği \n")
print("4-Sadece bir günde yaşanan ölümlerin grafiği  \n")
print("5-O gündeki toplam ölüm sayısının, yine o gündeki toplam vaka sayısına bölünmesinden çıkan sonuç grafiği \n")
secim = int(input("Görmek istediğiniz grafiği seçin:"))

günlerdeki_toplam_vaka_ve_ölüm_sayısı()
if(secim == 1):
    günlerdeki_toplam_vaka_sayısı_grafiği()
elif (secim == 2):
    günlerdeki_toplam_ölüm_sayısı_grafiği()
elif (secim == 3):
    sadece_o_gün_içindeki_vaka_sayısı_grafiği()
elif (secim == 4):
    sadece_o_gün_içindeki_ölüm_sayısı_grafiği()
elif(secim == 5):
    toplam_ölüm_sayısının_toplam_vaka_sayısına_oranı()
else:
    print("\nSeciminiz yanlış")


corona.close()


