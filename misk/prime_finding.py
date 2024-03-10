def trialDivision(nb):
    prime = []
    for i in range(2, nb + 1):
        isPrime = True
        for element in prime:
            if element * element > i:
                break
            if i % element == 0:
                isPrime = False
                break
        if isPrime:
            prime.append(i)
    return prime

nb = 1000000
print(trialDivision(nb))
