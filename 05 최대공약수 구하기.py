#greatest common factor = 최대 공약수 구하는 알고리즘
def gcf(a,b):
    i = min(a,b)
    #while True: - 왜 넣는거지?
    if a%i==0 and b%i==0:
        return i
    i=i-1
        
        
#print(gcf(81,27))
        
# 유클리드 알고리즘 - 재귀로 풀기
'''
a와 b의 최대공약수는 b와 a를 b로 나눈 나머지의 최대공약 + a와 0의 최대공약수는 a
gcd(a,b) = gcd(b, a%b), gcd(a,0)=a

ex) gcd(60,24) = gcd(24,60%24) = gcd(24,12) = gcd(12, 24%12) = ... gcd(27,0) = 27

즉 이 친구들은 재귀로 돌아가면서 어떤 수와 0이 되는 순간을 찾는거
'''

def u_gcd(a,b):
    if b==0: # 종료 조건
        return a
    return u_gcd(b, a%b)

print(u_gcd(60,24))
        


