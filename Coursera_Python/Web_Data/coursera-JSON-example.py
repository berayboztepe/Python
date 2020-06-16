#same examples as we did with XML, now we're doing this with json

import json
data = '''{
    "name" : "Chuck", 
    
    "phone" : {
        "type" : "intl1",
        "number" : "+1 734 850 0001"
    },
    "email" : {
        "hide" : "yes"
    }
}
'''

info = json.loads(data)
print("Name: ", info["name"])
print("Phone Number: ", info["phone"] ["number"])
print("Phone Type: ", info["phone"] ["type"])
print("Hide: ", info["email"] ["hide"])
print("\n\n")

input = '''[
    {
    "id" : "0101",
    "name" : "Emre",
    "x" : 2
    },
    {
    "id" : "0110",
    "name" : "Beray",
    "x" : 3
    }
]
'''

info1 = json.loads(input)
print("User Count: ", len(info1))
print("\n")
for item in info1:
    print("Name: ", item["name"])
    print("ID: ", item["id"])
    print("Attribute: ", item["x"])