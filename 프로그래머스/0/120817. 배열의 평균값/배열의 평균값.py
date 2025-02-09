def solution(numbers):
    total = 0
    avg = 0
    for i in range(len(numbers)):
        total += numbers[i]
    avg = total / len(numbers)
    
    return avg