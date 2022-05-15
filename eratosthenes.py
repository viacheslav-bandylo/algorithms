# Sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit.

# Решето Эратосфена - алгоритм нахождения всех простых чисел до некоторого целого числа n.


def eratosthenes(n):
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for i in range(2 * num, n + 1, num):
                numbers[i] = False
    return numbers


def eratosthenes_effective(n):
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for i in range(num * num, n + 1, num):
                numbers[i] = False
    return numbers


def eratosthenes_linear(n):
    lp = [0] * (n + 1)  # least prime
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


print(eratosthenes(100))

print(eratosthenes_effective(100))

print(eratosthenes_linear(100))
