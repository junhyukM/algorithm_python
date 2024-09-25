def solution(n):
    answer = []
    temp = []
    i = 2
    while i <= n:
        if n % i == 0:
            temp.append(i)
            n = n / i
        else:
            i = i + 1
    
    
    for i in temp:
        if i not in answer:
            answer.append(i)
    
        
    return answer