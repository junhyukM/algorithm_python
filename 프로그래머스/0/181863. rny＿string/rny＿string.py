def solution(rny_string):
    answer = ''
    for i in rny_string:
        append_word = i
        if i == 'm':
            append_word = "rn"
        answer += append_word
    return answer