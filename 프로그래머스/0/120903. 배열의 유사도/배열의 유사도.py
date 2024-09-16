def solution(s1, s2):
    answer = 0
    # 문자열(리스트) 두개 받아서
    # 요소끼리 비교한다. s1과 s2의 원소의 수는 다를 수 있다.
    for i in s1:
        if i in s2:
            answer += 1
    return answer