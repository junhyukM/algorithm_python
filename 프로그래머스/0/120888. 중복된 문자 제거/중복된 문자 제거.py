def solution(my_string):
    answer = ''
    my_list = list(map(str, my_string))
    my_list2 = []
    print(my_list)
    for i in my_list:
        if i not in my_list2:
            my_list2.append(i)
    answer = ''.join(my_list2)        
            
    return answer