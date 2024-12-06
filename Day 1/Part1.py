def part1(lst1, lst2):
    # sort the first list of location IDs
    lst1.sort()

    # sort the second list of location IDs
    lst2.sort()

    n = len(lst1)

    totalDistance = 0
    for i in range(n):
        distance = abs(lst1[i] - lst2[i])

        # add the distance to the total distance
        totalDistance += distance

    return totalDistance

def main():
    lst1 = []
    lst2 = []

    with open("Day 1\input.txt", "r") as f:
        f = f.readlines()

        for line in f:
            # split the line into two parts
            line = line.split()

            # add the first part to the first list
            lst1.append(int(line[0]))

            # add the second part to the second list
            lst2.append(int(line[1]))

    totalDistance = part1(lst1, lst2)

    print(totalDistance)

if __name__ == "__main__":
    main()