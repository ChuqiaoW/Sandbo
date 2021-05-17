import os
import shutil


def main():
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        try:
            os.mkdir(extension)
        except:
            pass
        print("{}/{}".format(extension, filename))
        shutil.move(filename, '{}/'.format(extension) + filename)


main()