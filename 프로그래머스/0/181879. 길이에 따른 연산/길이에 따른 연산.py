def solution(num_list):
    total = 1
    if len(num_list) >= 11:
        total = sum(num_list)
    else:
        for i in range(len(num_list)):
            total = total * num_list[i]
    return total