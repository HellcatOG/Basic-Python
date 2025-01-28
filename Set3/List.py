list = ["Pranav", "Kichu", "Achu", "Kichu", "Pranav"] #List items are ordered, changeable, and allow duplicate values.
print(list[2:])
#
list[3:5] = ["Prathyush","Vichu"]
print(list)
list.insert(6,"Akshidev") #add to a spisefic index
print(list)
list.append("Sree")
print(list)

Madathil = ["Sarojaniamma"]
for i in list:
    Madathil.append(i) #add to the last index
print(Madathil)

Madathil.remove("Kichu") #remove the fist elemet is multiple exist
print(Madathil)

Madathil.pop(2) #Pop removes with the specifed index and if not specifed tthe last index is removed
print(Madathil)
Gokulam= []

for x in Madathil:
    if "P" in x:
        Gokulam.append(x)
print(Gokulam)

Madathil.sort() #will sort the list alphanumerically, ascending, by default:
print(Madathil)
    
Madathil.sort(reverse = True) #To sort descending, use the keyword argument reverse = True:
print(Madathil)



