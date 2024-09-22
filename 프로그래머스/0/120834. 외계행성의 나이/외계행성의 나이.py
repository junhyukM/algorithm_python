def solution(age):
    answer = ''
    age_al = 'abcdefghijklmnopqrstuvwxyz'

    age_list = list(map(int, str(age)))
    for i in age_list:
        answer += age_al[i]
        
    return answer