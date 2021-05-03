array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    # 리스트가 하나 이상의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 피벗 = 첫번째 원소
    tail = array[1:] # tail은 피벗 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot] # tail에서 피벗보다 작은 수들
    right_side = [x for x in tail if x > pivot] # tail에서 피벗보다 큰 수들
    
    # 작은수, 큰수 각각 또 퀵정렬의 과정 거치고 피벗 기준으로 붙이기
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
    
        