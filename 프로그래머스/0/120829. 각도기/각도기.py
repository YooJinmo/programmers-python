def solution(angle):
    result = 0
    if 0 < angle <= 180:
        if 0 < angle < 90: result = 1
        elif angle == 90: result = 2
        elif 90 < angle < 180: result = 3
        else: result = 4
        
    return result