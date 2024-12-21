def solution(number: int) -> bool:

    divisors = 0
    for num in range(1, number+1):        
        if number % num == 0:
            divisors += 1
        if divisors > 3:
            break        
    return True if divisors == 3 else False

print(solution(25))