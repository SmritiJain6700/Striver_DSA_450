def decimalToBinary(n):
    # initialize binary as empty
    binary = ""
    # till n > 0
    while(n != 0):
        x = n%2
        binary = str(x) + binary
        n = n//2

    return binary

x = decimalToBinary(5)
print(x)

# time-complexity = O(logn) 