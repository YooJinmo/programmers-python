def solution(order):
    count = 0
    game = ["3", "6", "9"]
    for num in str(order):
        if num in game:
            count += 1
    return count