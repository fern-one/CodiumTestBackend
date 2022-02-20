def mutiples(number : int,divisor : int):
    if number % divisor == 0 :
        return True
    return False

for i in range(1,101):
    if mutiples(i,3) and  mutiples(i,5) :
        print('FizzBuzz')
    elif mutiples(i,3) :
        print('Fizz')
    elif mutiples(i,5) :
        print('Buzz')
    else:
        print(i)




