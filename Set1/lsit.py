list1 = ["first","second","third","fourth"]
print(len(list1))
print(type(list1))
print(list1[0:3])
print(list1[2])

if "second" in list1:
    print("Yes! it is")
    
list1[1] = "newitem"
print(list1)

list1.insert(0,"lol")
print(list1)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

    