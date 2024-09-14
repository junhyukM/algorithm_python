def solution(my_string):
    answer = 0
    # 문자열을 받아서 숫자만 추려서 덧셈을 해라
    for i in my_string:
        if ord(i) < 58:
            answer += int(i)
    return answer