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

    def part2(self, corruptedMemory):
        """
        Calculate the sum of all multiplication operations found in the corrupted memory commands,
        following the instructions to add or not to add the results to the total sum.

        This function searches for patterns of the form 'mul(x,y)', 'do()', or 'don't()' within each command
        string in the provided corruptedMemory list, where x and y are integers. It then calculates the
        product of x and y for each 'mul(x,y)' occurrence and adds the product to the total sum according
        to the following rules:

        - If the previous command was 'do()', add the product to the total sum.
        - If the previous command was 'don't()', do not add the product to the total sum.

        Parameters
        ----------
        corruptedMemory : list
            A list of strings representing corrupted memory commands, each of which may contain
            zero or more 'mul(x,y)', 'do()', or 'don't()' patterns.

        Returns
        -------
        int
            The total sum of the products of all 'mul(x,y)' patterns found in the corruptedMemory,
            following the instructions to add or not to add the results to the total sum.
        """
        accurateSum = 0 # Initialize the sum of all valid multiplication operations
        add_it = True # A flag to determine whether to add the multiplication result to the sum

        # Define the regex pattern to match 'do()', 'don't()', or 'mul(x,y)' where x and y are 1-3 digit numbers
        pattern = re.compile(r"(?:do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))")

        # Iterate through each command in the corrupted memory
        for command in corruptedMemory:
            matches = pattern.finditer(command) # Find all matches for the defined pattern in the command

            if matches: # If any matches are found, process them
                for line in matches:
                    if line[0] == "do()": # If the match is 'do()', set the flag to allow adding multiplication values
                        add_it = True
                    elif line[0] == "don't()": # If the match is 'don't()', set the flag to skip adding multiplication values
                        add_it = False
                    else:  # If the match is 'mul(x,y)', process the multiplication
                        if add_it: # Only add the product if the flag is set to True
                            accurateSum += (int(line[1]) * int(line[2]))
                        else: # Skip adding the product if the flag is False
                            continue

        return accurateSum # Return the total sum after processing all commands
    
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

        # Call part2 method to calculate the accurate sum of all 'mul(x,y)' patterns while considering the conditionals
        accurateMulSum = day3_instance.part2(corruptedMemory)

        # Print the total sum and the accurate sum of multiplication values respectively
        print(f"The total sum of multiplication values is: {totalMulSum}")
        print(f"The accurate sum of multiplication values is: {accurateMulSum}")

if __name__ == "__main__":
    Day3.main()