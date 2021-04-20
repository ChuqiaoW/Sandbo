text = input("Text: ").split()
dictionary = {}
for each in text:
    if each not in dictionary:
        dictionary[each] = 1
    else:
        dictionary[each] += 1
for key, value in sorted(dictionary.items()):
    print(f"{key}: {value}")