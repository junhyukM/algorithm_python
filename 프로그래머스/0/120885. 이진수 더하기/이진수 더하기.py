def solution(bin1, bin2):
    answer = ''
    # 두 이진수를 십진수로 변환
    # 십진수인 두 수를 더하고
    # 그 십진수를 이진수로 변환
    num1 = str('0b' + bin1)
    num2 = str('0b' + bin2)
    
    int1 = int(num1, 2)
    int2 = int(num2, 2)
    
    total = int1 + int2
    
    answer = format(total, 'b')
    
    return answer