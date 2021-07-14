# 07-1 위치를 모두 return 

def search_list(a,x):
    n = len(a)
    find_list = []
    for i in range(0, n):
        if x == a[i]:
            find_list.append(i)
        
    return find_list

v = [17, 92, 18, 33, 18]

print(search_list(v, 18))
print(search_list(v, 8))