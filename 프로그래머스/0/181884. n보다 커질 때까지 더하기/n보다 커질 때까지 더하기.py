def solution(numbers, n):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
        if total > n:
            return total
    return total