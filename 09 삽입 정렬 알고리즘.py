# 삽입 정렬 알고리즘

def ins_sort(a):
    
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        
        
        while j>=0 and a[j] > key:
            a[j+1] = a[j]
            #print(a)
            j -= 1
        
        a[j+1] = key
        
    return a

d = [5,3,2,1,4]
print(ins_sort(d))