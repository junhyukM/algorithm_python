def solution(my_string):
    answer = ''
    for w in range(1, len(my_string) + 1):
        answer += my_string[-w]
        
    return answer