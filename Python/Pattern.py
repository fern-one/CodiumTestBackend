#3.1

def Article1(number : int) :
    for i in range(1,number+1) :
        print('*' * i)

Article1(3)

#3.2

def Article2(number : int) :
    for i in range(1,number+1) :
        for j in range(number-i) :
            print(' ',end='')
        print('*' * i)

Article2(3)

#3.3

def Article3(number : int) :
    center = 1
    for i in range(1,number+1):
        if number == 1 :
            print('*')
        else:
            for j in range(1,number-i+1):
                print(' ',end='')
            print('*',end='')
            if i>1:
                for k in range(1,center+1):
                    print(' ',end='')
                center = center + 2
                print('*',end='')
        print()

Article3(5)

'''for x in range(1,6):
    for y in range(6 - x):
        print(" ", end="")
    print('*', end="")
    for y in range(x):
        print("  ", end="")
    print('*', end="")
    print()'''

#3.4

def Article4(number : int) :
    k = number - 2
    half_round = (number + 1) // 2

    for i in range(half_round):
        print(' ' * i, end='')
        print('*', end='')
        print(' ' * k, end='')
        if (i + 1 != ((number + 1) // 2)) or number % 2 == 0:
            print('*', end='')
        k -= 2
        print()

    for i in range(number - half_round, 0, -1):
        print(' ' * (i - 1), end='')
        print('*', end='')
        print(' ' * (number - i - i), end='')
        if (i - 1 != ((number - half_round)) or (i == 1)):
            print('*', end='')
        print()

Article4(5)

#3.5

def Article5(number: int):
    k = 1
    for i in range((number + 1) // 2):
        for blank in range(1, ((number + 1) // 2) - i):
            print(' ', end='')
        print('*' * k, end='')
        k += 2
        print()
    if (number % 2 == 0):
        print('*' * (k - 2), end='')
        print()
        k = number - 1
    else:
        k = number
    for i in range(1, ((number) // 2 + 1)):
        for blank in range(i):
            print(' ', end='')
        k -= 2
        print('*' * k, end='')
        print()

Article5(9)

#3.6

def Article6(number: int):
    k = number
    p = 1
    if (number == 1):
        print('*')
    else:
        for i in range(1, number):
            for a in range(1, k):
                print('A', end='')
            if i == 1:
                print('+', end='')
            else:
                print('+', end='')
                for e in range(p):
                    print('E', end='')
                p += 2
                print('+', end='')
            for b in range(1, k):
                print('B', end='')
            k -= 1
            print()
        print('+', end='')
        for centerE in range(p):
            print('E', end='')
        print('+', end='')
        print()
        for i in range(1, number):
            for c in range(k):
                print('C', end='')
            if i == number - 1:
                print('+', end='')
            else:
                p -= 2
                print('+', end='')
                for e in range(p):
                    print('E', end='')
                print('+', end='')
            for c in range(k):
                print('D', end='')
            k += 1
            print()

Article6(5)