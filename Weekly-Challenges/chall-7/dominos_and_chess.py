def fill(matrix):

    pos = 0
    foward = True
    for row, line in enumerate(matrix):
        for _ in line:
            if foward:            
                if pos+1 < len(line) and line[pos] == 0 and line[pos+1] == 0:
                    line[pos] = "D"
                    line[pos+1] = "D"
                    pos += 2
                if pos+1 < len(line) and (line[pos] == 1 or line[pos+1] == 1 or line[pos]== "D" or line[pos+1] == "D"):
                    pos +=1
                
                if pos == len(line): pos -= 1 # reset index if out of bound

                if pos == len(line) - 1:
                    if row+1 < len(matrix) and line[pos] == 0 and matrix[row+1][pos] == 0:
                        line[pos] = "D"
                        matrix[row+1][pos] = "D"
                    foward = False   
                    break                                                                    

            if not foward:
                    if pos-1 >= 0 and line[pos] == 0 and line[pos-1] == 0:
                        line[pos] = "D"
                        line[pos-1] = "D"
                        pos -= 2

                    if pos-1 >= 0 and (line[pos] == 1 or line[pos-1] == 1 or line[pos]== "D" or line[pos-1] == "D"):
                        pos -= 1

                    if pos < 0: pos = 0 # reset index if out of bound

                    if pos == 0:
                        if row+1 < len(matrix) and line[pos] == 0 and matrix[row+1][pos] == 0:
                            line[pos] = "D"
                            matrix[row+1][pos] = "D"
                        foward = True
                        break

        if foward: 
            pos = 0
        else: 
            pos = len(line) - 1
    
    zeros = 0
    for line in matrix:
        print(line)
        zeros += sum(1 for l in line if l == 0)  

    return zeros == 0 

matrix = [[1,0,0,0],
          [0,0,0,0],
          [0,0,0,1]]

for line in matrix:
    print(line)
print("\n")

print(fill(matrix))