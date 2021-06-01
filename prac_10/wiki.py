import wikipedia


def main():
    search = input("Please enter the page title or search phrase:")
    while search != "":
        get_result(search)
        search = input("Please enter the page title or search phrase:")


def get_result(search):
    page = wikipedia.page(search)
    if str(page.title).lower() == search.lower():
        print(page.title)
        print(page.summary)
        print(page.url)
    else:
        print(f"Cannot find this page but found page for {page.title}")
        print(page.title)
        print(page.summary)
        print(page.url)


if __name__ == '__main__':
    main()