def solution(arr, k):
    answer = []
    if k % 2:
        for i in arr:
            answer.append(i*k)
    else:
        for j in arr:
            answer.append(j+k)
    return answer