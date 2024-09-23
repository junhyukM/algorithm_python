def solution(s):
    answer = ''
    list = []
    b_list = []
    total_list = []
    for i in s:
        if i not in list:
            list.append(i)
        else:
            b_list.append(i)
            
    for l in s:
        if l not in b_list:
            total_list.append(l)
            total_list.sort()
    answer = ''.join(total_list)
    return answer