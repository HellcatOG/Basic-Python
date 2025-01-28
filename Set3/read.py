try:
    f = open("sale.txt", "r")
    for x in f:
        print(x)
    f.close()
except FileNotFoundError:
    print("file Not found exception")

#output



