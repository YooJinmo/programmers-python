def solution(n, k):
    total = 0
    if n // 10 >= 1:
        total = n * 12000 + k * 2000 - n // 10 * 2000
    else:
        total = n * 12000 + k * 2000
    return total