n,m,k = 5,8,3
data = [2, 4 ,5, 4 ,6]

import time
start_time= time.time()

#n, m, k = map(int, input().split())
#data = list(map(int, input().split()))

data.sort()

first = data[-1]
second = data[-2]

result = 0

while m>0:
    for i in range(k):
        result+=first
        m-=1
    result+=second
    m-=1
    
    
print('result = ', result)


print("time:", time.time()-start_time)
    
