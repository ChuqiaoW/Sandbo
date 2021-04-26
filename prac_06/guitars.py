from prac_06.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    done = "False"
    while done != "True":
        name = input("Name:")
        year = input("Year:")
        cost = input("Cost:$")
        guitars.append(Guitar(name, year, cost))
        print("{} ({}) :$ {:,.2f} added.".format(name, year, float(cost)))
        done = input("")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, float(guitar.cost),
                                                                  " (vintage)" if 2021-int(guitar.year) > 50 else ""))


main()
