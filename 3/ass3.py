from puzzleInput import puzzle_input


def solution1():
    result = [0, 0]
    index = 3
    for i, row in enumerate(puzzle_input):
        if i == 0:
            continue

        if row[index % len(row)] == '#':
            result[0] = result[0] + 1
        else:
            result[1] = result[1] + 1

        index = index + 3

    print("Solution 1:")
    print("There were %d trees and %d empty spots." % (result[0], result[1]))


def solution2():
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2],
    ]

    results = []

    for slope in slopes:
        index = slope[0]
        result = [0, 0]
        to_collision = slope[1]

        for i, row in enumerate(puzzle_input):
            if to_collision != 0:
                to_collision = to_collision - 1
                continue

            if to_collision == 0:
                if row[index % len(row)] == '#':
                    result[0] = result[0] + 1
                else:
                    result[1] = result[1] + 1

                index = index + slope[0]
                to_collision = slope[1]
                to_collision = to_collision - 1

        results.append(result)

    print("Solution 2:")
    answer = 0
    for result in results:
        if answer == 0:
            answer = result[0]
        else:
            answer = answer * result[0]
        print("There were %d trees and %d empty spots." %
              (result[0], result[1]))

    print("Multiplying all trees nets: %s" % (answer))


solution1()
solution2()
