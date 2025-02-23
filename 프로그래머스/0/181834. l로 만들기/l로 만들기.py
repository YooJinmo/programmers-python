def solution(myString):
    alp = "abcdefghijk"
    result = []

    for char in myString: 
        if char in alp:
            result.append("l") 
        else:
            result.append(char) 

    return "".join(result)