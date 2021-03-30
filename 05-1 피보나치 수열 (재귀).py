# 피보나치 수열 구하기
#오류버전
'''
def f_num(n):
    
    if n==1: #조건에 문제가 있네!!!!!!!
        return n
    else:
        result= f_num(n-1)+f_num(n-2) #0, -1, -2 계속 내려가서 ^^^^^^ 무한대^^^
    return result
    
print(f_num(2))

'''
#제대로 돌아가는 버전 
def f_num(n):
    
    if n<=1: 
        return n
    result= f_num(n-1)+f_num(n-2)
    return result
    
    
print(f_num(7))
