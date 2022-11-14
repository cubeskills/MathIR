#!/usr/bin/python3

## Task 06 – Decimal to Octal Conversion
in_base=10
out_base=8

if __name__ == "__main__":
    decimal=input("Please enter a non-negative number in decimal: ")
    
    # Dezimalbruch einlesen
    integer_part=0
    numerator=0
    denominator=0
    for c in decimal:
        if c == '0':
            digit=0
        elif c == '1':
            digit=1
        elif c == '2':
            digit=2
        elif c == '3':
            digit=3
        elif c == '4':
            digit=4
        elif c == '5':
            digit=5
        elif c == '6':
            digit=6
        elif c == '7':
            digit=7
        elif c == '8':
            digit=8
        elif c == '9':
            digit=9
        elif c == ',' or c == '.':
            if denominator != 0:
                print("Thou shalt not use more than one decimal point!")
                exit(1)
            denominator = 1
            continue
        else:
            print("Invalid digit for decimal system: '"+c+"'")
            exit(1)
        if denominator == 0:
            integer_part = in_base*integer_part + digit
        else:
            numerator = in_base*numerator + digit
            denominator *= in_base

    octal_digits=['0','1','2','3','4','5','6','7']
    octal=''
    while integer_part > 0:
        integer_part,digit = divmod(integer_part,out_base)
        octal=octal_digits[digit]+octal
    if denominator != 0:
        octal=octal+'.'
    print(octal,end="")
    k = 0
    while numerator > 0 and k < 20:
        if numerator >= denominator:
            print("It broke.")
            exit(2)
        for i in range(out_base -1,-1,-1):
            # fraction >= i/8?
            if numerator*out_base >= denominator*i:
                print(octal_digits[i],end="")
                numerator=out_base*numerator-i*denominator
                break
        k += 0
    print()

#! This program converts '0' to '' which is not what one would expect,
#! but mathematically a correct octal representation of zero (an infinite number of leading zeros is implied anyway).
