def solution(n):
    answer = []
    answer.append(n)
    while n != 1:
        if n % 2 == 0:
            n /= 2
            answer.append(n)
        elif n % 2:
            n = 3 * n + 1
            answer.append(n)
            
    return answer