def solution(my_string):
    answer = ''
    for w in my_string:
        if w.islower():
            answer += w.upper()
        else:
            answer += w.lower()
    return answer