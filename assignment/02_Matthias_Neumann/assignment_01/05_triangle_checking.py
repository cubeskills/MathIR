#!/usr/bin/python3

## Task 05 – Triangle Checking

if __name__ == "__main__":
    while True:
        user_input=input("Please enter the side lengths of a triangle, separated by commas: ")
        lengths = user_input.split(',')
        if len(user_input) == 0:
            print("No input is good input.")
            exit(0)
        if len(lengths) != 3:
            print(user_input+'?',"That could maybe be the side lengths of a",str(len(lengths))+"-angle","but not a triangle. Nice try.")
            continue
        try:
            #lengths=[int(l) for l in user_input.split(',')]   #- Version für ganzzahlige Seitenlängen
            lengths=[float(l) for l in lengths] #- Version für Gleitkomma-Ungenauigkeit
            #- Dreiecksungleichung prüfen
            a,b,c=lengths
            if a+b > c and b+c > a and c+a > b:
                break
            if a+b >= c and b+c >= a and c+a >= b:
                print("Every triangle with side lengths",str(a)+',',str(b),"and",str(c),"is degenerate.")
                exit(0)
            print(user_input,"are not side-lengths of a triangle. Try again.")
        except ValueError:
            print(user_input+'?',"Some of that does not look like a number! Try harder.")
            #break
    a,b,c=lengths
    equalities=(a == b)+(b == c)+(c == a)
    if equalities == 0:
        answer="scalene"
    elif equalities == 1:
        answer="isosceles"
    elif equalities == 3:
        answer="equilateral"
    else:
        print("It broke.")
        exit(1)
        
    print("Every triangle with side lengths",str(a)+',',str(b),"and",str(c),"is",answer+'.')
