def solution(num_list):
    answer = 0
    sum1 = 0
    sum2 = 0
    for idx, i in enumerate(num_list):
        if idx % 2 : 
            sum1 += i
        else:
            sum2 += i
    if sum1 > sum2:
        answer = sum1
    else:
        answer = sum2
    return answer