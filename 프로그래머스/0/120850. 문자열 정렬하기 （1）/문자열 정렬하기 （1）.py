def solution(my_string):
    result = []
    num_list = "0123456789"

    for char in my_string:
        if char in num_list:
            result.append(int(char))

    result.sort()
    return result
