def solution(days: int) -> list:

    MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    options = []
    index = [i for i, _ in enumerate(MONTHS) if _ == days]
    for i in index:
        if i + 1 == len(MONTHS):
            i = -1
        options.append(MONTHS[i+1])

    return list(set(sorted(options)))

print(solution(31))