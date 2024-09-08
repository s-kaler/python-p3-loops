#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print('Happy New Year!')
    pass

def square_integers(int_list):
    int_squares = list()
    for num in int_list:
        int_square = num * num
        int_squares.append(int_square)
    return int_squares
    pass

def fizzbuzz():
    for i in range(1,101):
        
        if (i % 15) == 0:
            print('FizzBuzz')
        elif (i % 3) == 0:
            print('Fizz')
        elif (i % 5) == 0:
            print('Buzz')
        else:
            print(i)
    pass
