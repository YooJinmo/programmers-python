def solution(arr):
    result = []
    for j in range(len(arr)):
        list_num = arr[j]
        for i in range(list_num):
            result.append(list_num)
    return result