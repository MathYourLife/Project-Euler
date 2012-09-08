"""
ARITHMETIC class

classes and methods contained are targeted to basic number
theory and number facts.
"""

import numpy as np

# Global list of primes to be referenece and appended to by all
# Arithmetic methods so they don't need to be recalculated.
PRIMES_LIST = np.array([2, 3], dtype=int)

def primes_up_to(value):
    """
    Generate a list of primes up to the passed value,
    if the class instance already contains a list of 
    primes, determine if we already know enough or need
    to calculate more.
    
    @example:
        call:    primes_up_to(30)
        returns: array([2 3 5 7 11 13 17 19 23 29])
    
    @param value: Number to be broken into its prime factors
    @type  value: int
    
    @return: Array of prime factors
    @rtype: numpy.ndarray
    """
    
    global PRIMES_LIST
    # We already know enough primes to give you what you want
    if (not len(PRIMES_LIST) == 0) and (value <= PRIMES_LIST[-1]):
        return PRIMES_LIST[PRIMES_LIST <= value]
    
    # Prime the candidates array with a list of numbers from the last
    # value checked through to the desired value.  Any composite
    # numbers will be stripped out in one of the following loops.
    # The array is primed with 2 and 3.  When generating a list of 
    # candidates, skip the even valuesself.
    max_known_prime = PRIMES_LIST[-1]
    candidates = np.arange(max_known_prime + 2, value + 1, 2, dtype=int)
    check_up_to = np.sqrt(value)
    
    # If the PRIMES_LIST is already populated, eliminate their multiples
    for num in PRIMES_LIST:
        # Only need to run through primes <= sqrt(value)
        if num > check_up_to:
            break
        # Strip out any multiples of 'num'
        bools = candidates % num == 0
        candidates = candidates[bools == False]
        # All the candidates were composite, return
        if len(candidates) == 0:
            return PRIMES_LIST[PRIMES_LIST <= value]
    
    # From this point we either do not know any primes or not
    # enough primes, so fill in the gap
    
    # Loop through starting at the last number check to the desired
    # candidates and start stripping out composite numbers from the 
    # candidates array
    for num in np.arange(max_known_prime + 1, value + 1, dtype=int):
        # Only need to run through primes <= sqrt(value)
        if num > check_up_to:
            break
        # Strip out any multiples of 'num', making sure to keep
        # 'num' since it's prime
        bools = (candidates % num == 0) & (candidates > num)
        candidates = candidates[bools == False]
        # All the candidates were composite, return
        if len(candidates) == 0:
            return PRIMES_LIST
    
    # Update the class with the new information and return
    PRIMES_LIST = np.append(PRIMES_LIST, candidates)
    return PRIMES_LIST


def find_multiples_up_to(factor_list, upper_limit):
    """
    Given a list of factors generate an array of multiples for those values. up
    to and including the upper limit value.  Multiple factors will result in an
    array that is the union of the individual sets.
    @example:
        call:    find_multiples_up_to([3,5], 15)
        returns: array([3, 5, 6, 9, 10, 12, 15])
    
    @param factor_list: list of factors to generate multiples from, if multiples
                    provided, the returned array is a union of the individual sets
    @type  factor_list: list
    
    @param upper_limit: The higest value to include in the list of multiples
    @type  upper_limit: int
    
    @return: Array of multiples
    @rtype: numpy.ndarray
    """
    
    values = np.arange(1, upper_limit + 1, dtype=int)
    multiples = np.array([])
    for factor in factor_list:
        multiples = np.unique(np.concatenate([multiples, 
            values[values % factor == 0]]))
    
    return multiples

def prime_factorization(value):
    """
    Generate a prime factorization for the passed value.
    
    @example:
        call:    prime_factorization(24)
        returns: array([2, 2, 2, 3])
    
    @param value: Number to be broken into its prime factors
    @type  value: int
    
    @return: Array of prime factors
    @rtype: numpy.ndarray
    """
    
    # Get a list of primes up to either 10000 or half the value
    p_list = primes_up_to(min(10000, int(np.sqrt(value))) + 1)
    
    # Starting to look for the factors.  Starting at 2
    # work up and pull out factors until the value is 1
    factor_list = np.array([], dtype=int)
    working = value
    for prime in p_list:
        # If the value is 1, we've got it all
        if working == 1:
            break
        while working % prime == 0:
            # this prime is a factor of value so pull it out
            factor_list = np.append(factor_list, prime)
            working = working / prime
    
    if not working == 1:
        factor_list = np.append(factor_list, working)
    if (len(factor_list) == 0) and (not working == 1):
        return np.array([value])
    else:
        return factor_list

def factors(value, count_only=False):
    """
    Retrieve the factors of the value passed.
    
    @param value: Number to find the factors of
    @type  value: int
    
    @param   count_only: Return just the number of factors
    @type    count_only: bool
    @default count_only: False
    
    @return: Array of factors
    @rtype:  numpy.ndarray
    """
    prime_factors = prime_factorization(value)
    
    if count_only:
        count = 1
        for factor in np.unique(prime_factors):
            count *= np.sum(prime_factors == factor) + 1
        return count
    
    factor_list = np.array([], dtype=int)
    for i in range(1, value + 1):
        if value % i == 0:
            factor_list = np.append(factor_list, i)
    return factor_list


