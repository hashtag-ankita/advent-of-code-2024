import re
class Day3:
    def part1(self, corruptedMemory):
        """
        Calculate the sum of all multiplication operations found in the corrupted memory commands.

        This function searches for patterns of the form 'mul(x,y)' within each command string in the
        provided corruptedMemory list, where x and y are integers. It then calculates the product of x and y
        for each occurrence and sums all the products.

        Parameters
        ----------
        corruptedMemory : list
            A list of strings representing corrupted memory commands, each of which may contain 
            zero or more 'mul(x,y)' patterns.

        Returns
        -------
        int
            The total sum of the products of all 'mul(x,y)' patterns found in the corruptedMemory.
        """
        # Regular expression to match 'mul(x,y)' where x and y are 1-3 digit integers
        pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

        totalMulSum = 0 # Initialize the sum of all multiplication results
        for command in corruptedMemory:
            matches = pattern.finditer(command) # Find all 'mul(x,y)' patterns in the current command
            if matches:
                for line in matches:
                    MulValue = int(line[1]) * int(line[2]) # Compute the product of the matched numbers
                    totalMulSum += MulValue # Add the product to the total sum

        return totalMulSum # Return the sum of all multiplication results
    
    @staticmethod
    def main():
        """
        Reads in the input.txt file in the Day 3 directory and prints the sum of all
        multiplication operations found in the corrupted memory commands to the console.

        Does not take any parameters and does not return any value.
        """
        corruptedMemory = [] # Initialize an empty list to store corrupted memory commands

        with open('Day 3/input.txt', 'r') as f:
            file = f.readlines() 

            for line in file:
                # Remove any leading or trailing whitespace from the line
                line = line.strip()
                corruptedMemory.append(line) # Add each line from the file to the corruptedMemory list

        # Create an instance of the Day3 class
        day3_instance = Day3()

        # Call part1 method to calculate the total sum of all 'mul(x,y)' patterns
        totalMulSum = day3_instance.part1(corruptedMemory)

        # Print the total sum of multiplication values
        print(f"The total sum of multiplication values is: {totalMulSum}")

if __name__ == "__main__":
    Day3.main()