def solution(i, j, k):
    answer = 0
    # i : 시작숫자
    # j : 끝 숫자
    # k : 등장 횟수를 세어야 하는 숫자
    
    
    numbers = ''.join(([str(num) for num in range(i,j+1)]))
    numbers_list = list(map(str, numbers))
    for n in numbers_list:       
        if str(k) == n:
            answer += 1
    return answer