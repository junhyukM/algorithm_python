def solution(n):
    answer = 0
    for num in range(1, n + 1):
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count > 2:
            answer += 1
    return answer