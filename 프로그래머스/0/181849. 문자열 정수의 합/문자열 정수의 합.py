def solution(num_str):
    result = []
    total = 0
    
    for i in num_str:
        result.append(i)
        
    for j in range(len(result)):
        total += int(result[j])
    
    return total
