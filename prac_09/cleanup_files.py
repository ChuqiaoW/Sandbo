import shutil
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    # TODO: Use exception handling to avoid the crash (just pass)
    try:
        os.mkdir('temp')
    except:
        pass
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))
        os.rename(filename, new_name)
        shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    pos = [i for i, e in enumerate(filename) if e.isupper() and filename[i-1].islower()]
    parts = []
    for j in range(len(pos)):
        try:
            parts.append(filename[pos[j]:pos[j + 1]])
        except IndexError:
            parts.append(filename[pos[j]:])
    filename = " ".join(parts)
    filename = filename.title()
    filename = filename.split(".")
    filename[1] = filename[1].lower()
    new_name = ".".join(filename)
    new_name.replace(" ", "_")
    return new_name


def demo_walk():
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        for filename in filenames:
            print(os.path.join(directory_name, filename))
            new_name = get_fixed_filename(filename)
            os.rename(os.path.join(directory_name, filename), os.path.join(directory_name, new_name))


main()
print(get_fixed_filename("ItIsWell (oh my soul).txt"))