def solution(n):
    total = 0
    if n % 2 != 0:
        for i in range(1, n+1, 2):
            total += i
    else:
        for i in range(2, n+1, 2):
            total += i ** 2
    return total