import random

bunco_count = 0
mini_bunco_count = 0
total = 0
bunco = 21
mini_bunco = 5

input("Press Enter for start Round 1 First Dice…")
dice_111 = random.randint(1, 6)
dice_121 = random.randint(1, 6)
dice_131 = random.randint(1, 6)
print("[", dice_111, dice_121, dice_131, "]")
temp11 = total
if (dice_111 == dice_121 == dice_131 == 1):
    print("Bunco!")
    bunco_count += 1
    total += bunco
elif (dice_111 == dice_121 == dice_131 != 1):
    print("Mini-Bunco!")
    mini_bunco_count += 1
    total += mini_bunco
else:
     if (dice_111 == 1) :
          total += 1
          print("+1")
     elif (dice_121 == 1) :
          total += 1
          print("+1")
     elif (dice_131 == 1) :
          total += 1
          print("+1")

if temp11 != total :
    input("Press Enter for start Round 1 Second Dice…")
    dice_112 = random.randint(1, 6)
    dice_122 = random.randint(1, 6)
    dice_132 = random.randint(1, 6)
    print("[", dice_112, dice_122, dice_132, "]")

    temp12 = total
    if (dice_112 == dice_122 == dice_132 == 1):
        print("Bunco!")
        bunco_count += 1
        total += bunco
    elif (dice_112 == dice_122 == dice_132 != 1):
        print("Mini-Bunco!")
        mini_bunco_count += 1
        total += mini_bunco
    else:
        if (dice_112 == 1):
            total += 1
            print("+1")
        elif (dice_122 == 1):
            total += 1
            print("+1")
        elif (dice_132 == 1):
            total += 1
            print("+1")

        if temp12 != total:
            input("Press Enter for start Round 1 Third Dice…")
            dice_113 = random.randint(1, 6)
            dice_123 = random.randint(1, 6)
            dice_133 = random.randint(1, 6)
            print("[", dice_113, dice_123, dice_133, "]")

            if (dice_113 == dice_123 == dice_133 == 1):
                print("Bunco!")
                bunco_count += 1
                total += bunco
            elif (dice_113 == dice_123 == dice_133 != 1):
                print("Mini-Bunco!")
                mini_bunco_count += 1
                total += mini_bunco
            else:
                if (dice_113 == 1):
                    total += 1
                    print("+1")
                elif (dice_123 == 1):
                    total += 1
                    print("+1")
                elif (dice_133 == 1):
                    total += 1
                    print("+1")

print("You have run out of rights for first round...")

input("Press Enter for start Round 2 First Dice…")

dice_211 = random.randint(1, 6)
dice_221 = random.randint(1, 6)
dice_231 = random.randint(1, 6)
print("[", dice_211, dice_221, dice_231, "]")

temp21 = total
if (dice_211 == dice_221 == dice_231 == 2):
    print("Bunco!")
    bunco_count += 1
    total += bunco
elif(dice_211 == dice_221 == dice_231 != 2):
    print("Mini-Bunco!")
    mini_bunco_count += 1
    total += mini_bunco
else:
     if (dice_211 == 2) :
          total += 1
          print("+1")
     elif (dice_221 == 2) :
          total += 1
          print("+1")
     elif (dice_231 == 2) :
          total += 1
          print("+1")

if temp21 != total:
    input("Press Enter for start Round 2 Second Dice…")
    dice_212 = random.randint(1, 6)
    dice_222 = random.randint(1, 6)
    dice_232 = random.randint(1, 6)
    print("[", dice_212, dice_222, dice_232, "]")

    temp22 = total
    if (dice_212 == dice_222 == dice_232 == 2):
        print("Bunco!")
        bunco_count += 1
        total += bunco
    elif (dice_212 == dice_222 == dice_232 != 2):
        print("Mini-Bunco!")
        mini_bunco_count += 1
        total += mini_bunco
    else:
        if (dice_212 == 2):
            total += 1
            print("+1")
        elif (dice_222 == 2):
            total += 1
            print("+1")
        elif (dice_232 == 2):
            total += 1
            print("+1")

        if temp22 != total:
            input("Press Enter for start Round 2 Third Dice…")
            dice_213 = random.randint(1, 6)
            dice_223 = random.randint(1, 6)
            dice_233 = random.randint(1, 6)
            print("[", dice_213, dice_223, dice_233, "]")

            if (dice_213 == dice_223 == dice_233 == 2):
                print("Bunco!")
                bunco_count += 1
                total += bunco
            elif (dice_213 == dice_223 == dice_233 != 2):
                print("Mini-Bunco!")
                mini_bunco_count += 1
                total += mini_bunco
            else:
                if (dice_213 == 2):
                    total += 1
                    print("+1")
                elif (dice_223 == 2):
                    total += 1
                    print("+1")
                elif (dice_233 == 2):
                    total += 1
                    print("+1")

