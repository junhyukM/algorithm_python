def solution(id_pw, db):
    answer = ''
    temp = []
    for i in db:
        temp.append(i[0])
        
    if id_pw in db:
        answer = 'login'
    elif id_pw[0] in temp:
        answer = 'wrong pw'
    else:
        answer = 'fail'
            
    return answer