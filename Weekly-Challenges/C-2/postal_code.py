def validate(code: int) -> bool:
    try:
        int(code)
    except ValueError:
        return False    
    
    if len(code) != 5:
        return False

    for i, digit in enumerate(code):
        index = code[i+1:].find(digit)
        if index == -1:
            continue
        if index < 2:
            return False

    return True

if __name__ == "__main__":
    code = input("Postal Code (5 digits): ")
    print(validate(code))