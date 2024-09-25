def solution(s):
    answer = 0
    s = s.split()
    
    num_list = []

    for i in s:
        try :
            if float(i):
                num_list.append(int(i))
        except:
            # 숫자가 아닌 문자가 나온 경우, 이전에 추가한 숫자를 제거합니다.
            if num_list:
                num_list.pop(-1)  # 가장 최근에 추가된 숫자를 제거합니다.
            
    answer = sum(num_list)    

    return answer