print("You have run out of rights for second round...")

input("Press Enter for start Round 3 First Dice…")

dice_311 = random.randint(1, 6)
dice_321 = random.randint(1, 6)
dice_331 = random.randint(1, 6)
print("[", dice_311, dice_321, dice_331, "]")

temp31 = total
if (dice_311 == dice_321 == dice_331 == 3):
    print("Bunco!")
    bunco_count += 1
    total += bunco
elif (dice_311 == dice_321 == dice_331 != 3):
    print("Mini-Bunco!")
    mini_bunco_count += 1
    total += mini_bunco
else:
    if (dice_311 == 3):
        total += 1
        print("+1")
    elif (dice_321 == 3):
        total += 1
        print("+1")
    elif (dice_331 == 3):
        total += 1
        print("+1")

if temp31 != total:
    input("Press Enter for start Round 3 Second Dice…")
    dice_312 = random.randint(1, 6)
    dice_322 = random.randint(1, 6)
    dice_332 = random.randint(1, 6)
    print("[", dice_312, dice_322, dice_332, "]")

    temp32 = total
    if (dice_312 == dice_322 == dice_332 == 3):
        print("Bunco!")
        bunco_count += 1
        total += bunco
    elif (dice_312 == dice_322 == dice_332 != 3):
        print("Mini-Bunco!")
        mini_bunco_count += 1
        total += mini_bunco
    else:
        if (dice_312 == 3):
            total += 1
            print("+1")
        elif (dice_322 == 3):
            total += 1
            print("+1")
        elif (dice_332 == 3):
            total += 1
            print("+1")

        if temp32 != total:
            input("Press Enter for start Round 3 Third Dice…")
            dice_313 = random.randint(1, 6)
            dice_323 = random.randint(1, 6)
            dice_333 = random.randint(1, 6)
            print("[", dice_313, dice_323, dice_333, "]")

            if (dice_313 == dice_323 == dice_333 == 3):
                print("Bunco!")
                bunco_count += 1
                total += bunco
            elif (dice_313 == dice_323 == dice_333 != 3):
                print("Mini-Bunco!")
                mini_bunco_count += 1
                total += mini_bunco
            else:
                if (dice_313 == 3):
                    total += 1
                    print("+1")
                elif (dice_323 == 3):
                    total += 1
                    print("+1")
                elif (dice_333 == 3):
                    total += 1
                    print("+1")

print("You have run out of rights for third round...")

input("Press Enter for start Round 4 First Dice…")

dice_411 = random.randint(1, 6)
dice_421 = random.randint(1, 6)
dice_431 = random.randint(1, 6)
print("[", dice_411, dice_421, dice_431, "]")

temp41 = total
if (dice_411 == dice_421 == dice_431 == 4):
    print("Bunco!")
    bunco_count += 1
    total += bunco
elif (dice_411 == dice_421 == dice_431 != 4):
    print("Mini-Bunco!")
    mini_bunco_count += 1
    total += mini_bunco
else:
    if (dice_411 == 4):
        total += 1
        print("+1")
    elif (dice_421 == 4):
        total += 1
        print("+1")
    elif (dice_431 == 4):
        total += 1
        print("+1")

if temp41 != total:
    input("Press Enter for start Round 4 Second Dice…")
    dice_412 = random.randint(1, 6)
    dice_422 = random.randint(1, 6)
    dice_432 = random.randint(1, 6)
    print("[", dice_412, dice_422, dice_432, "]")

    temp42 = total
    if (dice_412 == dice_422 == dice_432 == 4):
        print("Bunco!")
        bunco_count += 1
        total += bunco
    elif (dice_412 == dice_422 == dice_432 != 4):
        print("Mini-Bunco!")
        mini_bunco_count += 1
        total += mini_bunco
    else:
        if (dice_412 == 4):
            total += 1
            print("+1")
        elif (dice_422 == 4):
            total += 1
            print("+1")
        elif (dice_432 == 4):
            total += 1
            print("+1")

        if temp42 != total:
            input("Press Enter for start Round 4 Third Dice…")
            dice_413 = random.randint(1, 6)
            dice_423 = random.randint(1, 6)
            dice_433 = random.randint(1, 6)
            print("[", dice_413, dice_423, dice_433, "]")

            if (dice_413 == dice_423 == dice_433 == 4):
                print("Bunco!")
                bunco_count += 1
                total += bunco
            elif (dice_413 == dice_423 == dice_433 != 4):
                print("Mini-Bunco!")
                mini_bunco_count += 1
                total += mini_bunco
            else:
                if (dice_413 == 4):
                    total += 1
                    print("+1")
                elif (dice_423 == 4):
                    total += 1
                    print("+1")
                elif (dice_433 == 4):
                    total += 1
                    print("+1")

print("You have run out of rights for forth round...")


input("Press Enter for start Round 5 First Dice…")

