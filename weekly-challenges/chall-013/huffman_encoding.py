def solution(text: str) -> str:
    word_counter = {}
    # key is the word, value is the frequency
    for word in text.split():        
        word_counter[word] = text.count(word)
    
    # get the most frequent word at the beggining of the dict
    sorted_word_counter = {key: value for key, value in sorted(word_counter.items(), key=lambda item: item[1], reverse=True)}

    encoded_text = text
    frequency = 1

    # replace the word with the equivalent frequency
    for word in sorted_word_counter.keys():
        encoded_text = encoded_text.replace(word, str(frequency))
        frequency += 1

    return encoded_text


text = 'hi hi bye hi cya bye'
print(text)
print(solution(text))