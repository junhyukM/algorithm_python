def solution(arr):
    answer = 1
    list1 = []
    for i in range(len(arr)):
        list1.append(i)
    list2 = list1[::-1]
    
    for i in list1:
        for j in list2:
            if arr[i][j] == arr[j][i]:
                continue
            else:
                answer = 0
                break
                    
    return answer