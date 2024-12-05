import re

def get_info():
    with open("input_test.txt", "r") as file:
        data = file.read().splitlines()        
    
    return data

def solution1():
    array = get_info()

    count_h = 0
    for line in array: #find horizontal matches       
        count_h += find_xmas(line)

    count_v = 0
    inverted_array = list(zip(*array)) #swapped row and columns to verify vertical matches
    for line in inverted_array: #find vertical matches
        count_v += find_xmas("".join(line))

    count_d = 0

    for l, line in enumerate(array): # find diagonal matches
        line = line.strip()
        index = [x.start() for x in re.finditer("X", line)] #find all instances of X to iniciate matches
        diagonal = []

        for i in index:         

            if l > 2 and i > 2:  #diagonal up-left
                diagonal.append([array[l-1][i-1], array[l-2][i-2], array[l-3][i-3]])  

            if l > 2 and i < len(line) - 3: #diagonal up-right
                diagonal.append([array[l-1][i+1], array[l-2][i+2], array[l-3][i+3]])                 
                
            if l < len(array) - 3 and i > 2: #diagonal down-left
                diagonal.append([array[l+1][i-1], array[l+2][i-2], array[l+3][i-3]])                      

            if l < len(array) - 3 and i < len(line) - 3: #diagonal down-right
                diagonal.append([array[l+1][i+1], array[l+2][i+2], array[l+3][i+3]])  

        for dia in diagonal:
            is_match = "".join(dia)
            if is_match == "MAS":
                count_d +=1                         

    print(f"h {count_h} v {count_v} d {count_d}")
    total = count_h + count_v + count_d
    return total


def find_xmas(line):
    count = 0
    if re.findall(r"XMAS", line):
        count += 1

    if re.findall(r"SAMX",line):
        count += 1

    return count


def solution2():
    pass


print(f'Resultado: {solution1()}')
print(f'Resultado: {solution2()}')