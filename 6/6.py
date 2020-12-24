import sys


def parse(puzzle):
    questions = []
    for line in puzzle:
        if line.split():
            questions.append(line.strip("\n"))
        else:
            yield questions
            questions = []


def solution1(puzzleinput):
    count = 0
    for res in puzzleinput:
        count = count + len(set(''.join(res)))

    # must be some stupid comprehension for this
    print(count)


def solution2(puzzleinput):
    count = 0
    for res in puzzleinput:
        count = count + len(''.join(set(res[0]).intersection(*res)))

    print(count)


answers = list(parse(sys.stdin))
solution1(answers)
solution2(answers)
