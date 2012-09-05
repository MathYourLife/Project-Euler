"""
Project Euler - Problem 11
http://projecteuler.net/problem=11

In the 20x20 grid below, four numbers along a diagonal line 
have been marked.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10[26]38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95[63]94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17[78]78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35[14]00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 x 63 x 78 x 14 = 1788696.

What is the greatest product of four adjacent numbers in any 
direction (up, down, left, right, or diagonally) in the 20x20 grid?

Author: Daniel Couture
User: MathYourLife
Date: Sep 1, 2012
"""

from ProjectEuler.Problem import Solution
from re import findall
import numpy as np

class Problem011(Solution):
    """
    Extension of the ProjectEuler.Solution class that solves the problem:
    
    In the 20x20 grid below, four numbers along a diagonal line 
    have been marked.
    
    08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
    32 98 81 28 64 23 67 10[26]38 40 67 59 54 70 66 18 38 64 70
    67 26 20 68 02 62 12 20 95[63]94 39 63 08 40 91 66 49 94 21
    24 55 58 05 66 73 99 26 97 17[78]78 96 83 14 88 34 89 63 72
    21 36 23 09 75 00 76 44 20 45 35[14]00 61 33 97 34 31 33 95
    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
    
    The product of these numbers is 26 x 63 x 78 x 14 = 1788696.
    
    What is the greatest product of four adjacent numbers in any 
    direction (up, down, left, right, or diagonally) in the 20x20 grid?
    """
    
    # Bit flags used to identify search directions.
    SEARCH_S  = 1
    SEARCH_SE = 2
    SEARCH_SW = 4
    SEARCH_E  = 8
    
    def __init__(self):
        super(Problem011, self).__init__()
        self.search = None
        self.grid = None
        self.max_prod = None
    
    def find_solution(self):
        """
        This method contains the guts of finding the solution.
        The timer starts just prior to calling this method
        and stops just after returning the solution's value.
        """
        
        # Convert the string into a 20x20 array
        self.grid = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
