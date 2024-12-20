def compress(input: str) -> str:
    compressed_input = ""
    previous_letter = ""
    count = 1
    for i, letter in enumerate(input):
        if not previous_letter:
            previous_letter = letter
        elif letter == previous_letter:
            count += 1
        elif letter != previous_letter:
            compressed_input += previous_letter + str(count)            
            count = 1
            previous_letter = letter
            
        if i == len(input) - 1:
            compressed_input += previous_letter + str(count)
    
    if len(compressed_input) < len(input):
        return compressed_input
    else:
        return input
    

input = "aaabbbccdaa"
print(compress(input))