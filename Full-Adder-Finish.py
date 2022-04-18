a = 0  # it is temporary variable for loop.


while a < 1: 
    print("Welcome to Full-Adder!")
    print("--(1) Compute and display the outputs")
    print("--(2) Quit")

    choose = input("----You choose: ")

    if(choose == "1"):
        print("----You have chosen 1")
        b = 0
        while b < 1:
            base = input("------Which base will you use to enter data lines (base 16/8/2)?")
            if(base == "2"):
                c = 0
                while c < 1:
                    bin = input("--------Please enter input: ")

                    isOk = True
                    for i in bin:
                        if(i == "1" or i == "0"):
                            isBinary = True
                        else:
                            isOk = False

                    if(isOk):
                        if(len(bin) == 3 and isBinary):
                            c += 2
                            b += 2
                            if(bin == "111"):
                                A = 1
                                B = 1
                                C_IN = 1
                                SUM = 1
                                C_OUT = 1
                                print("----------SUM:", SUM)
                                print("----------C_OUT:", C_OUT)
                            elif(bin == "110"):
                                A = 1
                                B = 1
                                C_IN = 0
                                SUM = 0
                                C_OUT = 1
                                print("----------SUM:", SUM)
                                print("----------C_OUT:", C_OUT)
                            elif(bin == "101"):
                                A = 1
                                B = 0
                                C_IN = 1
                                SUM = 0
                                C_OUT = 1
                                print("----------SUM:", SUM)
                                print("----------C_OUT:", C_OUT)
                            elif(bin == "011"):
                                A = 0
                                B = 1
                                C_IN = 1
                                SUM = 0
                                C_OUT = 1
                                print("----------SUM:", SUM)
                                print("----------C_OUT:", C_OUT)
                            elif(bin == "100"):
                                A = 1
                                B = 0
                                C_IN = 0
                                SUM = 1
                                C_OUT = 0
                                print("----------SUM:", SUM)
                                print("----------C_OUT:", C_OUT)
                            elif(bin == "010"):
                                A = 0
                                B = 1
                                C_IN = 0
                                SUM = 1
                                C_OUT = 0
                                print("----------SUM:", SUM)
                                print("----------C_OUT:", C_OUT)
                            elif(bin == "001"):
                                A = 0
                                B = 0
                                C_IN = 1
                                SUM = 1
                                C_OUT = 0
                                print("----------SUM:", SUM)
                                print("----------C_OUT:", C_OUT)
                            elif(bin == "000"):
                                A = 0
                                B = 0
                                C_IN = 0
                                SUM = 0
                                C_OUT = 0
                                print("----------SUM:", SUM)
                                print("----------C_OUT:", C_OUT)
                            print("\n")
                        
                        else:
                            print("...Please enter 3-digit binary input...")
                    
                    else:
                        print("...Please enter a binary code...")

            elif(base == "8" or base == "16"):
                d = 0
                if(base == "8"):
                    type = "Octal"
                elif(base == "16"):
                    type = "Hexadecimal"
                
                while d < 1:
                    bin = input("--------Please enter input: ")
                    
                    isNumeric = True
                    for j in bin:
                        if(j == "0" or j == "1" or j == "2" or j == "3" or j == "4" or j == "5" or j == "6" or j == "7" or j == "8" or j == "9"):
                            isOk = True
                        else:
                            isNumeric = False
                    

                    if(isNumeric):
                        intBin = int(bin)
                        if(intBin > 7):
                            print("..." + type, bin, "cannot be represented with 3 bits! Please try again!...")
                        
                        else:
                            d += 2
                            b += 2
                            if(intBin == 0):
                                A = 0
                                B = 0
                                C_IN = 0
                                SUM = 0
                                C_OUT = 0
                                print("----------SUM:", SUM)
                                print("----------C_OUT:", C_OUT)
                            elif(intBin == 1):
                                A = 0
                                B = 0
                                C_IN = 1
                                SUM = 1
                                C_OUT = 0
                                print("----------SUM:", SUM)
                                print("----------C_OUT:", C_OUT)
                            elif(intBin == 2):
                                A = 0
                                B = 1
                                C_IN = 0
                                SUM = 1
                                C_OUT = 0
                                print("----------SUM:", SUM)
                                print("----------C_OUT:", C_OUT)
                            elif(intBin == 3):
                                A = 0
                                B = 1
                                C_IN = 1
                                SUM = 0
                                C_OUT = 1
                                print("----------SUM:", SUM)
                                print("----------C_OUT:", C_OUT)
                            elif(intBin == 4):
                                A = 1
                                B = 0
                                C_IN = 0
                                SUM = 1
                                C_OUT = 0
                                print("----------SUM:", SUM)
                                print("----------C_OUT:", C_OUT)
                            elif(intBin == 5):
                                A = 1
                                B = 0
                                C_IN = 1
                                SUM = 0
                                C_OUT = 1
                                print("----------SUM:", SUM)
                                print("----------C_OUT:", C_OUT)
                            elif(intBin == 6):
                                A = 1
                                B = 1
                                C_IN = 0
                                SUM = 0
                                C_OUT = 1
                                print("----------SUM:", SUM)
                                print("----------C_OUT:", C_OUT)
                            elif(intBin == 7):
                                A = 1
                                B = 1
                                C_IN = 1
                                SUM = 1
                                C_OUT = 1
                                print("----------SUM:", SUM)
                                print("----------C_OUT:", C_OUT)
                            print("\n")
                    
                    else:
                        print("..." + type, bin, "cannot be represented with 3 bits! Please try again!...")

            else:
                print("...Please choose an option...")
            
    elif(choose == "2"):
        a += 2
        print("You have chosen 2")
        print("Byee!")
    else:
        print("...Please choose an option...")
        print("\n")