"""
        self.grid = np.array(findall('\d+', self.grid),'int')
        self.grid.shape = (20, 20)
        
        # Create the full search bit flag grid assuming we can search
        # in any direction from any cell.
        self.search =  np.ones((20, 20), dtype=np.int) * \
            (self.SEARCH_S | self.SEARCH_SE | self.SEARCH_SW | self.SEARCH_E)
        
        self.remove_invalid_searches()
        
        # Remove any searches that would contain a zero in the product.
        for pos in self.find_value(0):
            row = pos[0]
            col = pos[1]
            
            # Shift the starting position to cover all searches that
            # would hit the position of this zero.  Turn off the
            # appropriate search bit for each.
            for shift in range(0, 4):
                if row - shift >= 0:
                    self.bits_off((row - shift, col), self.SEARCH_S)
                if col - shift >= 0:
                    self.bits_off((row, col - shift), self.SEARCH_E)
                if (row - shift >= 0) and (col - shift >= 0):
                    self.bits_off((row - shift, col - shift), self.SEARCH_SE)
                if (row - shift >= 0) and (col + shift < 20):
                    self.bits_off((row - shift, col + shift), self.SEARCH_SW)
        
        # Complete the actual search here.  The general process:
        # 1)  Loop through search values (x) from the max of 99 and down to 1
        # 2)  Find any/all locations of x in the grid.
        # 3)  Find all combinations of starting positions and search directions
        #     (south, east, south east, south west), that would contain x.
        # 4)  Calculate the product for each case found in 3) and determine 
        #     if it is the new max product found.
        # 5)  Since all values from the max of 99 down to x have been covered,
        #     if max product > (x - 1)^4 it is impossible to find anything 
        #     larger. (SOLUTION FOUND)
        # 6)  If we haven't found the solution yet, decrement x and repeat 
        #     from step 2)
        for search_value in range(np.max(self.grid), 0, -1):
            for search_pos in self.find_value(search_value):
                search_directions = self.get_search_directions(search_pos)
                for direction, pos_list in search_directions.items():
                    for pos in pos_list:
                        self.get_product(pos, direction)
            if pow(search_value - 1, 4) < self.max_prod:
                break
        
        # Return the largest product found
        return self.max_prod
    
    def remove_invalid_searches(self):
        """
        Unset the bit flags for positions that would extend outside
        the boundaries of the search grid.
        """
        # Remove the ability to search South, South East, or 
        # South West with a starting position in the bottom three
        # rows since there is not enough room to get 4 values.
        for row in range(17, 20):
            for col in range(0, 20):
                bits = self.SEARCH_S | self.SEARCH_SE | self.SEARCH_SW
                self.bits_off((row, col), bits)
        
        # Remove the ability to search East, or South East
        # with a starting position in the right three
        # columns since there is not enough room to get 4 values.
        for row in range(0, 20):
            for col in range(17, 20):
                bits = self.SEARCH_E | self.SEARCH_SE
                self.bits_off((row, col), bits)
        
        # Remove the ability to search South West
        # with a starting position in the left three
        # columns since there is not enough room to get 4 values.
        for row in range(0, 20):
            for col in range(0, 3):
                bits = self.SEARCH_SW
                self.bits_off((row, col), bits)
        
    def get_product(self, pos, direction):
        """
        For the specified starting position on the grid and 
        direction, grab the 4 values off the grid, calculate
        the product and check if it's the new max.
        """
        
        if direction == 'south':
            # south search: grab the 3 values below
            values = self.grid[pos[0] : pos[0] + 4, pos[1]]
            self.bits_off(pos, self.SEARCH_S)
        elif direction == 'east':
            # east search: grab the 3 values below
            values = self.grid[pos[0], pos[1] : pos[1] + 4]
            self.bits_off(pos, self.SEARCH_E)
        elif direction == 'south_east':
            # south east search: grab 3 values on a negative slope
            values = [ \
                self.grid[pos[0], pos[1]],
                self.grid[pos[0] + 1, pos[1] + 1],
                self.grid[pos[0] + 2, pos[1] + 2],
                self.grid[pos[0] + 3, pos[1] + 3],
                ]
            self.bits_off(pos, self.SEARCH_SE)
        elif direction == 'south_west':
            # south west search: grab 3 values on a positive slope
            values = [ \
                self.grid[pos[0], pos[1]],
                self.grid[pos[0] + 1, pos[1] - 1],
                self.grid[pos[0] + 2, pos[1] - 2],
                self.grid[pos[0] + 3, pos[1] - 3],
                ]
            self.bits_off(pos, self.SEARCH_SW)
        
        self.is_max(np.prod(values))
    
    def is_max(self, check):
        """
        Set the class max_prod value to the passed value
        if it's larger or not set.
        """
        if self.max_prod == None:
            self.max_prod = check
        elif check > self.max_prod:
            self.max_prod = check
    
    def get_search_directions(self, pos):
        """
        The brains of the class.  Supplied with starting 
        grid position determine the combination of starting
        locations and directions that would include that position
        given the 4 value product.  Searches are excluded if they
        extend outside the grid bounds or have already been covered
        by a larger number.
        
        Ex:
        If passed the position (2, 5) for the value 79 with the grid
        08 02 22 97 38 15 00 40 00
        49 49 99 40 17 81 18 57 60
        81 49 31 73 55[79]14 29 93
        52 70 95 23 04 60 11 42 69
        22 31 16 71 51 67 63 89 41
        24 47 32 60 99 03 45 02 44
        32 98 81 28 64 23 67 10 26
        67 26 20 68 02 62 12 20 95
        24 55 58 05 66 73 99 26 97
        21 36 23 09 75 00 76 44 20
        
        south:
        (2, 5) - [79 60 67 03]  valid
        (1, 5) - [81 79 60 67]  bit flag off. Already searched by 81
        (0, 5) - [15 81 79 60]  bit flag off. Already searched by 81
        (-1, 5) - outside bounds of the grid
        east:
        (2, 5) - [79 14 29 93]  bit flag off. Already searched by 93
        (2, 4) - [55 79 14 29]  valid
        (2, 3) - [73 55 79 14]  valid
        (2, 2) - [31 73 55 79]  valid
        south east:
        (2, 5) - [79 11 89 44]  bit flag off. Already searched by 89
        (1, 4) - [17 79 11 89]  bit flag off. Already searched by 89
        (0, 3) - [97 17 79 11]  bit flag off. Already searched by 97
        (-1, 2) - outside bounds of the grid
        south west:
        (2, 5) - [79 04 71 32]  valid
        (1, 6) - [18 79 04 71]  valid
        (0, 7) - [40 18 79 04]  valid
        (-1, 8) - outside bounds of the grid
        """
        south = []
        for shift in range(0, 4):
            # check if moving outside bounds
            if pos[0] - shift < 0:
                break
            # check bit flag of shifted position too see 
            # if this group has already been covered.
            shift_pos = (pos[0] - shift, pos[1])
            if self.search[shift_pos] & self.SEARCH_S:
                south.append(shift_pos)
        
        east = []
        for shift in range(0, 4):
            # check if moving outside bounds
            if pos[1] - shift < 0:
                break
            # check bit flag of shifted position too see 
            # if this group has already been covered.
            shift_pos = (pos[0], pos[1] - shift)
            if self.search[shift_pos] & self.SEARCH_E:
                east.append(shift_pos)
        
        south_west = []
        for shift in range(0, 4):
            # check if moving outside bounds
            if (pos[0] - shift < 0) or (pos[1] + shift > 19):
                break
            # check bit flag of shifted position too see 
            # if this group has already been covered.
            shift_pos = (pos[0] - shift, pos[1] + shift)
            if self.search[shift_pos] & self.SEARCH_SW:
                south_west.append(shift_pos)
        
        south_east = []
        for shift in range(0, 4):
            # check if moving outside bounds
            if (pos[0] - shift < 0) or (pos[1] - shift < 0):
                break
            # check bit flag of shifted position too see 
            # if this group has already been covered.
            shift_pos = (pos[0] - shift, pos[1] - shift)
            if self.search[shift_pos] & self.SEARCH_SE:
                south_east.append(shift_pos)
        
        # Return all valid starting positions by direction
        return {
            'south'      : south,
            'east'       : east,
            'south_west' : south_west,
            'south_east' : south_east
            }
    
    def find_value(self, value):
        """
        Find the position all instances of the value in the grid.
        """
        
        bools = self.grid == value
        
        # Track how man positions out of the total we have located
        qty = np.sum(bools)
        found_qty = 0
        
        pos_list = []
        for row in range(0, 20):
            for col in range(0, 20):
                # Check the bools array for a location match
                if bools[row, col]:
                    found_qty += 1
                    pos_list.append((row, col))
                    # If we've found them all, return early
                    if found_qty == qty:
                        return pos_list
        return pos_list
        
    def bits_off(self, pos, bits):
        """
        Remove the search direction bits for the grid position.
        """
        
        # Invert and turn off the selected bits
        self.search[pos] = self.search[pos] & ~bits

def main():
    """
    Run this if called directly versus imported
    """
    prob = Problem011()
    
    prob.solve()
    
    print prob.problem_statement()
    print prob.results()

if __name__ == "__main__":
    main()

