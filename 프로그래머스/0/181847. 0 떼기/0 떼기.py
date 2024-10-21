def solution(n_str):
    answer = ''
    for idx, i in enumerate(n_str):
        print(i)
        if i == '0':
            continue
        else:
            answer = n_str[idx:]
            break
    return answer