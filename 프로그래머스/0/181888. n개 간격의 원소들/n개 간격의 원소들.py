def solution(num_list, n):
    result = []
    for i in num_list[::n]:
        result.append(i)
    return result