from collections import defaultdict

class Day5:
    def part1(self, rules, updates):
        """
        Calculate the sum of middle elements from a list of updates that satisfy given rules.

        Each update is a list of numbers, and the rules are pairs of numbers indicating
        an ordering constraint (a should appear before b). For each update, if it correctly
        satisfies all the rules, it contributes its middle element to the sum.

        Parameters
        ----------
        rules : list of tuples
            A list of pairs (a, b) representing ordering constraints.
        updates : list of lists
            A list containing lists of numbers to be evaluated against the rules.

        Returns
        -------
        int
            The sum of the middle elements from each update that satisfies the rules.
        """
        middleSum = 0 # Sum of middle elements for correct updates

        for update in updates:
            idx = {} # Map to store the index positions of each number in the update
            correct = True # Flag to track if the current update satisfies all rules
            n = len(update)
            
            # Create an index map for the numbers in the current update
            for i, num in enumerate(update):
                idx[num] = i

            # Validate the current update against all rules
            for a, b in rules:
                if a in idx and b in idx: # Only consider rules applicable to this update
                    if idx[a] > idx[b]: # If rule is violated, mark as incorrect
                        correct = False
                        break
            
            # Add the middle element if the update is valid
            if correct:
                middleSum += update[n//2]

        return middleSum
    
    def part2(self, rules, updates):
        """
        Calculate the sum of middle elements from a list of updates that do not satisfy given rules after being correctly ordered.

        Each update is a list of numbers, and the rules are pairs of numbers indicating
        an ordering constraint (a should appear before b). For each update, if it does not
        satisfy all the rules, the numbers in the update are reordered to satisfy the rules
        and the middle element of the reordered update is added to the sum.

        Parameters
        ----------
        rules : list of tuples
            A list of pairs (a, b) representing ordering constraints.
        updates : list of lists
            A list containing lists of numbers to be evaluated against the rules.

        Returns
        -------
        int
            The sum of middle elements from each update that does not satisfy the rules, after being correctly ordered.
        """
        totalMidSum = 0 # Sum of middle elements for all updates after correction

        for update in updates:
            n = len(update)

            # Filter out relevant rules applicable to the current update
            current_rules = []
            for a, b in rules:
                if a in update and b in update:
                    current_rules.append((a, b))

            # Calculate in-degrees to determine dependencies for topological sorting
            indeg = defaultdict(int)
            for a, b in current_rules:
                indeg[b] += 1

            # Perform topological sorting to find the correct order
            correct_order = []
            while len(correct_order) < len(update):
                for x in update:
                    if x in correct_order: # Skip already sorted numbers
                        continue
                    if indeg[x] <= 0: # If no dependencies remain, add to sorted order
                        correct_order.append(x)
                        for a, b in current_rules: # Reduce in-degrees of dependent numbers
                            if a == x:
                                indeg[b] -= 1

            # Add the middle element of the corrected update to the total sum
            totalMidSum += correct_order[n//2]
            

        return totalMidSum

    @staticmethod
    def main():
        """
        Main method to read input from a file, process it to determine the sums of middle
        elements from correct and incorrect updates, and print the results.

        This method reads the input data from "Day 5/input.txt", creates an instance of
        the Day5 class, and utilizes the part1 and part2 methods to calculate and display
        the middle sums of the correct and incorrect updates after applying a problem
        dampening technique.

        The results are printed to the console, showing the middle sums of correct and
        incorrect updates.
        """
        # Read and parse the input data
        with open("Day 5/input.txt", "r") as f:
            raw_rules, raw_updates = f.read().split("\n\n")

            # Process rules into a list of (a, b) tuples
            rules = []
            for rule in raw_rules.split("\n"):
                num1, num2 = rule.split("|")
                rules.append((int(num1), int(num2)))

            # Process updates into a list of lists of integers
            raw_updates = raw_updates.split("\n")
            updates = []
            for update in raw_updates:
                temp = update.split(",")
                updates.append(list(map(int, temp)))

            # Create an instance of Day5 and solve both parts
            Day5_instance = Day5()

            # Part 1: Middle sum of valid updates
            middleSum = Day5_instance.part1(rules, updates)
            print(f"Middle sum of the correct upd
            ates: {middleSum}")

            # Part 2: Middle sum of corrected updates minus Part 1's result
            totalMidSum = Day5_instance.part2(rules, updates) - middleSum
            print(f"Middle sum of the incorrect updates, after correction: {totalMidSum}")


if __name__ == "__main__":
    Day5.main()