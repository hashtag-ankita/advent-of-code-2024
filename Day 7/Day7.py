import re
from itertools import product

class Day7:
    def part1(self, equations):
        """
        This function takes a list of strings representing arithmetic equations and returns the total sum of all left-hand side (LHS) values that can be matched with their corresponding right-hand side (RHS) values by applying the combination of "+" and "*" operators.

        The function iterates through each equation string and tries all possible combinations of operators to evaluate the RHS and match it with the LHS. If a combination is found that matches the LHS, the LHS is added to the total sum and the evaluation is stopped for that equation.

        Parameters
        ----------
        equations : list of str
            A list of strings representing arithmetic equations.

        Returns
        -------
        int
            The total sum of all valid LHS values.
        """

        lhsSum = 0 # Initialize the sum of valid left-hand side (LHS) values.

        # Define the regex pattern to extract the LHS and RHS of the equation
        pattern = re.compile(r"^(\d+): ((\d\s?)+)$")

        # Iterate through each equation string in the input
        for equation in equations:
            match = re.match(pattern, equation) # Match the equation with the regex pattern

            # Extract and convert the LHS (number before the colon) to an integer
            lhs = int(match.group(1))

            # Extract the RHS (numbers after the colon)
            raw_rhs = match.group(2) 
            rhs = list(map(int, raw_rhs.split(" "))) # Convert the RHS string into a list of integers

            # Generate all possible combinations of "+" and "*" operators for (len(rhs) - 1) slots.
            combinations = product("+*", repeat=len(rhs)-1)          

            # Check each operator combination to evaluate the RHS and match it with LHS.  
            for combination in combinations:
                res = rhs[0] # Star with the first number in RHS
                for i in range(1, len(rhs)): # Apply each operator between successive numbers in RHS
                    if combination[i-1] == "*":
                        res *= rhs[i] # Multiply if the operator is "*"
                    else:
                        res += rhs[i] # Add if the operator is "+"
                
                # If the result matches the LHS, add LHS to the sum and stop further combinations.
                if res == lhs:
                    lhsSum += lhs
                    break
        
        return lhsSum # Return the total sum of valid LHS values.

    def part2(self, equations):
        """
        This function takes a list of strings representing arithmetic equations and returns the total sum of all left-hand side (LHS) values that can be matched with their corresponding right-hand side (RHS) values by applying the combination of "+", "*", and "|" operators.

        The function iterates through each equation string and tries all possible combinations of operators to evaluate the RHS and match it with the LHS. If a combination is found that matches the LHS, the LHS is added to the total sum and the evaluation is stopped for that equation.

        The function returns the total sum of all valid LHS values.

        Parameters
        ----------
        equations : list of str
            A list of strings representing arithmetic equations.

        Returns
        -------
        int
            The total sum of all valid LHS values.
        """
        lhsSum = 0 # Initialize the sum of valid LHS values.

        # Define the regex pattern to extract the LHS and RHS parts of the equation.
        pattern = re.compile(r"^(\d+): ((\d\s?)+)$")

        # Iterate through each equation string in the input.
        for equation in equations:
            match = re.match(pattern, equation) # Match the equation with the regex pattern.

            lhs = int(match.group(1)) # Extract and convert the LHS (number before the colon).

            raw_rhs = match.group(2) # Extract the RHS (number after the colon)
            rhs = list(map(int, raw_rhs.split(" "))) # Convert the RHS string into a list of integers

            # Generate all possible combinations of "+", "*", and "|" operators for (len(rhs) - 1) slots.
            combinations = product("+*|", repeat=len(rhs)-1)            

            # Check each operator combination to evaluate the RHS and match it with LHS
            for combination in combinations:
                res = rhs[0] # STart with the first number in RHS
                for i in range(1, len(rhs)): # Apply each operator between successive numbers in RHS
                    if combination[i-1] == "*":
                        res *= rhs[i] # Multiple if the operator is "*"
                    elif combination[i-1] == "|":
                        res = int(f"{res}{rhs[i]}") # Concatenate the numbers as string and convert to integer
                    else:
                        res += rhs[i] # Add if the operator is "+"
                
                # If the result matches the LHS, add LHS to the sum and stop further combinations
                if res == lhs:
                    lhsSum += lhs
                    break

        return lhsSum # Return the total sum of valid LHS values.

    @staticmethod
    def main():
        """
        Main method to read input from a file, process it to determine the sums of valid
        left-hand side (LHS) values from correct and incorrect updates, and print the results.
        """
        equations = [] # Initialize a list to store equations from the input file.

        # Read the equations from the input file and clean up whitespace.
        with open("Day 7/input.txt", "r") as f:
            file = f.readlines()
            for line in file:
                equations.append(line.strip()) # Remove leading/trailing whitespace

            Day7_instance = Day7() # Create an instance of the Day7 class

            # Part 1: Using 2 operators "+" & "*", we find the total calibration result by combining the LHS of valid equations from the input
            totalCalibResult = Day7_instance.part1(equations)
            print(f"Total calibration result: {totalCalibResult}")

            # part 2: Using 3 operators "+", "*", and "|", we find the actual total calibration result by combining the LHS of valid equations from the input
            actualCalibResult = Day7_instance.part2(equations)
            print(f"Actual calibration result: {actualCalibResult}")

if __name__ == '__main__':
    Day7.main()