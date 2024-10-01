def solution(numbers, k):
    answer = 0

    num_len = len(numbers) + 2 * (k - 1)
    temp = num_len % len(numbers)
    answer = numbers[temp]
    return answer