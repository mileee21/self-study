# 07 럭키 스트레이트

num = input()

left = num[0:int(len(num)/2)]
right = num[int(len(num)/2):]


left_sum = sum(map(int, left))
right_sum = sum(map(int, right))

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
