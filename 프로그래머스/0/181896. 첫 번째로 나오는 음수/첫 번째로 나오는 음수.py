def solution(num_list):
    answer = 0
    for idx, i in enumerate(num_list):
        if i < 0 :
            answer = idx
            break
        if idx == len(num_list)-1:
            answer = -1
    return answer