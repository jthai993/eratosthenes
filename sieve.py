# Brute Force
def brute_primes(arr):
    # Loop through all nums in arr
    for num in arr:
        # Only check numbers greater than 1
        if num > 1:
            # Check if all nums divisible by nums in arr
            if all(num % i != 0 for i in range(2, num)):
                # If not divisible
                print(num)


# brute_primes([0, 1, 2, 3, 4, 5])


# Sieve of Eratosthenes
def sieve_of_eratosthenes(n):
    if n <= 2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    # Divisor from 2
    # up to sqrt of n
    for i in range(2, int(n**0.5)):
        # Mark multiples of that number as isPrime = False
        if is_prime[i]:
            for num in range(i*i, n, i):
                is_prime[num] = False
    # Use list comprehension to return arr of numbers that are prime
    return [i for i in range(n) if is_prime[i]]


print(sieve_of_eratosthenes(100))
