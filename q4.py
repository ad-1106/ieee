import math
def prime_factors(n):  
    list=[]  
    while n % 2 == 0:
        list.append(2)
        n = n // 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            list.append(i)
            n = n // i
    if n > 2:
        list.append(n)
    return(list)
def list_intersect(list_1, list_2):
    Intersection_set = set(list_1).intersection(set(list_2))
    Intersection_list = []
    for i in Intersection_set:
        num = min(list_1.count(i), list_2.count(i))
        for j in range(num):
            Intersection_list.append(i)
    return Intersection_list
def common_list_of_factors(list):
    common_factors=list[0]
    for i in range(len(list)):
        common_factors=list_intersect(list[i],common_factors)  
    return common_factors
list_of_factors=[]    
for i in range(1,6):
    x = int(input(f"input {i} number"))
    list_of_factors.append(prime_factors(x))
list_of_common_factors=common_list_of_factors(list_of_factors)
if len(list_of_common_factors) == 0:
    print(1)
else:
    tmp=1
    for i in list_of_common_factors:
        tmp*=i
print(tmp)

