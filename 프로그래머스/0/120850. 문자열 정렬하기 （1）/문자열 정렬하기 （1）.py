def solution(my_string):
    answer = []
    # 문자열의 요소를 순서대로 가져오기
    for i in my_string:
        # 문자인지 숫자인지 구분하기
        if i.isdigit():
            answer.append(int(i))
    answer.sort()

    return answer