def nfactorial(n):
    result = 0
    while n > 0:
        result *= n
        n -= 1
    return result

print(nfactorial(1))
