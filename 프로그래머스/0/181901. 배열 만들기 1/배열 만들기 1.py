def solution(n, k):
    result = []
    for i in range(1, n // k + 1):
        new = k * i
        if new <= n:
            result.append(new)
    return result