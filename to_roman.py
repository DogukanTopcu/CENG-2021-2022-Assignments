year = int(input("Please give a year..."))

thousand = year // 1000

if (thousand // 5) > 0:
    if thousand < 9:
        x = "V̅"+"M"*(thousand-5)
    if thousand == 9:
        x = "MX̅"
else:
    if thousand == 4:
        x = "MV̅"
    if thousand < 4:
        x = "M"*thousand

year -= thousand * 1000

hundred = year // 100
if (hundred // 5) > 0:
    if hundred < 9:
        y = "D" + "C"*(hundred-5)
    if hundred == 9:
        y = "CM"
else:
    if hundred == 4:
        y = "CD"
    if hundred < 4:
        y = "C"*hundred

year -= hundred * 100

decimal = year // 10
if (decimal // 5) > 0:
    if decimal < 9:
        z = "L" + "X"*(decimal-5)
    if decimal == 9:
        z = "XC"
else:
    if decimal == 4:
        z = "XL"
    if decimal < 4:
        z = "X"*decimal

year -= decimal*10

if (year // 5) > 0:
    if year < 9:
        t = "V" + (year-5)*"I"
    if year == 9:
        t = "IX"
else:
    if year == 4:
        t = "IV"
    if year < 4:
        t = "I"*year


print(x+y+z+t)