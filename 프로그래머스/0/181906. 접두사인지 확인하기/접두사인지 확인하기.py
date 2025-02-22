def solution(my_string, is_prefix):
    add = []
    for i in range(len(my_string)):
        add.append(my_string[:i])
    if is_prefix in add:
        return 1
    else: 
        return 0