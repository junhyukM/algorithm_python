def solution(participant, completion):
    dict1 = dict()
    # participant의 여러 값들을 key와 1의 value로 초기화
    for i in participant:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    # complietion에 있다면 값을 -1 해줌
    for i in completion:
        dict1[i] -= 1
    # 단 하나의 key만 값이 0이 아닐 것이므로 그 값을 반환
    for i in dict1.keys():
        if dict1[i] != 0:
            return i