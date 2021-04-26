from prac_06.guitar import Guitar
guitar1 = Guitar("Gibson L-5 CES", 1922, 16035)
guitar2 = Guitar("Another Guitar", 2013, 16035)
guitar3 = Guitar("50-year old guitar", 1971, 16035)
print(f"Gibson L-5 CES get_age() - Expected 99. Got{guitar1.get_age()}")
print(f"Another Guitar get_age() - Expected 8. Got{guitar2.get_age()}")
print(f"Gibson L-5 CES is_vintage() - Expected True. Got{guitar1.is_vintage()}")
print(f"Another Guitar is_vintage() - Expected False. Got{guitar2.is_vintage()}")
print(f"50-year old guitar is_vintage() - Expected True. Got{guitar3.is_vintage()}")