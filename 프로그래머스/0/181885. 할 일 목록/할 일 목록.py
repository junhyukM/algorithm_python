def solution(todo_list, finished):
    answer = []
    for idx, i in enumerate(finished):
        if i:
            pass
        else:
            answer.append(todo_list[idx])
    return answer