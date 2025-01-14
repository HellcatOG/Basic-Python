# tuple =("item1", "item2", "item3", "item4")
# print(tuple[0])
# print(tuple[-4])
# print(tuple[2:5])
# if "item1" in tuple:
#     print("Yes")
# # 
# x = ("apple", "Orange", "cherry")
# # y = list(x)
# # y[1] = "kiwi"
# # x = tuple(y)
# 
# #
# z = list(x)
# z.append("BlueBerry")
# x = tuple(z)
# print(x)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)