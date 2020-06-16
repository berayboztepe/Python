#get datas with XML
#''' = multi string
import xml.etree.ElementTree as ET

data = '''<person>
    <name>Chuck</name>
    <phone type = "intl1">+1 734 850 0001</phone>
    <email hide = "yes"/>
    </person>'''

tree = ET.fromstring(data)#take the strings and make them sense
print('Name: ', tree.find('name').text)
print('Attr: ', tree.find('email').get('hide'))
print('Phone: ', tree.find('phone').text)
print('Phone Type: ', tree.find('phone').get('type'))

input = '''<stuff>
    <users>
        <user x = "2">
            <id>0101</id>
            <name>Emre</name>
        </user>
        <user x = "3">
            <id>0110</id>
            <name>Beray</name>
        </user>
    </users>
</stuff> 
'''
print("\n\n")
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')#find count of users under user
print('User Count: ', len(lst))
for item in lst:
    print('Name: ', item.find('name').text)
    print('ID: ', item.find('id').text)
    print('Attribute: ', item.get('x'))