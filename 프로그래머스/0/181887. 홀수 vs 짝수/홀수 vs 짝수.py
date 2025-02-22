def solution(num_list):
    even = 0
    odd = 0
    for i in num_list[::2]:
        even += i
    for i in num_list[1::2]:
        odd += i
    if even > odd:
        return even
    elif even <= odd:
        return odd