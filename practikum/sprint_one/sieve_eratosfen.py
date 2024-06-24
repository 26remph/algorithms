import time


def eratosthenes(n):
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(2 * num, n + 1, num):
                numbers[j] = False
    return numbers


def eratosthenes_effective(n):
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(num * num, n + 1, num):
                numbers[j] = False
    return numbers 


def get_least_primes_linear(n):
    lp = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
    return primes, lp

# start_time = time.time()
# eratosthenes_effective(1000000)
# print("--- %s seconds ---" % (time.time() - start_time))

# start_time = time.time()
# eratosthenes(500000)
# print("--- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
get_least_primes_linear(1000000000)
print("--- %s seconds ---" % (time.time() - start_time))
