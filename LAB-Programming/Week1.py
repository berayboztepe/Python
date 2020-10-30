#istenen bir sayının istenen bir kuvvetini veren fonksiyon

def power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a*power(a, b-1)
print (power(4,3))

#recursive version
def power(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        if b % 2 == 0:
            return power(a*a, b//2)
        else:
            return power(a*a, b//2)*a
        #return a*power(a, b-1)
print (power(5, 3))

#verilen bir listede ardışık olan sayılardaki en yüksek toplam ve listeyi sağ, sol olarak ikiye böldüğümüzde sol tarafa sağdan, sol tarafa sağdan gidilirkenki ardışık sayıların en yüksek toplamı
liste_1=[4,-3,5,-2,-1,2,6,-2]
max=0
for i in range(8):
    for j in range(i,8):
        t=0
        for k in range(i,j):
            t=t+liste_1[k]
    if max<t:
        max=t
        i_1,i_2=i,j
print(max,i_1,i_2)