# 07 순차 탐색

def search_list(a,x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            return i 
        
    return -1

v = [17, 92, 18, 33]

print(search_list(v, 18))
print(search_list(v, 8))