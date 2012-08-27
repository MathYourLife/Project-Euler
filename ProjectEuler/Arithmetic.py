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
        from numpy import array
        self.primes_through = 1
        self.primes_list = array([])
    
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
        from numpy import append, array
        
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
        from numpy import arange, append
        
        # We already know enough primes to give you what you want
        if value <= self.primes_through:
            return self.primes_list[self.primes_list <= value]
        
        # Prime the values array with a list of numbers from the last
        # value checked through to the desired value.  Any composite
        # numbers will be stripped out in one of the following loops
        min_val = self.primes_through + 1
        values = arange(min_val, value+1)
        
        # if this instance already knows some primes use them first
        # to eliminate numbers from the values array that are 
        # composite numbers.
        for num in self.primes_list:
            # Only need to run through the lower half
            if num > value / 2:
                break
            # Strip out any multiples of 'num'
            bools = values % num == 0
            values = values[bools == False]
            # All the values were composite, update the primes_through
            # and return
            if len(values) == 0:
                self.primes_through = value
                return self.primes_list
        
        # If we don't know any primes yet or the primes we do know
        # don't cover the lower half of the desired value.
        if len(self.primes_list) == 0 or (self.primes_list[-1] < value / 2):
            # Loop through starting at the last number check to the desired
            # values and start stripping out composite numbers from the 
            # values array
            for num in arange(self.primes_through + 1, value+1):
                # Only need to run through the lower half
                if num > value / 2:
                    break
                # Strip out any multiples of 'num', making sure to keep
                # 'num' since it's prime
                bools = (values % num == 0) & (values > num)
                values = values[bools == False]
                # All the values were composite, update the primes_through
                # and return
                if len(values) == 0:
                    self.primes_through = value
                    return self.primes_list
        
        # Update the class with the new information and return
        self.primes_through = value
        self.primes_list = append(self.primes_list, values)
        return self.primes_list

