class Day4:
    def part1(self, wordSearch):
        """
        Find the number of times the string 'XMAS' appears horizontally, vertically, or diagonally in a given 2D word search.

        Parameters
        ----------
        wordSearch : list
            A 2D list of characters representing the word search.

        Returns
        -------
        int
            The number of times 'XMAS' appears in the word search.
        """
        rows = len(wordSearch) # Number of rows in the grid
        cols = len(wordSearch[0]) # Number of columns in the grid

        numberOfXmas = 0 # Counter for the occurences of 'XMAS'

        # Generate all possible directions (8 directions)
        directions = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx != 0 or dy != 0: # Skip the (0, 0) direction
                    directions.append((dx, dy))

        # dd = [(-1, -1), (-1, 0), (-1, 1),
        #       (0, -1),           (0, 1),
        #       (1, -1), (1, 0), (1, 1)]

        # Iterate through each cell in the grid
        for row in range(rows):
            for col in range(cols):
                # Check all directions from the current cell
                for dx, dy in directions:
                    match_found = True # Assume a match until proven otherwise

                    # Check each character of 'XMAS' in the current direction
                    for k, x in enumerate('XMAS'):
                        ii = row + k * dx # New row index
                        jj = col + k * dy # New column index

                        # If out of bounds, no match can be found in this direction
                        if not (0 <= ii < rows and 0 <= jj < cols):
                            match_found = False
                            break

                        # If the character doesn't match, no match in this direction
                        if wordSearch[ii][jj] != x:
                            match_found = False
                            break
                    
                    # Increment the count if a match was found
                    if match_found:
                        numberOfXmas += 1

        return numberOfXmas # Returns the number of times 'XMAS' appears in the word search
    

    def part2(self, wordSearch):
        """
        Count the number of times the string 'MAS' appears in an 'X' shape within a given 2D word search.

        This function searches for patterns where the string 'MAS' appears in an 'X' shape around 
        the letter 'A' within the word search grid. It checks for four possible 'X' configurations 
        with 'MAS' or 'SAM' in the diagonal positions.

        Parameters
        ----------
        wordSearch : list
            A 2D list of characters representing the word search.

        Returns
        -------
        int
            The number of times 'MAS' appears in an 'X' shape in the word search.
        """
        rows = len(wordSearch) # Number of rows in the grid
        cols = len(wordSearch[0]) # Number of columns in the grid

        numOfMAS = 0 # Counter for the occurences of 'MAS'

        # Iterate through each cell in the grid
        for row in range(1, rows-1):
            for col in range(1, cols-1):
                if wordSearch[row][col] == 'A': # Since the center is always 'A', no matter which case of X-MAS it is, we check if the current cell is 'A'
                    # Check if the surrounding cells form an 'X' shape of the word 'MAS' (4 possible cases)
                    if (
                        (wordSearch[row-1][col-1] == 'M' and wordSearch[row-1][col+1] == 'M' and wordSearch[row+1][col-1] == 'S' and wordSearch[row+1][col+1] == 'S') or
                        (wordSearch[row-1][col-1] == 'S' and wordSearch[row-1][col+1] == 'S' and wordSearch[row+1][col-1] == 'M' and wordSearch[row+1][col+1] == 'M') or
                        (wordSearch[row-1][col-1] == 'M' and wordSearch[row-1][col+1] == 'S' and wordSearch[row+1][col-1] == 'M' and wordSearch[row+1][col+1] == 'S') or
                        (wordSearch[row-1][col-1] == 'S' and wordSearch[row-1][col+1] == 'M' and wordSearch[row+1][col-1] == 'S' and wordSearch[row+1][col+1] == 'M')
                    ):
                        numOfMAS += 1

        return numOfMAS # Returns the number of times 'MAS' in 'X' shape appears in the word search

    @staticmethod
    def main():
        """
        Reads the word search grid from a file and prints the number of times the word 'XMAS' appears in all directions.
        """
        wordSearch = []

        # Read the grid from the file
        with open("Day 4/input.txt", "r") as f:
            file = f.readlines()

            for line in file:
                line = line.strip() # Remove trailing whitespace (if any)
                wordSearch.append(line)

        # Create an instance of the Day4 class
        Day4_instance = Day4()

        # Scan the word search grid to find the number of times 'XMAS' appears
        numOfXmas = Day4_instance.part1(wordSearch)

        # Scan the word search grid to find the number of 'MAS' in 'X' shape
        numOfMAS = Day4_instance.part2(wordSearch)
        
        print(f"The number of times 'XMAS' appears in the word search grid is: {numOfXmas}")
        print(f"The number of 'MAS' in 'X' shape in the word search grid is: {numOfMAS}")

if __name__ == "__main__":
    Day4.main()