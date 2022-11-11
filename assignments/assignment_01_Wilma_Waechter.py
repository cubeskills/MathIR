#Task 1
def welcome():
    name = input('Please enter your name: ')
    print(f'Hello {name}, nice to meet you!')
    print('Welcome to the programming course!')
    return
welcome()

#Task 2
def reversedWords():
    word = input('Enter word to reverse: ')
    return word[::-1]

reversedWords()

#Task 3
def fibonacci():
    try:
        n = int(input('Enter integer up to which the fibonacci numbers shall be printed: '))
        F_n_2, F_n_1 = 0, 1
        print(f'{F_n_2}, {F_n_1}, ', sep=' ', end='', flush=True )
        while F_n_1 + F_n_2 < n:
            print(f'{F_n_2 + F_n_1}, ', sep=' ', end='', flush=True)
            F_n_2, F_n_1 = F_n_1, F_n_2 + F_n_1
        return
    except:
        print('Please enter an integer')


fibonacci()


#Task 4
def selectivePrinting():
    n = int(input('Please enter integer up to which shall be printed except the numbers divisible by 3: '))
    for i in range(n + 1):
        if i % 3 == 0:
            continue
        else:
            print(f'{i}, ', sep=' ', end='', flush=True)
    return

selectivePrinting()

#Task 5
def triangleChecking():
    try:
        x, y, z = input(
            'Please enter the 3 lengths of the sides of your triangle. They should be seperated by a white space after each integer.  ').split()
        x, y, z = int(x), int(y), int(z)
        if x == y and y == z:
            print('Your triangle is equilateral.')

        elif x == y or y == z:
            print('Your triangle is isosceles.')
        else:
            print('Your triangle is scalene.')
        if 2 * max(x, y, z) < x + y + z:
            print('The triangle inequality holds.')
        else:
            print('The triangle inequality does not hold.')
    except:
        print('Please enter a valid input. Input must be 3 integers seperated by a white space each.')


triangleChecking()

#Task 6
def decimalToOctal():
    try:
        n = int(input('Please enter a number in decimal to be converted to octal: '))
        tmpArr = []
        while n > 0:
            tmpArr.append(n % 8)
            n = n // 8
        # declaring the as decimal place as multiplicator for the result and initializing with value for first loop pass
        # declaring result variable and initializing with the neutral element under addition
        decimalPlace = 1
        result = 0
        for j in range(len(tmpArr)):
            result += tmpArr[j] * decimalPlace
            decimalPlace *= 10
        return result

    except:
        print('Please enter a valid input. Input must be an integer.')


print(decimalToOctal())
