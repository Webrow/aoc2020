import sys

translation = str.maketrans('FBLR', '0101')


def parse(puzzle):
    spots = []
    for line in puzzle:
        spots.append(int(line.translate(translation), 2))

    return spots


spots = parse(sys.stdin)


def solution1(spotlist):
    low, high = min(spotlist), max(spotlist)
    print("Highest seatID found: %d" % high)


def solution2(spotlist):
    low, high = min(spotlist), max(spotlist)
    myseat = sum(range(low, high + 1)) - sum(spotlist)
    print("My seatnumber is: %d" % myseat)


solution1(spots)
solution2(spots)
