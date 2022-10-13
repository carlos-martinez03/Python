print("\n\n==============\nPrime numbers")

limitS = int(input("Number to Start : "))
limitF = int(input("Number to Finish : "))
if limitS > limitF:
    limitS, limitF = limitF, limitS

for i in range(limitS, limitF + 1):
    if i in (2, 3, 5, 7):
        isPrime = True
    elif i % 2 == 0:
        isPrime = False
    elif i % 3 == 0:
        isPrime = False
    elif i % 5 == 0:
        isPrime = False
    elif i % 7 == 0:
        isPrime = False
    else:
        isPrime = True

    print(i, " ", isPrime)
