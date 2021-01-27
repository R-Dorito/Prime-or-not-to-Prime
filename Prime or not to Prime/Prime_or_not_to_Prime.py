import random

game = False
over = True

while game is not over:
    value = int(random.random() * 100)
    print(value,"is this a prime?")
    inp = input()
    for n in range (1, int(value/2)):
        if value % n == 0:
             isPrime = False
             print("no")
        else:
             print("yes")


