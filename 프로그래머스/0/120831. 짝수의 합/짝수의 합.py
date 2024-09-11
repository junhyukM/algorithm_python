def solution(n):
    answer = 0
    # 짝수 리스트 생성
    num = list(range(2,n + 1,2))
    for i in num:
        answer += i
        
    return answer