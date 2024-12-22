def solution(square: list) -> bool:

    if not soma(square):
        return False
    
    inverted_square = switch_row_col(square) # switch columns with rows
    if not soma(inverted_square):
        return False
    
    # make a new list with the diagonal values
    diagonal_values = []    
    plus, minus = [-1,len(square)] # start position out of bounds      
    for row in square:            
        plus += 1
        minus -= 1
        diagonal_values.append([square[plus][plus], square[plus][minus]]) # plus row plus col = go down to the right, plus row minus col = go down to the left  
        
    # values grouped by row values: 1st value of row 0 and last value of row 0
    # we want to sum the 1st value of row 0, 2nd value of row 1, ..., last value of last row
    # so we switch the rows with the columns of the diagonal_values list before getting the sum
    return soma(switch_row_col(diagonal_values)) 


def soma(square):
    total = 0
    for row in square:
        if not total:
            total = sum(row) # get total of first row as base value to check the magic square
        elif total != sum(row):            
            return False
    return True

def switch_row_col(square):
    return list(zip(*square))


input = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(solution(input))