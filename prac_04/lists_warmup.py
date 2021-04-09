numbers = [3, 1, 4, 1, 5, 9, 2]
"""
numbers [0] = 3
numbers [-1] = 2
numbers [3] = 1
numbers [:-1] = [3, 1, 4, 1, 5, 9]
numbers [3:4] = [1]
5 in numbers is True
7 in numbers is False
"3" in numbers is False
numbers + [6,5,3] is [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
I checked and I'm right
"""
numbers[0] = "ten"
numbers[-1] = 1
print(numbers)
elements = numbers[2:]
print(elements)
print(9 in numbers)
