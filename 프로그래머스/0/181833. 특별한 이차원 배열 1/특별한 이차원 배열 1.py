def solution(n):
    answer = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        answer.append(temp)
    for i in range(n):
        answer[i][i] = 1
        
    return answer