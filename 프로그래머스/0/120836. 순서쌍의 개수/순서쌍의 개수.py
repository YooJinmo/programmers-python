def solution(n):
    total = 0
    i = 1

    while i * i <= n:  # i를 1부터 sqrt(n)까지만 탐색
        if n % i == 0:  # i가 n의 약수라면
            total += 1  # (i, n // i) 중 첫 번째 요소 추가
            if i != n // i:
                total += 1  # 서로 다른 두 숫자이면 (중복 방지)
        i += 1

    return total
