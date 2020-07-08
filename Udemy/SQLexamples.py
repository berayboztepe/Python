import sqlite3

connection = sqlite3.connect("chinook.db")

#order and where
#besteci isimlerini normal yazar, besteciler aynıyken şarkı isimlerini tersten sıralar.
curser = connection.execute('''select * from tracks where genreID = 3
            order by Composer, Name desc

            ''')
#desc yazarsak tersten yazar

for row in curser:
    print("Composer Name = ", row[5], "--------", "Song Name = ", row[1])



#group by(hangi şehirden kaç tane var mesela*** ve kücükten büyüğe sırala
curser = connection.execute(''' select  BillingCity, count(*) from invoices group by BillingCity

    having count(*)>7 order by count(*)

''')
#having ile sayısı x'ten büyük olanları yazdır diyoruz

for row in curser:
    print("City = ", row[0])
    print("Count = ", row[1])
    print("*************")


#içerisinde a geçen besteciler. %a% ilk % = başı önemli değil, sondaki % = sonu önemli değil, a = o harf var mı(like)
#'a%' = a ile başlayacak, '%a' = a ile bitecek
curser = connection.execute(''' select * from customers where firstname like '%j%'

 ''')
for row in curser:
    print("Name = ", row[1])
    print("*************")


#insert ile yeni row ekleme
connection.execute(''' insert into customers (FirstName, LastName, Company, Address, City, State, Country, PostalCode, Phone, Fax, Email)
values ('Beray', 'Boztepe', '', 'Barbaros Mah.', 'Çanakkale', 'TR', 'Turkey', '17100', '+90 213 43241', '', 'deneme@hotmail.com')

''')
"""for row in curser:
    print("Name = ", row[1])
    print("*************")"""
connection.commit()


connection.execute(''' update customers set CustomerId = 60 where CustomerId = 66 

''')

connection.commit()

connection.close()


