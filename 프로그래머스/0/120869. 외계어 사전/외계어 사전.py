from itertools import permutations

def solution(spell, dic):
    # spell에 있는 알파벳으로 만들 수 있는 모든 단어 생성
    words = [''.join(permutation) for permutation in permutations(spell)]
    
    # 생성한 단어가 dic에 존재하는지 확인
    for word in words:
        if word in dic:
            return 1
    
    return 2