dice_511 = random.randint(1, 6)
dice_521 = random.randint(1, 6)
dice_531 = random.randint(1, 6)
print("[", dice_511, dice_521, dice_531, "]")

temp51 = total
if (dice_511 == dice_521 == dice_531 == 5):
    print("Bunco!")
    bunco_count += 1
    total += bunco
elif (dice_511 == dice_521 == dice_531 != 5):
    print("Mini-Bunco!")
    mini_bunco_count += 1
    total += mini_bunco
else:
    if (dice_511 == 5):
        total += 1
        print("+1")
    elif (dice_521 == 5):
        total += 1
        print("+1")
    elif (dice_531 == 5):
        total += 1
        print("+1")

if temp51 != total:
    input("Press Enter for start Round 5 Second Dice…")
    dice_512 = random.randint(1, 6)
    dice_522 = random.randint(1, 6)
    dice_532 = random.randint(1, 6)
    print("[", dice_512, dice_522, dice_532, "]")

    temp52 = total
    if (dice_512 == dice_522 == dice_532 == 5):
        print("Bunco!")
        bunco_count += 1
        total += bunco
    elif (dice_512 == dice_522 == dice_532 != 5):
        print("Mini-Bunco!")
        mini_bunco_count += 1
        total += mini_bunco
    else:
        if (dice_512 == 5):
            total += 1
            print("+1")
        elif (dice_522 == 5):
            total += 1
            print("+1")
        elif (dice_532 == 5):
            total += 1
            print("+1")

        if temp52 != total:
            input("Press Enter for start Round 4 Third Dice…")
            dice_513 = random.randint(1, 6)
            dice_523 = random.randint(1, 6)
            dice_533 = random.randint(1, 6)
            print("[", dice_513, dice_523, dice_533, "]")

            if (dice_513 == dice_523 == dice_533 == 5):
                print("Bunco!")
                bunco_count += 1
                total += bunco
            elif (dice_513 == dice_523 == dice_533 != 5):
                print("Mini-Bunco!")
                mini_bunco_count += 1
                total += mini_bunco
            else:
                if (dice_513 == 5):
                    total += 1
                    print("+1")
                elif (dice_523 == 5):
                    total += 1
                    print("+1")
                elif (dice_533 == 5):
                    total += 1
                    print("+1")

print("You have run out of rights for fifth round...")



input("Press Enter for start Round 6 First Dice…")

dice_611 = random.randint(1, 6)
dice_621 = random.randint(1, 6)
dice_631 = random.randint(1, 6)
print("[", dice_611, dice_621, dice_631, "]")

temp61 = total
if (dice_611 == dice_621 == dice_631 == 6):
    print("Bunco!")
    bunco_count += 1
    total += bunco
elif (dice_611 == dice_621 == dice_631 != 6):
    print("Mini-Bunco!")
    mini_bunco_count += 1
    total += mini_bunco
else:
    if (dice_611 == 6):
        total += 1
        print("+1")
    elif (dice_621 == 6):
        total += 1
        print("+1")
    elif (dice_631 == 6):
        total += 1
        print("+1")

if temp61 != total:
    input("Press Enter for start Round 6 Second Dice…")
    dice_612 = random.randint(1, 6)
    dice_622 = random.randint(1, 6)
    dice_632 = random.randint(1, 6)
    print("[", dice_612, dice_622, dice_632, "]")

    temp62 = total
    if (dice_612 == dice_622 == dice_632 == 6):
        print("Bunco!")
        bunco_count += 1
        total += bunco
    elif (dice_612 == dice_622 == dice_632 != 6):
        print("Mini-Bunco!")
        mini_bunco_count += 1
        total += mini_bunco
    else:
        if (dice_612 == 6):
            total += 1
            print("+1")
        elif (dice_622 == 6):
            total += 1
            print("+1")
        elif (dice_632 == 6):
            total += 1
            print("+1")

        if temp62 != total:
            input("Press Enter for start Round 6 Third Dice…")
            dice_613 = random.randint(1, 6)
            dice_623 = random.randint(1, 6)
            dice_633 = random.randint(1, 6)
            print("[", dice_613, dice_623, dice_633, "]")

            if (dice_613 == dice_623 == dice_633 == 6):
                print("Bunco!")
                bunco_count += 1
                total += bunco
            elif (dice_613 == dice_623 == dice_633 != 6):
                print("Mini-Bunco!")
                mini_bunco_count += 1
                total += mini_bunco
            else:
                if (dice_613 == 6):
                    total += 1
                    print("+1")
                elif (dice_623 == 6):
                    total += 1
                    print("+1")
                elif (dice_633 == 6):
                    total += 1
                    print("+1")

print("You have run out of rights for sixth round...")

input("Press Enter for view your result")
print("Your total point : ", total)
print("Your bunco count : ", bunco_count)
print("Your mini bunco count : ", mini_bunco_count)