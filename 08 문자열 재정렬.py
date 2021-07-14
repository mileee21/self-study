# 08 문자열 재정렬
import re

K = input()

str_p = re.compile("[A-Z]")
strr = str_p.findall(K)
strr.sort()


num_p = re.compile("[\d]")
num = num_p.findall(K)
num_sum = sum(map(int, num))

string_sort = "".join(strr)


print(string_sort+str(num_sum))