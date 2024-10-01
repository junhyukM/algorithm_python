def solution(balls, share):
    answer = 0
    
    balls_result = 1
    for val in range(1, balls + 1):  # 1 ~ n 까지
        balls_result *= val
    
    share_result = 1
    for val in range(1, share + 1):  # 1 ~ n 까지
        share_result *= val
    
    sub = balls - share
    
    sub_result = 1
    for val in range(1, sub + 1):  # 1 ~ n 까지
        sub_result *= val
    
    
    answer = balls_result / (sub_result * share_result)
    
    return answer