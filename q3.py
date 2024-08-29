def binary_search(array,target):   
    mid=len(array)//2
    if(array == []):
        return False
    if (array[mid] == target):
        return True
    elif (array[mid] > target):
        return binary_search(array[:mid],target)
    elif (array[mid] < target):
        return binary_search(array[mid+1:],target)
    else:
        return False
list = input("Enter elements: ").split()
list = [int(num) for num in list]
target_num = int(input("enter target num: "))
target_list=[]
for i in list:
    result = binary_search(list,target_num-i)
    if(result):
        list.remove(i)
        target_list.append([i,target_num-i])
print(target_list)
