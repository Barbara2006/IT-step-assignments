
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def prime_generator():
    number = 2

    while True:
        if is_prime(number):
            yield number

        number += 1

primes = prime_generator()

for _ in range(10):
    print(next(primes))
