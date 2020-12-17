from puzzleInput import puzzle_input
import re


def solution1():
    valid = 0
    passport = {}
    keys = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
    ]

    for entry in puzzle_input:
        all_entries = True
        if entry == '':
            for key in keys:
                if key not in passport.keys():
                    all_entries = False
                    break

            valid = valid + 1 if all_entries else valid + 0

            passport = {}
        else:
            fields = entry.split(' ')
            for field in fields:
                key, value = field.split(':')
                passport[key] = value

    print("Solution 1:")
    print("There were %d valid passports." % (valid))


def validator(passport):
    print(passport)
    for key, value in passport.items():
        if key == 'byr':
            if not (value.isdigit() and (1920 <= int(value) <= 2002)):
                print("BIRTHDATE FAIL")
                return False

        if key == 'iyr':
            if not (value.isdigit() and (2010 <= int(value) <= 2020)):
                print("ISSUEYEAR FAIL")
                return False

        if key == 'eyr':
            if not (value.isdigit() and (2020 <= int(value) <= 2030)):
                print("EXP YEAR FAIL")
                return False

        if key == 'hgt':
            if value.isdigit():
                print("HEIGHT IS DIGIT")
                return False
            else:
                if value[-2:] == 'in' and not (59 <= int(value[:-2]) <= 76):
                    print("INCH HEIGHT FAIL")
                    return False
                elif value[-2:] == 'cm' and not (150 <= int(value[:-2]) <= 193):
                    print("CM HEIGHT FAIL")
                    return False

        if key == 'hcl':
            if not re.match(r"#[a-f0-9]{6}", value):
                print("HAIRCOLOR FAIL")
                return False

        if key == 'ecl':
            colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if value not in colors:
                print("EYECOLOR FAIL")
                return False

        if key == 'pid':
            if not re.match(r"[0-9]{9}$", value):
                print("PID FAIL")
                return False

    return True


def solution2():
    valid = 0
    passport = {}
    keys = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
    ]

    for entry in puzzle_input:
        all_entries = True
        if entry == '':
            for key in keys:
                if key not in passport.keys():
                    all_entries = False
                    break

            if all_entries:
                if validator(passport):
                    print("VALID")
                    valid += 1

            passport = {}
        else:
            fields = entry.split(' ')
            for field in fields:
                key, value = field.split(':')
                passport[key] = value

    print("Solution 2:")
    print("There were %d valid passports." % (valid))


solution1()
solution2()
