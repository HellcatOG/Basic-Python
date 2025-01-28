gokulam = {"Pranav", "Prathyush"} #Set items are unordered, unchangeable, and
print(gokulam)                    #do not allow duplicate values.

gokulam.add("Kichu")
print(gokulam)

Madathil = {"Akshaidev", "Aksharasree", "Sree",}

Madathil.update(gokulam)
print(Madathil)

Madathil.discard("Sree")
Madathil.discard("Null") #If the item to remove does not exist, discard() will NOT raise an error.
print(Madathil)

# The union() and update() methods joins all items from both sets.
# 
# The intersection() method keeps ONLY the duplicates.
# 
# The difference() method keeps the items from the first set that are not in the other set(s).
# 
# The symmetric_difference() method keeps all items EXCEPT the duplicates.


family = gokulam.union(Madathil)
print(family)
