def get_info():
    with open("input.txt", "r") as file:
        data = file.readlines()

    left = []
    right = []
    for line in data:
        l, r = line.strip().split("   ")
        left.append(l)
        right.append(r)

    left.sort()
    right.sort()

    return left, right

def solution1():
    left, right = get_info()
    distance = 0

    for l, r in zip(left, right):
        distance += abs(int(l) - int(r))

    print(f"Distance: {distance}")

def solution2():
    left, right = get_info()
    similarity = 0

    for l in left:
        similarity += int(l) * right.count(l)

    print(f"Similarity: {similarity}")

solution1()
solution2()