def solution(price):
    answer = 0
    # 50만원 이상 20프로
    if price >= 500000:
        answer = price * 0.8
    # 30만원 이상 10프로
    elif price >= 300000:
        answer = price * 0.9
    # 10만원 이상 5프로
    elif price >= 100000:
        answer = price * 0.95    
    else:
        answer = price
        
    return int(answer)