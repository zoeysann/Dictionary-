
# 6->7->5

grades = {
    "zoey": 85,
    "luca": 90,
    "mia": 100,
    "owen": 90,
    "chloe": 65,
    "grace": 40
}

subjects = {
    "math": "zoey",
    "chemistry": "luca",
    "math": "mia",
    "physics": "owen",
    "chemistry": "chloe",
    "math": "grace"
}

dicts = {
    "subjects": subjects,
    "grades": grades
}

#task 7
grades.update({"zoey":95})

#for task 5 I've 2 idea
len=len(grades)
sum=0

for i in grades.values():
    sum = sum + i
print("Average: ", sum/len)

# or
sum=0
for i in grades:
    sum = sum + grades[i]
print("Average: ", sum/len)
    