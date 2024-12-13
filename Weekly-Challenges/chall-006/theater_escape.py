from seatings_generator import print_matrix

def whichExit(matrix):
    left = right = 0
    for line in matrix:
        if 0 in line:
            me = line.index(0)
            left = sum(1 for i in line[0:me] if i==1)
            right = sum(1 for i in line[me:] if i==1)
            break
    
    if left == right:
        print("same")
    elif left > right:
        print("right")
    else:
        print("left")

matrix = print_matrix(6, 4)

whichExit(matrix)