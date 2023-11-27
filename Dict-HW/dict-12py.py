words={
    "hello": 5,
    "wassup": 6,
    "how's going": 9,
    "bye": 3
    }
h=0
val_list=list(words.values())
for i in val_list:
    if i>h:
        h=i

index_h=val_list.index(h)
key_list=list(words.keys())

print("The word with the Highest frequence is: ",key_list[index_h])
