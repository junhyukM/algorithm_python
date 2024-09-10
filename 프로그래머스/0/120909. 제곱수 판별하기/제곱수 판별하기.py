def solution(n):
    answer = 0
    # 제곱수인지 여부 확인
    for i in range(1,n):
        if n % i == 0 and n == i**2:
            return 1
        else:
            answer = 2
    return answer