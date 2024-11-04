def solution(my_strings, parts):
    answer = ''
    for idx, i in enumerate(parts):
        temp = my_strings[idx]
        answer += temp[i[0]:i[1]+1]
    return answer