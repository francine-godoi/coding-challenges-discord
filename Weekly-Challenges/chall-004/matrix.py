from matrix_generator import TwoDList

def matrixSum(matrix: list) -> int:
    total = 0
    zero_column = []
    for li, line in enumerate(matrix):        
        for ci, col in enumerate(line):
            if matrix[li][ci] == 0:
                zero_column.append(ci)
            
            if li == 0 or ci not in (zero_column):
                total += col
    
    return(total)

matrix = TwoDList()
for _ in matrix: print(_)

print(f"Result: {matrixSum(matrix)}")