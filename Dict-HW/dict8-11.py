dict = {
    "name": "Zoey",
    "surname": "Everglen",
    "age": 17,
    "city": "Baku"
    }
#tasks 8-9-10-11

if "name" in dict:
    print("Yes, Exists")

for i in dict:          # prints keys
    print(i)
for i in dict.keys():
    print(i)

for i in dict:          # prints values
    print(dict[i]) 
for i in dict.values():
    print(i)

for i in dict.items():  # keys and values all together
    print(i)

print(dict)             # and this is the simple one hahah but 
                        # I loved items() method more than this 