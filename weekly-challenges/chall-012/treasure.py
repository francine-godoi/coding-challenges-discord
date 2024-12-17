def solution(value1: int, weight1: int, value2: int, weight2: int, maxW: int) -> int:
    
    if weight1 + weight2 <= maxW:
        return value1 + value2
    elif value1 > value2 and weight1 <= maxW:
        return value1
    elif value2 > value1 and weight2 <= maxW:
        return value2
    elif weight1 <= maxW:
        return value1
    elif weight2 <= maxW:
        return value2
    else:
        return 0
        

print(solution(value1 = 1, weight1 = 5, value2 = 6, weight2 = 15, maxW = 9))