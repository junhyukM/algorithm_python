def solution(numbers):
    answer = 0
    # 평균 : 원소 전체의 합 / 원소 전체의 수
    num_uni = 0
    num_count = 0
    for i in numbers:
        num_uni += i
        num_count += 1
        
    answer = num_uni / num_count    
    
    return answer