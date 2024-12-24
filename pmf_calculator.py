import pmf_module

print("Probability Mass Function Calculator")

while True:
    print("Enter 0 if you want to quit")
    print("Enter 1 if you want to calculate Discrete Uniform function")
    print("Enter 2 if you want to calculate Hypergeometric function")
    print("Enter 3 if you want to calculate Binomial function")
    print("Enter 4 if you want to calculate Geometric function")
    print("Enter 5 if you want to calculate Negative Binomial function")
    print("Enter 6 if you want to calculate Poisson function")
    num = int(input("Enter your number: "))

    # cloes the program
    if num == 0:
        print("Bye!")
        break

    # Discrete Uniform
    elif num == 1:
        result = pmf_module.discrete()
        print(f"\033[1mThe probability is {result:.3f}\033[0m\n")

    # Hypergeometric function
    elif num == 2:
        result = pmf_module.hypergeometric()
        print(f"\033[1mThe probability is {result:.3f}\033[0m\n")

    # Binomial function
    elif num == 3:
        result = pmf_module.binomial()
        print(f"\033[1mThe probability is {result:.3f}\033[0m\n")

    # Geometric function
    elif num == 4:
        result = pmf_module.geometric()
        print(f"\033[1mThe probability is {result:.3f}\033[0m\n")
        
    # Negative Binomial function
    elif num == 5:
        result = pmf_module.negative_binomial()
        print(f"\033[1mThe probability is {result:.3f}\033[0m\n")

    # Poissan function
    elif num == 6:
        result = pmf_module.poisson()
        print(f"\033[1mThe probability is {result:.3f}\033[0m\n")

    # Invalid number
    else:
        print("Invalid input, please enter a number between 0 and 6.")