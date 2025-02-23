def solution(cipher, code):
    list1 = list(cipher)
    list1 = list1[code-1::code]
    return "".join(list1)