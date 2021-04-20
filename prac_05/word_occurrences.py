text = input("Text: ").split()
dictionary = {}
for each in text:
    if each not in dictionary:
        dictionary[each] = 1
    else:
        dictionary[each] += 1
length = max(len(x) for x in dictionary)
for key, value in dictionary.items():
    print(f"{key:<{length}} : {value}")