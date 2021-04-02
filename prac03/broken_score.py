import random


def main():
    try:
        score = float(input("Enter score: "))
        result = define_result(score)
        print(result)
    except:
        random_score = random.randint(0, 100)
        print("The random score is: ", random_score, ", which is ", define_result(random_score))


def define_result(score):
    if 90 <= score <= 100:
        result = "Excellent"
    elif 50 <= score < 90:
        result = "Passable"
    elif 0 <= score < 50:
        result = "Bad"
    else:
        result = "Invalid score"
    return result


main()