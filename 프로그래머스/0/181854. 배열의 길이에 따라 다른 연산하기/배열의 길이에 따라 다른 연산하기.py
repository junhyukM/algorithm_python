def solution(arr, n):
    answer = []
    if len(arr) % 2:
        for idx, i in enumerate(arr):
            if idx % 2:
                answer.append(i)
            else:
                answer.append(i + n)
    else:                
        for idx, i in enumerate(arr):
            if idx % 2:
                answer.append(i + n)
            else:
                answer.append(i)
    return answer