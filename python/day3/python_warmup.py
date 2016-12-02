# references document day3Warmup.txt

candy_bars = ["snickers", "twix-left", "twix-right"]

print(candy_bars)

candy_bars.insert(3, "milkyway")
candy_bars.insert(4, "twix")

print(candy_bars)

# if statement to make sure I entered my list in correctly *snickers being the first element

if candy_bars[4] == "twix" and candy_bars[0] == "snickers":
        # this references the first and argument in the .format by index number
    print("{0} was the last and {1} is the first in the list.".format(candy_bars[4],candy_bars[0]))
