import os


def main():
    type_of_extensions = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        if extension not in type_of_extensions:
            category = input("What category would you like to sort {} files into? ".format(extension))
            type_of_extensions[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
        os.rename(filename, "{}/{}".format(type_of_extensions[extension], filename))


main()
