def solution(arr, idx):
    answer = 0
    for index, i in enumerate(arr):
        if index > idx-1 and i == 1:
            answer = index
            break
        elif index > idx-1 and index == (len(arr) - 1):
            answer = -1
    return answer