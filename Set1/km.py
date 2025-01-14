print("Program Output")
print("KPH"  "\t"  "MPH")
print("-----------")
for i in range (60,131,10):
    mph = i * 0.6214
    print(f"{i}\t{mph:.1f}")
