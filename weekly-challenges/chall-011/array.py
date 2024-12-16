def solution(inputArray: list) -> int:

    moves = 0
    last_num = inputArray[0]
    for i, num in enumerate(inputArray):
        if i > 0:
            if num > last_num:
                last_num = num
            elif num <= last_num:
                moves += last_num - num + 1            
                last_num = num + (last_num - num + 1)

    return moves

                           
inputArray = [-1000, 0, -2, 0]
print(solution(inputArray))