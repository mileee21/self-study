# 09 문자열 압축

def solution(s):
    
    repeat = 1
    answer = len(s)
    compressed = ''
    
    for i in range(1,len(s)//2+1):
        
        for j in range(0,len(s),i):
            
            if s[j:j+i] == s[j+i:j+i+i]:
                #print(s[j:j+i],s[j+i:j+i+i],i)
                repeat += 1
                
                
            else:
                #if len(s[j+i:j+i+i])== i or len(s[j+i:j+i+i])== 0:
                #print(s[j+i:j+i+i])
                if repeat == 1:
                    compressed += s[j:j+i]
                    continue
                
                else:
                    compressed += str(repeat) + s[j:j+i]
                    repeat = 1
                    
        #print(i, compressed)
        if len(compressed) < answer:
            answer = len(compressed)
            
        compressed = ''
        
        
    return answer

s = "aaaaaaaaaabbb"
print(solution(s))