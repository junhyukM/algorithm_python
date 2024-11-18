def solution(myString):
    answer = []
    temp = myString.split('x')
    for i in temp:
        if i == '':
            continue
        else:
            answer.append(i)
    answer.sort()
    
    return answer