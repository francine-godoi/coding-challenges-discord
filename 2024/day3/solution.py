import re

def get_info():
    with open("input.txt", "r") as file:
        data = file.readlines()
   
    return data

def solution1():

    txt = get_info()
    mul_data = []

    for line in txt:
        mul = re.findall(r"mul[(]\d{1,3},\d{1,3}[)]", line)
        mul_data.append(mul)

    total = 0
    for num in mul_data:
        for n in num:
            num1, num2 = re.findall(r'\d+', n) 
            total += int(num1)* int(num2)
        
    return total

def solution2():
    txt = get_info()
    mul_data = []

    for line in txt:
        mul = re.compile(r"mul[(]\d{1,3},\d{1,3}[)] | do[(][)] | don't[(][)]", flags=re.I | re.X)        
        mul_data.append(mul.findall(line))

    total = 0
    enable = True
    for num in mul_data:
        for n in num:
            if n[:n.find("(")] == "do":
                enable = True
                continue
            elif n[:n.find("(")] == "don't":
                enable = False                
            
            if enable:
                num1, num2 = re.findall(r'\d+', n)
                total += int(num1)* int(num2)
        
    return total


print(f"Total uncorrupted multiplication: {solution1()}")
print(f'Enabled multiplications: {solution2()}')