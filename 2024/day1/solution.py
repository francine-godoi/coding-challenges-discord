def solution1():
    with open("input.txt", "r") as file:
        data = file.readlines()

    left = []
    right = []
    for line in data:
        l, r = line.split("  ")
        left.append(l)
        right.append(r)

    left.sort()
    right.sort()

    distance = 0

    for l, r in zip(left, right):
        distance += abs(int(l) - int(r))

    print(distance)

