def solution(my_string):
    answer = 0
    # 공백 제거
    my_string = my_string.replace(" ", "")
    
    # 문자열 계산
    answer = eval(my_string)
    
    return answer