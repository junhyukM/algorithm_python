def solution(my_string, m, c):
    answer = ''
    temp = 0
    temp2 = []
    for i in range(0,len(my_string)+1,m):
        if i > 0:
            temp2.append(my_string[temp:i])
            temp = i
    for j in temp2:
        answer += j[c-1]
    return answer