#!/usr/bin/python3

## Task 04 – Selective Printing

if __name__ == "__main__":
    bound=int(input("Upper bound for the numbers: "))
    mod3=3 #! Please note that 0 is divisible by 3.
    comma=""
    for i in range(bound):
        if mod3 == 3:
            mod3=1
            continue
        print(comma,end="")
        print(i,end="")
        comma=", "
        mod3+=1
    #! Also note that negative integers exist!
    i=0
    mod3=3
    while True:
        i-=1
        mod3-=1
        if mod3 == 0:
            mod3 = 3
        else:
            print(',',i,end="")

#*
#* Tipp: Wer sich nicht imstande sieht schnell genug STRG-C zu drücken,
#* um zu verhindern dass der Anfang der Zahlenkolonne aus dem Rückscroll-Puffer verschwindet,
#* kann die Ausgabe an ein Pager-Programm (z.B. 'more' oder 'less') umleiten.
#*
#* Zum Beispiel so:
#$ python3 04_selective_printing.py | more
#*

