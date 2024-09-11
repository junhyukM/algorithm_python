def solution(money):
    answer = []
    ice_a = money // 5500
    chan = money % 5500
    answer = [ice_a, chan]
    return answer