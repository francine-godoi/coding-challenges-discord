def solution(matrix):
    bombs = 0
    for row, line in enumerate(matrix):
        for col, elem in enumerate(line):
            if elem == 0:
                # diagonal up left
                if row - 1 >= 0 and col - 1 >= 0 and matrix[row-1][col-1] == 'x':
                    bombs += 1

                # diagonal up right
                if row - 1 >= 0 and col + 1 < len(line) and matrix[row-1][col+1] == 'x':
                    bombs += 1

                # diagonal down left
                if row + 1 < len(matrix) and col - 1 >= 0 and matrix[row+1][col-1] == 'x':
                    bombs += 1                

                # diagonal down right
                if row + 1 < len(matrix) and col + 1 < len(line) and matrix[row+1][col+1] == 'x':
                    bombs += 1   

                # vertical down
                if row + 1 < len(matrix) and matrix[row+1][col] == 'x':
                    bombs += 1    

                # vertical up      
                if row - 1 >= 0 and matrix[row-1][col] == 'x':
                    bombs += 1                                  

                # horizontal right      
                if col + 1 < len(line) and matrix[row][col+1] == 'x':
                    bombs += 1    

                # horizontal left      
                if col - 1 >= 0 and matrix[row][col-1] == 'x':
                    bombs += 1   

                matrix[row][col] = bombs
                bombs = 0

    return matrix

matrix = [[ 0 , 0 , 0 ,'x', 0 ],
          ['x', 0 , 0 ,'x', 0 ],
          [ 0 , 'x' , 0 , 0 , 0 ]]

new_matrix = solution(matrix)
for _ in new_matrix: print(_)