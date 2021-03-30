# 숫자 카드 게임
#n,m = map(int, input().split())
#lst = list(map(str, input().split()))

import time
start_time= time.time()

n,m = 2,4
lst = [7,3,1,8,3,3,3,4]

new_list = []
for i in range(n):
    new_list.append(min(lst[m*(i):m*(i+1)]))
result = max(new_list)

print('result=',result)
            


print("time:", time.time()-start_time)
