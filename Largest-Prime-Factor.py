def max_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n = n / i
    return n


print(max_prime_factor(600851475143))
