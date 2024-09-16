def solution(cipher, code):
    answer = ''
    # print(cipher[15])
    for i in range(code - 1, len(cipher), code):
        answer += cipher[i]
        
    return answer