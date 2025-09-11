def decimalToBinary(n):
    if(n == 0):
        return "0"
    # initialize binary as empty
    binary = ""
    # till n > 0
    while(n != 0):
        x = n%2
        binary = str(x) + binary
        n = n//2

    return binary

x = decimalToBinary(0)
print(x)

# time-complexity = O(logn) 