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
    for num in (mul_data):
        for n in num:
            numbers = re.findall(r'\d+', n) 
            total += (int(numbers[0]) * int(numbers[1]))
        
    return total


print(f"Total uncorrupted multiplication: {solution1()}")