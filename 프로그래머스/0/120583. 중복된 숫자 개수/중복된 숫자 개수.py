def solution(array, n):
    total = 0
    for i in range(len(array)):
        if array[i] == n:
            total += 1
    return total