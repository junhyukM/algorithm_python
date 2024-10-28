def solution(num_list, n):
    answer = []
    answer = num_list[n:n+1] + num_list[n+1:] + num_list[:n]
    return answer