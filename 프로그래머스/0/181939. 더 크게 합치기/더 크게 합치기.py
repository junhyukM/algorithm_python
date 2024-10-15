def solution(a, b):
    a = str(a)
    b = str(b)
    
    num1 = a + b
    num2 = b + a
    
    if int(num1) > int(num2):
        answer = int(num1)
    else:
        answer = int(num2)
    
    return answer