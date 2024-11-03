def solution(numLog):
    answer = ''
    for i in range(1,len(numLog)):
        if (int(numLog[i]) - int(numLog[i-1])) == 1:
            answer += 'w'
        elif (int(numLog[i]) - int(numLog[i-1])) == -1:
            answer += 's'
        elif (int(numLog[i]) - int(numLog[i-1])) == 10:
            answer += 'd'
        elif (int(numLog[i]) - int(numLog[i-1])) == -10:
            answer += 'a'
    return answer