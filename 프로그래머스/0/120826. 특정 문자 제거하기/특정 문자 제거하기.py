def solution(my_string, letter):
    answer = ''
    for w in my_string:
        if w in letter:
            my_string = my_string.replace(w, '')
            
    return my_string