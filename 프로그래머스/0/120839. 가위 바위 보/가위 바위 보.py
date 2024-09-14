def solution(rsp):
    answer = ''
    # 2 는 0으로
    # 0 은 5로
    # 5 는 2로
    for i in rsp:
        if i == '2':
            answer += '0'
        elif i == '0':
            answer += '5'
        else:
            answer += '2'
    return answer