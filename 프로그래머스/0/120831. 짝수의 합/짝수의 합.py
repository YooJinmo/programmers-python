def solution(n):
    if 0 < n <= 1000:
        total = 0
        for i in range(1, n+1):
            if i % 2 == 0:
                total += i
    return total