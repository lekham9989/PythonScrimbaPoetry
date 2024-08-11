# PERFORMANCE AND TIMELINE MODULE
# Experiment with sieve of Eratosthenes
# code for sieve of Eratosthenes below - it's a list comprehension
import timeit
# import the timeit code
# print the timestamps telling us how much time its gonna take and run 10 cycles of each of these
def test1():
    [x for x in range(1, 151) if not any([x % y == 0 for y in range(2, x)]) and not x == 1]
    return(1)

def test2():
    [x for x in range(2, 151) if not any([x % y == 0 for y in range(2, x)])]
    return(1)

def test3():
    # Initialize a list
    primes = []
    for possiblePrime in range(2, 151):
        # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
# print(primes)
    return(1)


print(timeit.timeit('test1()', globals=globals(), number=10))
print(timeit.timeit('test2()', globals=globals(), number=10))
print(timeit.timeit('test3()', globals=globals(), number=10))

# encapsulate calls inside the function and check the time for all the 3 ways of writing code
# boom! messy code the third one is faster than other two. So, list comprehension can't be the fastest but even messy code can be the fastest.

# console: times taken to run the 3 tests
# 0.935999870300293 - test1
# 0.8949999809265137 - test2
# 0.04900002479553223 - test3