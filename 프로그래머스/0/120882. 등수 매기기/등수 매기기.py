def solution(score):
    answer = []
    temp = []
    for i in score:
        temp.append(sum(i))
    
    rank_list = sorted(temp, reverse=True)
    
    for i in temp: 
        answer.append(rank_list.index(i)+1)
        
    return answer