def solution(array):
    answer = 0
    word = ''.join(str(e) for e in array)
    for i in word:
        if int(i) == 7:
            answer += 1
    return answer