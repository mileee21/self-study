# 곱하기 혹은 더하기

num_list = input()

total = 1

for n in num_list:
    if n == '0':
        continue
    elif n=='1':
        total+=1
    else:
        total = total*int(n)

print(total)