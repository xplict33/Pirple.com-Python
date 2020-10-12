for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    # This calculate the prime number.
    # A prime number is any number that is divisible by 1 and the number itself.
    # "( i % i == 0)" say if the number in i divided by i equals to 0 and "(i % 1 == 0) ...
    # if the number in i divided by 1 equals to 0. print "prime".
    # " % " is used to get reminder in divisions.
    elif (i % i == 0) and (i % 1 == 0):
        print("prime")
    else:
        print(i)