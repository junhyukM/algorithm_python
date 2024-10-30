def solution(my_string, is_suffix):
    answer = 0
    temp = my_string[-len(is_suffix):]    
    if is_suffix == temp:
        answer = 1
    return answer