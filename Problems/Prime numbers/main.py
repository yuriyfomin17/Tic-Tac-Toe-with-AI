from math import sqrt

prime_numbers = [2]


def is_prime(x: int) -> bool:
    limit = sqrt(x)
    for divider in prime_numbers:
        if divider > limit:
            break
        if not x % divider:
            return False
    return True


for i in range(3, 1001, 2):
    if is_prime(i):
        prime_numbers.append(i)