def solution(myString, pat):
    answer = 0
    reverse_str = ''
    for i in myString:
        if i == 'A':
            reverse_str += 'B'
        else:
            reverse_str += 'A'
    if pat in reverse_str:
        answer = 1
        
    return answer