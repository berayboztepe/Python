from sympy import FiniteSet

# Liste içersinden eleman sayısı bulma

liste_1 = [0,5,25,100,5,5,0,100]
def my_h(liste_1):
    my_d = {}
    for i in liste_1:
        if i in my_d:
            my_d[i]=my_d[i] + 1
        else:
            my_d[i] = 1
    return my_d
print(my_h(liste_1))

#Liste içersinden eleman sayısı bulmak için farklı bir yol

liste_1 = [0,5,25,100,5,5,0,100]
def my_h(liste_1):
    my_d = {}
    for i  in liste_1:
        if i not in my_d:
           my_d[i] = 1
        else:
            my_d[i] +=1
    return my_d
print(my_h(liste_1))

# Fibonacci hesaplama recursive

known={0:0,1:1}
def fibo_rec(n):
    if n in known:
        return known[n]
    else:
        result = fibo_rec(n-1) + fibo_rec(n-2)
        known[n]=result
        return result
x=fibo_rec(10)
print(x)



# Gönderilen sayının listede olup olmadığının kontrol edilmesi(1 ise var, 0 ise yok)
def lookup(d,v):
    for key in range(0,len(liste_1)):
        if d[key]==v:
            return 1
    else:
        return 0

liste_1= [0,5,25,100,5,5,0,100]
print(lookup(liste_1,5100))


#sayının asal sayı olup olmadığını bulma

def check_prime(number):
    if number!=1:
        for i in range(2,number):
            if number%i==0:
                return False
    else:
        return False
    return True

#1-21 arasında sınırlanmış asal sayıları bulma ve bu asal sayıların sayısının 1-21 arasındaki sayı adetine bölünmesi

def probability(space,event):
    return len(event)/len(space)

space =FiniteSet(*range(1,21))#toplam 20 sayı var
primes =[]
for num in space:
    if check_prime(num):
        primes.append(num)
event=FiniteSet(*primes)#bu sayılardan 8 tanesi asal
p=probability(space,event)
print(p)