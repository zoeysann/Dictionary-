dict = {
    "name": "Zoey",
    "surname": "Everglen",
    "age": 17,
    "personality": "artsy",
    "city": "Baku",
    }
# 1st-print, 2nd-add, 3rd-remove 
print(dict["name"])
# simple way, using update() or setdefault() methods
dict["occopuation"]= "study"
dict.update({"occopuation":"study"})
dict.setdefault("occopuation", "study")
# pop() method or del built-in function
dict.pop("city")
del dict["city"]
