"""
ProjectEuler.Sequences

Collection of classes for various type of sequences.

Author: Daniel Couture
User: MathYourLife
Date: Aug 19, 2012

Last Updated: Aug 31, 2012
"""

import numpy as np

class PerfectSquares(object):
    """
    A perfect square is an integer multiplied by itself.
    """
    def __init__(self):
        self.pos = None
        self.value = None
        self.squares = np.array([1])
    
    def get_squares_up_to(self, value):
        """
        Retrieve perfect squares up to a value either off the
        calculated values on the class or append to the class
        array and reeturn when the value is reached.
        """
        
        # We already know enough primes to give you what you want
        if value <= self.squares[-1]:
            return self.squares[self.squares <= value]
        
        # Get the range of roots that need to be appended
        max_root = int(np.sqrt(value)) + 1
        min_root = np.sqrt(self.squares[-1]) + 1
        
        # Calculate the perfect squares and append to the known list
        roots = np.arange(min_root, max_root)
        self.squares = np.append(self.squares, roots * roots)
        
        return self.squares
    
    def previous(self):
        """
        Move to the previous perfect square.
        
        @return: The previous perfect square
        @rtype:  int
        """
        
        if self.pos == None:
            self.pos = 0
        self.pos -= 1
        self.value = self.pos * self.pos
        return self.value
        
    def next(self):
        """
        Move to the next perfect square.
        
        @return: The next perfect square
        @rtype:  int
        """
        
        if self.pos == None:
            self.pos = 0
        self.pos += 1
        self.value = self.pos * self.pos
        return self.value

class Fibonacci(object):
    """
    A Fibonacci series class.  Provided with a starting condition
    it will propagate to the next value by finding the sum of the
    previous two values.
    
    @param current: The last value of the known sequence
    @type  current: int
    
    @param previous: The previous value of the known sequence
    @type  previous: int
    """
    
    def __init__(self, current = 1, previous = 0):
        self.current = current
        self.__previous = previous
    
    def next(self):
        """
        Generate the next value in the sequence
        
        @return: The next value in the sequence by summing the previous two
        @rtype:  int
        """
        next_value = self.current + self.__previous
        self.__previous = self.current
        self.current = next_value
        return self.current
    
    def previous(self):
        """
        Generate the next value in the sequence
        
        @return: The next value in the sequence by summing the previous two
        @rtype:  int
        """
        pre_value = self.current - self.__previous
        self.current = self.__previous
        self.__previous = pre_value
        return self.current

class Palindrome(object):
    """
    Palindrome - Efficiently jumps from a palindrome to
    the next/previous.  The internal _seed property tracks
    the left portion of the number and allows us to jump
    from one to the next.
    
    @param   start: Starting palindrome
    @type    start: int
    @default start: 1
    """
    def __init__(self, start = 1):
        # Validate the starting value if not provided
        if start != 1:
            if start < 0:
                print 'Start value must be a non negative integer palindrome.'
                raise
            if not self.is_a_palindrome(start):
                print 'Start value supplied is not a palindrome.'
                raise
        
        # Initialize the seed on the class
        self._odd_length = len(str(start)) % 2 == 1
        start_list = list(str(start))
        seed_len = (len(start_list) + 1) / 2
        self._seed = int(''.join(start_list[:seed_len]))
        
        self.value = start
    
    def is_a_palindrome(self, value):
        """
        is_a_palindrome - Check if the passed value is a palindrome.
        
        @param value: Integer to verify if is a palindrome
        @type  value: Int
        
        @return: If the value is a palindrome
        @rtype:  bool
        """
        str_value = str(value)
        forward_list = list(str_value)
        reverse_list = list(str_value)
        reverse_list.reverse()
        return forward_list == reverse_list
    
    def previous(self):
        """
        Find the next largest palindrome.
        
        @return: The next largest palindrome
        @rtype:  int
        """
        
        if self.value == 0:
            print 'Can not go back past 0'
            raise
        
        # Determine how to modify the seed value
        if len(str(self._seed)) != len(str(self._seed - 1)):
            # Next palindrome has a fewer number of digits
            if self._odd_length == True:
                self._seed = self._seed - 1
                self._odd_length = False
            else:
                self._seed = (self._seed * 10) - 1
                self._odd_length = True
        else:
            # Palindrome is not changing the number of digits
            if self.value == 11:
                # Special case to transfer down to single digits
                self._seed = 9
                self._odd_length = True
            else:
                # Decrement the seed
                self._seed -= 1
        
        # Now that we have the right next seed, create the palindrome
        str_seed = str(self._seed)
        prefix_list = list(str_seed)
        suffix_list = list(str_seed)
        suffix_list.reverse()
        if self._odd_length:
            # Palindrome should be an odd length so no 
            # repeating the center digit
            self.value = int(''.join(prefix_list) + ''.join(suffix_list[1:]))
        else:
            # Just flip and concat the seed
            self.value = int(''.join(prefix_list) + ''.join(suffix_list))
        return self.value
    
    def next(self):
        """
        Find the smallest largest palindrome.
        
        @return: The next smallest palindrome
        @rtype:  int
        """
        
        # Determine how to modify the seed value
        if len(str(self._seed)) != len(str(self._seed + 1)):
            # Next palindrome has increased the number of digits
            if self._odd_length == True:
                self._seed = (self._seed + 1) / 10
                self._odd_length = False
            else:
                self._seed += 1
                self._odd_length = True
        else:
            # Increment the seed
            self._seed += 1
        
        # Now that we have the right next seed, create the palindrome
        str_seed = str(self._seed)
        prefix_list = list(str_seed)
        suffix_list = list(str_seed)
        suffix_list.reverse()
        if self._odd_length:
            # Palindrome should be an odd length so no 
            # repeating the center digit
            self.value = int(''.join(prefix_list) + ''.join(suffix_list[1:]))
        else:
            # Just flip and concat the seed
            self.value = int(''.join(prefix_list) + ''.join(suffix_list))
        return self.value

class TriangleNumbers(object):
    """
    Triangle Number Sequence
    
    The sequence is defined as the number of dots required to make
    larger and larger triangles by adding a row with one more dot 
    than the last row.
    
    1, 3, 6, 10, 15, 21, ...
    """
    def __init__(self):
        self.pos = None
        self.value = None
    
    def set_position(self, pos):
        """
        Set the position in the sequence for the class and
        return the value of the Triangle number sequence at 
        that position.
        
        @param: Set the position in the triangle sequence
        @type:  int
        
        @return: The triangle value at that position in the sequence
        @rtype:  int
        """
        self.pos = pos
        self.value = (pos * (pos + 1)) / 2
        return self.value
    
    def next(self):
        """
        Move to the next value in the triangle sequence.
        
        @return: The next triangle number
        @rtype:  int
        """
        if self.pos == None:
            self.pos = 0
            self.value = 0
        self.pos += 1
        self.value += self.pos
        return self.value
    
    def previous(self):
        """
        Move to the previous value in the triangle sequence.
        
        @return: The previous triangle number
        @rtype:  int
        """
        self.value -= self.pos
        self.pos -= 1
        return self.value
        
