def solution(num_list):
    answer = []
    num_list.sort(reverse=False)
    answer = num_list[5:]
    return answer