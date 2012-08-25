"""
ARITHMETIC class

classes and methods contained are targeted to basic number
theory and number facts.
"""

def find_multiples_up_to(factors, upper_limit):
    """
    Given a list of factors generate an array of multiples for those values. up
    to and including the upper limit value.  Multiple factors will result in an
    array that is the union of the individual sets.
    @example:
        call:    find_multiples_up_to([3,5], 15)
        returns: array([3, 5, 6, 9, 10, 12, 15])
    
    @param factors: list of factors to generate multiples from, if multiples
                    provided, the returned array is a union of the individual sets
    @type  factors: list
    
    @param upper_limit: The higest value to include in the list of multiples
    @type  upper_limit: int
    
    @return: Array of multiples
    @rtype: numpy.ndarray
    """
    from numpy import array, arange, unique, concatenate
    
    values = arange(1, upper_limit+1)
    multiples = array([])
    for factor in factors:
        multiples = unique(concatenate([multiples, 
            values[values % factor == 0]]))
    
    return multiples


class Primes:
    """
    The ever useful but difficult to predict prime number set.
    """
    def __init__(self):
        pass
    
    def prime_factorization(self, value):
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
        from numpy import array, append
        
        # Get a list of primes up to either 10000 or half the value
        primes_list = self.primes_up_to(min(10000, value / 2))
        
        # Starting to look for the factors.  Starting at 2
        # work up and pull out factors until the value is 1
        factors = array([])
        working = value
        for prime in primes_list:
            # If the value is 1, we've got it all
            if working == 1:
                break
            while working % prime == 0:
                # this prime is a factor of value so pull it out
                factors = append(factors, [prime])
                working = working / prime
        if len(factors) == 0:
            return array([value])
        else:
            return factors
    
    def primes_up_to(self, value):
        """
        Generate a list of primes up to the passed value
        
        @example:
            call:    primes_up_to(30)
            returns: array([2 3 5 7 11 13 17 19 23 29])
        
        @param value: Number to be broken into its prime factors
        @type  value: int
        
        @return: Array of prime factors
        @rtype: numpy.ndarray
        """
        from numpy import arange
        
        # List the values from 2..value
        values = arange(2, value+1)
        bools = values % 1 != 0
        # Loop through the numbers.  Cross off any 
        # multiples as we go.  Anything left is a prime
        for num in values:
            # Only need to run through the lower half
            if num > value / 2:
                break
            # If we've alredy marked it off as a multiple, skip
            if bools[num-2]:
                continue
            # add in any multiples of num to the bool array
            bools = bools | ((values % num == 0) & (values > num))
        # return the non multiples
        return values[bools == False]

