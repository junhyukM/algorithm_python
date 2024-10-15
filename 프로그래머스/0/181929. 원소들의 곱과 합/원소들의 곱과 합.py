def solution(num_list):
    sum_num = 0
    mul_num = 1
    for i in num_list:
        sum_num += i
        mul_num = mul_num * i
    if mul_num < (sum_num**2): 
        answer = 1
    else:
        answer = 0
    return answer