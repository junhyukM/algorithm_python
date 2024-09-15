def solution(sides):
    answer = 0
    max_sides = max(sides)
    sides.remove(max_sides)
    
    if max_sides < (sides[0] + sides[1]):
        answer = 1
    else:
        answer = 2
    
    return answer