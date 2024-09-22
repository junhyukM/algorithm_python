def solution(n):
    answer = []
    result = []
    for i in range(1,11):
        facto = 1
        for j in range(1,i+1):
            facto *= j
        result.append(facto)    
    
    for f in result:
        if f <= n:
            answer.append(f)
       

    return len(answer)