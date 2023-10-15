

#A program to find all generators

# function for the GCD
def gcd(a, b):
    if (a == 0):
        return b;
    return gcd(b % a, a);

# Print the generatorns of n

def printGeneratorns(n):

    # 1 is always a generator
    print("1", end = " ");

    for i in range(2,n):

            # A number x is generator
            # of GCD is 1
            if (gcd(i, n) == 1):
                 print(i, end = " ");

n = 10;
printGeneratorns(n);


###This code is find on https://www.geeksforgeeks.org/generators-finite-cyclic-group-addition/