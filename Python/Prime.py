
def Prime(number : int):
    for i in range(2,(number//2)+1) :
        if number % i == 0 :
            return False
    return True

n = int(input('Enter number for find all prime number = '))
num_list = []
for j in range(2,n+1) :
    if Prime(j) :
        num_list.append(j)
print( n, '->' ,num_list)