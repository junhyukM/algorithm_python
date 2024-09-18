def solution(numbers, direction):
    answer = []
    if direction == 'right':
        pop_num1 = numbers[-1]
        numbers.remove(pop_num1)
        numbers.insert(0, pop_num1)
    elif direction == 'left':
        pop_num2 = numbers[0]
        numbers.remove(pop_num2)
        numbers.append(pop_num2)
    answer = numbers    
    return answer