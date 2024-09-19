def solution(my_string):
    answer = ''
    my_string = my_string.lower()
    my_list = list(map(str, my_string))
    my_list.sort()
    answer = ''.join(my_list)
    return answer