def main():
    numbers = []
    for number in range(1, 6):
        write_in = int(input("Number:"))
        numbers.append(write_in)
    data = analyze_numbers(numbers)
    print(f"The first number is {data[0]}\nThe last number is {data[1]}\nThe smallest number is {data[2]}\n"
          f"The largest number is {data[3]}\nThe average of the numbers is {data[4]}")


def analyze_numbers(numbers):
    data = []
    data.append(numbers[0])
    data.append(numbers[-1])
    data.append(min(numbers))
    data.append(max(numbers))
    data.append(sum(numbers)/len(numbers))
    return data

main()