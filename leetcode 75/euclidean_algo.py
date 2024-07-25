def gcd(a, b):
    #base case b is equal to 0
    while b != 0:
        a, b = b, a%b
        gcd(a, b)
    return a

print(gcd(10,3))