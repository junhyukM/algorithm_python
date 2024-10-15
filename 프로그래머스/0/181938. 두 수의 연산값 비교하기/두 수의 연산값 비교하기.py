def solution(a, b):
    num2 = 2 * a * b
    a = str(a)
    b = str(b)
    num1 = a + b
    if int(num1) > num2:
        answer = int(num1)
    else:
        answer = num2
    return answer