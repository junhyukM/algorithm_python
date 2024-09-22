def solution(emergency):
    answer = []
    emergency_dict = {}
    for idx, n in enumerate(emergency):
        emergency_dict[n] = idx
        
    temp2 = list(emergency_dict.values())
    temp = list(emergency_dict.keys())
    
    temp.sort(reverse=True)
    
    num = 1
    for i in temp:
       
        emergency_dict[i] = num
        num += 1
        
    answer = list(emergency_dict.values())
    return answer
