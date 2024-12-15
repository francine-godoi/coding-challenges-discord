import re

def get_info():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()        
    
    return data

def solution1():
    array = get_info()
    count = 0    
    for row, line in enumerate(array):
        for col, letter in enumerate(line):            
            if letter == "X":     
                # horizontal forward     
                if col + 3 < len(line) and array[row][col+1] == "M" and array[row][col+2] == "A" and array[row][col+3] == "S":
                    count += 1

                # horizontal backwards
                if col - 3 >= 0 and array[row][col-1] == "M" and array[row][col-2] == "A" and array[row][col-3] == "S":
                    count += 1
            
                # diagonal up-left
                if col - 3 >= 0 and row - 3 >= 0 and array[row-1][col-1] == "M" and array[row-2][col-2] == "A" and array[row-3][col-3] == "S":
                    count += 1
            
                # diagonal up-right
                if row - 3 >= 0 and col + 3 < len(line) and array[row-1][col+1] == "M" and array[row-2][col+2] == "A" and array[row-3][col+3] == "S":
                    count += 1
            
                # diagonal down-left
                if row + 3 < len(array) and col - 3 >= 0 and array[row+1][col-1] == "M" and array[row+2][col-2] == "A" and array[row+3][col-3] == "S":
                    count += 1
            
                # diagonal down-right
                if row + 3 < len(array) and col + 3 < len(line) and array[row+1][col+1] == "M" and array[row+2][col+2] == "A" and array[row+3][col+3] == "S":
                    count += 1
            
                # vertical upwards
                if row - 3 >= 0 and array[row-1][col] == "M" and array[row-2][col] == "A" and array[row-3][col] == "S":
                    count += 1
            
                # vertical downwards
                if row + 3 < len(array) and array[row+1][col] == "M" and array[row+2][col] == "A" and array[row+3][col] == "S":
                    count += 1
                
    return count

def solution2():
    array = get_info()
    count = 0    
    for row, line in enumerate(array):
        for col, letter in enumerate(line):            
            if letter == "A":
                if row - 1 >= 0 and col - 1 >= 0 and row + 1 < len(array) and col + 1 < len(line):

                    # M M
                    #  A
                    # S S
                    if (array[row-1][col-1] == "M" and array[row+1][col+1] == "S") and (array[row-1][col+1] == "M" and array[row+1][col-1] == "S"):
                        count += 1
                    
                    # M S
                    #  A
                    # M S
                    if (array[row-1][col-1] == "M" and array[row+1][col+1] == "S") and (array[row-1][col+1] == "S" and array[row+1][col-1] == "M"):
                        count += 1         

                    # S S
                    #  A
                    # M M
                    if (array[row-1][col-1] == "S" and array[row+1][col+1] == "M") and (array[row-1][col+1] == "S" and array[row+1][col-1] == "M"):
                        count += 1

                    # S M
                    #  A
                    # S M
                    if (array[row-1][col-1] == "S" and array[row+1][col+1] == "M") and (array[row-1][col+1] == "M" and array[row+1][col-1] == "S"):
                        count += 1  

    return count


print(f'Resultado: {solution1()}')
print(f'Resultado: {solution2()}')