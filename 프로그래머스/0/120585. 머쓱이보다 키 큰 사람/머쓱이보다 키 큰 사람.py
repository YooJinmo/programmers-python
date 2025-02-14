def solution(array, height):
    total = 0
    for i in range(len(array)):
        if height < array[i]:
            total += 1
    return total