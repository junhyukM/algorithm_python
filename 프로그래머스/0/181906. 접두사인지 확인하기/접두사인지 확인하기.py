def solution(my_string, is_prefix):
    answer = 0
    temp = ''
    if len(is_prefix) < len(my_string):
        for i in range(len(is_prefix)):
            if my_string[i] == is_prefix[i]:
                temp += is_prefix[i]
        if is_prefix == temp:
            answer = 1
    return answer