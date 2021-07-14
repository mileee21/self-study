# 08 선택 정렬 알고리즘

def sel_sort(a):
    for i in range(0,len(a)-1):
        min_indx = i 
        
        for j in range(i+1, len(a)):
            
            if a[j] < a[min_indx]:
                min_indx = j
                a[i], a[min_indx] = a[min_indx], a[i]
    return a
            
d = [5,3,2,1,4]
print(sel_sort(d))