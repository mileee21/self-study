# 07-3 학생 번호로 학생 찾기 

def search_stu(num_list, stu_list, num):
    n = len(num_list)
    
    for i in range(0, n):
        if num == num_list[i]:
            return stu_list[i]
                
    return "?"

num_list = [34, 15, 6]
stu_list = ['John', 'Amy', 'Mary']

print(search_stu(num_list, stu_list, 15))
print(search_stu(num_list, stu_list, 4))