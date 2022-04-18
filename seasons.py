while True:
    x = input("Please give me a month name...")
    x = x.upper()
    if x == "JANUARY" or x == "FEBRUARY" or x == "DECEMBER":
        print(x.capitalize(),"is Winter")
    elif x == "MARCH" or x == "APRIL" or x == "MAY":
        print(x.capitalize()," is Spring")
    elif x == "JUNE" or x == "JULY" or x == "AUGUST":
        print(x.capitalize(),"is Summer")
    elif x == "SEPTEMBER" or x == "OCTOBER" or x == "NOVEMBER":
        print(x.capitalize(),"is Fall")
    elif x == "EXIT":
        break
    else:
        print("Please write a month name...")
