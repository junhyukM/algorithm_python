def solution(n):
    answer = 0
    # 피자 한판당 6조각
    # 사람수는 매개변수로 주어짐
    # 사람수의 곱들 중 가장 작은 6의 배수를 구하고 그것을 6으로 나누면 판수
    person = 0
    for i in range(1, 7):
        if n % 6 == 0:
            return n // 6
        elif (n * i) % 6 == 0:
            person = n * i
            return person // 6     
    