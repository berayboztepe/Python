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
    print("Günlere göre sadece o günde yaşanan vaka(2.günden itibaren)")
    for i in range(1, len(diagnose)):
        x_values.append(i+1)
        y = (diagnose[i] - diagnose[i-1])
        y_values.append(y)
    print(y_values)
    plt.plot(x_values, y_values)
    plt.show()

def sadece_o_gün_içindeki_ölüm_sayısı_grafiği():
    x_values, y_values = [], []
    print("Günlere göre sadece o günde yaşanan ölüm(2.günden itibaren)")
    for i in range(1, len(deaths)):
        x_values.append(i + 1)
        y = (deaths[i] - deaths[i - 1])
        y_values.append(y)
    print(y_values)
    plt.plot(x_values, y_values)
    plt.show()

def toplam_ölüm_sayısının_toplam_vaka_sayısına_oranı():
    x_values, y_values = [], []
    print("Bölümün günlere göre sonuçları")
    for i in range(0, len(deaths)):
        y = deaths[i] / diagnose[i]
        y_values.append(y)
        x_values.append(i+1)
        print(i, y)
    plt.plot(x_values, y_values)
    plt.show()


print("1-Toplam vakaların günlere göre grafiği \n")
print("2-Toplam ölümlerin günlere göre grafiği \n")
print("3-Sadece bir günde yaşanan vakaların grafiği(2.günden itibaren) \n")
print("4-Sadece bir günde yaşanan ölümlerin grafiği(2.günden itibaren)  \n")
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

