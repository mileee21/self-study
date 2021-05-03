# 삽입 정렬 소스코드

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]: # 자기보다 앞에 있는 데이터가 더 크면 
            array[j], array[j-1] = array[j-1], array[j] # 서로 위치를 바꿔서 자신이 앞으로 감
        else: # 자신보다 작은 데이터를 만나면
            break

print(array)