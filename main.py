isprime = True
numbers = int(input ("Enter any number to know that its prime number or not."))
if (numbers == 0):
    print("Number is neither prime nor composite")
elif (numbers == 1):
    print("Its a prime number")
elif (numbers > 1):
    for i in range(2, numbers):
        if (numbers % i == 0):
            isprime = False
            break
    if (isprime == True):
        print("Number is a prime number")
    else:
        print("Numner is not a prime number")
else:
    print("Something went wrong")