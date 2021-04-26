from prac_06.programming_language import ProgrammingLanguage
from operator import attrgetter
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(ruby, python, visual_basic, sep="\n")
languages = [ruby, python, visual_basic]
print("The dynamically typed languages are:")
for each in languages:
    if ProgrammingLanguage.is_dynamic(each):
        print(each.field)