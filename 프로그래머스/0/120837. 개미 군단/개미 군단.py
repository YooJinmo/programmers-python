def solution(hp):
    hp5 = hp // 5
    hp %= 5 
    hp3 = hp // 3  
    hp %= 3  
    hp1 = hp  
    return hp5 + hp3 + hp1
