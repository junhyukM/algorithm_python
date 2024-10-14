def solution(keyinput, board):
    answer = [0,0]
    left_right = board[0]
    up_down = board[1]

    for i in keyinput:        
        if i == 'left':
            if answer[0] > -1 * (left_right // 2):
                answer[0] -= 1  
        elif i == 'right':
            if answer[0] < left_right // 2:
                answer[0] += 1
        elif i == 'up':
            if answer[1] < up_down // 2:
                answer[1] += 1 
        elif i == 'down':
            if answer[1] > -1 * (up_down // 2):
                answer[1] -= 1


        
    return answer