def solution(myString):
    answer = ''
    temp = 'abcdefghijklmnopqrstuvwxyz'
    for i in myString:
        if i in temp[:12]:
            answer += 'l'
        else:
            answer += i
    return answer