def solution(num, k):
    answer = 0
    str_num = str(num)
    str_k = str(k)
    
    for idx, w in enumerate(str_num):
 
        if w == str_k:
            answer = idx + 1
            return answer    
    if answer == 0:
        return -1
         