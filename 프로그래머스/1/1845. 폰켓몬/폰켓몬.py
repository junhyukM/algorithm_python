def solution(nums):
    answer = 0
    nums_list = []
    for i in nums:
        if i in nums_list:
            continue
        else:
            nums_list.append(i)
    if len(nums_list) <= len(nums)/2:
        answer = len(nums_list)
    else:
        answer = len(nums)/2
    return answer