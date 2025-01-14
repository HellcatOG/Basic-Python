list1 = [5,5,5,1,4,7,5,9,10]

def list_process(num):
    remove_duplicate = []
    for i in num:
        if i in remove_duplicate:
            pass
        else:
            remove_duplicate.append(i)
    remove_duplicate.sort()
    print(remove_duplicate)

list_process(list1)

list1 = [5, 5, 5, 1, 4, 7, 5, 9, 10]

# def list_process(num):
#     unique_sorted = sorted(set(num)) if converted to set
#     print(unique_sorted)
# 
# list_process(list1)
