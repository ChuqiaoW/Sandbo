import random


def print_line():
    line = []
    while len(line) != 6:
        random_number = random.randint(1, 45)
        if random_number not in line:
            line.append(random_number)
    line = sorted(line)
    for each in line:
        print("{:>2d}".format(each), end=" ")


def main():
    time = int(input("How many quick picks?"))
    turn = 0
    while turn != time:
        print_line()
        print("\n")
        turn += 1


main()