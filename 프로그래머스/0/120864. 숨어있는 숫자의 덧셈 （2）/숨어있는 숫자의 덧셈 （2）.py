def solution(my_string):
    answer = 0
    temp = ''
    for n in my_string:
        if n.isdigit(): # 문자형으로 반환
            temp += n # 연속해서 숫자가 나오면 덧셈이 아닌 문자열 연결
        # temp에 값이 있는게 참일 때
        elif temp:
            answer += int(temp) # temp에 작성된 문자열을 int로 바꾸고 최종 답에 덧셈
            temp = '' # 다음 루프를 위해 temp 초기화
    if temp:
        answer += int(temp)
        
    return answer