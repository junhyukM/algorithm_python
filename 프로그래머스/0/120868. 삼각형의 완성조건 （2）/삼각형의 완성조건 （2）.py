def solution(sides):
    answer = sum(sides) - max(sides) + min(sides) - 1
    
    return answer