def solution(dot):
    answer = 0
    # 1사분면
    if dot[0] > 0 and dot[1] > 0:
        answer = 1
    # 2사분면
    elif dot[0] < 0 and dot[1] > 0:
        answer = 2
    # 3사분면
    elif dot[0] < 0 and dot[1] < 0:
        answer = 3
    # 나머지 
    else:
        answer = 4
    return answer