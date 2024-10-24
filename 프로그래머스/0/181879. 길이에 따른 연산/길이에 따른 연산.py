def solution(num_list):
    answer = 0
    temp = 1
    if len(num_list) >= 11:
        answer = sum(num_list)
    else:
        for i in range(len(num_list)):
            temp *= num_list[i]
        answer = temp
    return answer