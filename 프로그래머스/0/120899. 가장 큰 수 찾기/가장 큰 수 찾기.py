def solution(array):
    answer = []
    # 리스트에서 가장 큰 값 찾기
    max_value = max(array)
    # 큰 값의 인덱스 찾기
    for idx, i in enumerate(array):
        if i == max_value:
            answer_index = idx
    answer = [max_value, answer_index]
        
    return answer