def solution(before, after):
    answer = 0
    word_b = list(map(str, before))
    word_a = list(map(str, after))
    
    if sorted(word_b) == sorted(word_a):
        answer = 1
    
    
        
    return answer