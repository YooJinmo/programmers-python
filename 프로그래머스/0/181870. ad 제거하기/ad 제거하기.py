def solution(strArr):
    result = []
    for char in strArr:
        if "ad" not in char:
            result.append(char)
    return result