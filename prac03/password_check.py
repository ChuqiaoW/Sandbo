def main():
    password = input("pls input your password:")
    get_password(password)


def get_password(password):
    print("*" * len(password))


main()