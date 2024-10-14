def solution(dots):
    answer = 0
    temp = dots[0]
    x_len = 0
    y_len = 0
    for i in dots[1:]:
        if temp[0] == i[0]:
            x_len = abs(temp[1] - i[1])
        elif temp[1] == i[1]:
            y_len = abs(temp[0] - i[0])
    answer = x_len * y_len    
    
    return answer