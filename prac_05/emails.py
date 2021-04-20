NAME_DICT = {}
email = input("Email:").split("@")
while email != [""]:
    name_unconfirmed = ' '.join((str(email[0]).title()).split("."))
    confirm = str(input(f"Is your name {name_unconfirmed}? (Y/n)")).lower()
    if confirm == "no" or confirm == "n":
        confirmed_name = input("Name:")
        NAME_DICT[confirmed_name] = '@'.join(email)
    elif confirm == "" or confirm == "y":
        NAME_DICT[name_unconfirmed] = '@'.join(email)
    email = input("Email:").split("@")
for key, value in NAME_DICT.items():
    print(f"{key} ({value})")
