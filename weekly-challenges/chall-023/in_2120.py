def solution(input: int) -> bool:
    """
    Pattern found: all numbers found True have at least one non-zero number after the 1st zero
    """
    num = str(input)
    zero = num.find("0")
    if zero < 0 or zero + 1 == len(num): # if there is no zeros or the 1st zero is in the last position >>False
        return False
    else:
        return num[zero + 1] != "0" 
 

print("Expected Output: True")
print(f"Output: {solution(902200100)}") #True
print("\n")

print("Expected Output: False")
print(f"Output: {solution(11000)}") #False
print("\n")

print("Expected Output: True")
print(f"Output: {solution(99080)}") #True
print("\n")

print("Expected Output: True") 
print(f"Output: {solution(1022220)}") #True
print("\n")

print("Expected Output: True") 
print(f"Output: {solution(106611)}") #True
print("\n")

print("Expected Output: False")
print(f"Output: {solution(234230)}") #False
print("\n")

print("Expected Output: False")
print(f"Output: {solution(888)}") #False
print("\n")

print("Expected Output: False")
print(f"Output: {solution(100)}") #False
print("\n")

print("Expected Output: False")
print(f"Output: {solution(1000000000)}") #False
print("\n")

print("Expected Output: True")
print(f"Output: {solution(103456789)}") #True
print("\n")