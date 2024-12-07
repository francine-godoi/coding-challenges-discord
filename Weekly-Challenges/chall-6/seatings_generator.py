import random

def print_matrix(col=5,row=3):
    matrix = []
    for r in range(row):
        matrix.append([])
        for c in range(col):
            matrix[r].append(random.choice([1,-1]))
    boy = (random.randint(0,col-1),random.randint(0,row-1))
    matrix[boy[1]][boy[0]] = 0
    for _ in matrix: print(_)
    
    return matrix    
