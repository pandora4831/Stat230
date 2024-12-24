import math

# calculate pmf of discrete distribution function and return it
def discrete():
    print("This is to calculate the discrete uniform probability mass function.\n")

    # Read range of the pmf
    while True:
        a = int(input("Enter the beginning of the range (a): "))
        b = int(input("Enter the end of the range (b): "))

        # Check for invalid range
        if a > b:
            print("Invalid range: 'a' should be less than or equal to 'b'. Please try again.")
        else:
            break  # Exit the loop when the range is valid

    # Calculate the probability
    return 1 / (b - a + 1)



def binomial():
    print("This is to calculate the Binomial probability mass function.")

    # n indicates num of trials
    # p indicates probability of success

    n = int(input("Enter the number of trial n: "))
    p = float(input("Enter the probability of success p: "))
    x = int(input("Enter your x: "))

    return math.comb(n, x) * math.pow(p, x) * math.pow(1-p, n-x)



def hypergeometric():
    print("This is to calculate the Hypergeometric probability mass function.")

    # N indicates number of sample
    # r indicates number of target
    # n indicates number of elements we choose 

    cn = int(input("Enter the number of sample N: "))
    r = int(input("Enter the number of target r: "))
    n = int(input("Enter the number of elements we choose n: "))
    x = int(input("Enter your x: ")) 

    return math.comb(r,x) * math.comb(cn-r, n-x) / math.comb(cn, n)



def geometric():
    print("This is to calculate the geometric probability mass function")

    p = float(input("Enter the probability of success p: "))
    x = int(input("Enter your total number of trials x: "))

    return p * math.pow(1-p, x-1)


def poisson():
    print("This is to calculate the Poisson probability mass function.")

    mean = float(input("Enter the mean value: "))
    x = int(input("Enter number of events x: "))

    return math.pow(math.e, -mean) * math.pow(mean, x) / math.factorial(x)



def negative_binomial():
    print("This is to calculate the discrete uniform probability mass function.")

    # x is num of failures and k is num of successes
    # total number of trials: k + x

    k = int(input("Enter the number of successes, k: "))
    p = float(input("Enter the probability of success, p: "))
    x = int(input("Enter number of failures, x: "))

    return math.comb(x+k-1, x) * math.pow(p, k) * math.pow(1-p, x) 
