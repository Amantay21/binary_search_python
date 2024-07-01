# def binary_search(list,item):
#     list.sort()
#     low = list[0]
#     high = len(list[-1])
    
#     while low <= high:
#         middle = low+(high-low)//2
#         print("Middle: ",middle)
#         if list[middle] == item:
#             return [middle]
#         if list[middle] == item:
#             return middle
#         elif list[middle] > item:
#             high = middle-1
#         else:
#             low = mid+1
        
#     return -1

# my_list = [12,2,32,44,12,765,324,2,3,1,6,8]

# print(binary_search(my_list,32))
def binary_search(lst, item):
    lst.sort() 
    print(lst)# Ensure the list is sorted
    low = 0
    high = len(lst) - 1
    num=1
    while low <= high:
        middle = (low + high) // 2
        print("Попытка №",num)
        print("Middle index:", middle, "Middle value:", lst[middle])
        if lst[middle==item]:
            print(f"Обьект найден! {lst[middle]}")
        num+=1
        if lst[middle] == item:
            return middle
        elif lst[middle] > item:
            high = middle - 1
        else:
            low = middle + 1
        
    return 

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
print(binary_search(my_list, 17))
