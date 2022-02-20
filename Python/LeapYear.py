def mutiples(number : int,divisor : int):
    if number % divisor == 0 :
        return True
    return False

def notmutiples(number: int, divisor: int):
    if number % divisor != 0:
        return True
    return False


year = int(input('Enter Leap Year : '))

if mutiples(year,400) and mutiples(year,100) :
    print(year , ' -> True ')
elif notmutiples(year,400) and notmutiples(year,100) and mutiples(year,4) :
    print(year,'-> True')
else:
    print(year,'-> False')