def hanoi(n, origin_pos, final_pos, mid_pos):
    if n==1:
        print(origin_pos,'->', final_pos)
        return # 끝내라는거
    
    hanoi(n-1, origin_pos, mid_pos, final_pos)
    print(origin_pos, '->', final_pos)
    
    hanoi(n-1, mid_pos, final_pos, origin_pos)

print("n=1")
hanoi(1,1,3,2)

print('n=2')
hanoi(2,1,3,2)