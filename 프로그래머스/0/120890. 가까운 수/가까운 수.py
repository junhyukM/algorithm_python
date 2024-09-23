def solution(array, n):
    answer = 0
    array = sorted(array)
    result = 999999999
    
    for a in array:
        if abs(n-a) < result:
            result = abs(n-a)
            answer = a
        
    return answer