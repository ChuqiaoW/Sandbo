COLORS = {"aliceblue": "#f0f8ff", "antiquewhite": "	#faebd7", "brown": "#a52a2a", "burlywood": "#deb887",
          "cadetblue": "#5f9ea0", "coral": "#ff7f50", "chocolate": "#d2691e", "cornflowerblue": "#6495ed",
          "darkgoldenrod": "#b8860b", "darkorange": "#ff8c00"}
color_chose = input("Pls enter color name:")
while color_chose!= "":
    while color_chose.lower() not in COLORS:
        print("Invalid colour name.")
        color_chose = input("Pls enter color name:")
    print(COLORS[color_chose])
    color_chose = input("Pls enter color name:")
