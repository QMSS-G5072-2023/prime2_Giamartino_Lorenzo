import math

def is_prime(n):
"""
Returns True if input is a prime number, False if not prime. 

Input: an integer
Output: True or False if prime or not prime, respectively. 

    Examples
    --------
    >>> from prime_Giamartino_Lorenzo import is_prime
    >>> n = 7
    >>> is_prime(n)
    True

"""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True