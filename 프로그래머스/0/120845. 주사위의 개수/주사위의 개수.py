def solution(box, n):
    answer = 0
    box_0 = box[0]
    box_1 = box[1]
    box_2 = box[2]
    answer = (box_0 // n) * (box_1 // n) * (box_2 // n)
    
    return answer