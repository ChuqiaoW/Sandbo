from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    print("Let's drive!")
    menu_choose = input("q)uit, c)hoose taxi, d)rive\n>>>").lower()
    car1 = Taxi("Prius", 100)
    car2 = SilverServiceTaxi("Limo", 100, 2)
    car3 = SilverServiceTaxi("Hummer", 200, 4)
    cars = [car1, car2, car3]
    car_choose = ""
    bill_to_date = 0
    while menu_choose != "q":
        if menu_choose == "c":
            car_choose = choose_taxi(cars)
        elif menu_choose == "d":
            bill_to_date = drive_taxi(cars, car_choose, bill_to_date)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        menu_choose = input("q)uit, c)hoose taxi, d)rive\n>>>").lower()
    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    for i, each in enumerate(cars):
        print(f"{i} - {each.__str__()}")


def choose_taxi(cars):
    index_list = []
    print("Taxis available:")
    for i, each in enumerate(cars):
        index_list.append(i)
        print(f"{i} - {each.__str__()}")
    car_choose = input("Choose taxi: ")
    try:
        car_choose = int(car_choose)
        if car_choose in index_list:
            car_choose = car_choose
        else:
            print("Invalid taxi choice")
            car_choose = ""
    except:
        print("Invalid taxi choice")
        car_choose = ""
    return car_choose


def drive_taxi(cars, car_choose, bill_to_date):
    if car_choose == "":
        print("You need to choose a taxi before you can drive")
        bill_to_date = 0
    else:
        cars[car_choose].start_fare()
        distance = int(input("Drive how far?"))
        cars[car_choose].drive(distance)
        print(f"Your {cars[car_choose].name} trip cost you ${cars[car_choose].get_fare():.2f}")
        bill_to_date += cars[car_choose].get_fare()
    return bill_to_date


if __name__ == '__main__':
    main()
