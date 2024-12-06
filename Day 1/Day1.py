from collections import Counter

class Day1:
    def part1(self, lst1, lst2):
        '''
        Calculate the total distance between pairs of location IDs from two lists
        '''
        # Sort the first list of location IDs
        lst1.sort()

        # Sort the second list of location IDs
        lst2.sort()

        n = len(lst1) # Get the number of elements in the lists

        totalDistance = 0
        for i in range(n):
            # Calculate the absolute distance between corresponding location IDs
            distance = abs(lst1[i] - lst2[i])

            # Accumulate the total distance
            totalDistance += distance

        # Return the total distance
        return totalDistance

    def part2(self, lst1, lst2):
        '''
        Calculate the total similarity score between two lists.
        Similarity score is calculated by multiplying the value of an element from the first list with the number of times it appears in the second list.
        '''
        # Count occurences of each element in the second list
        lst2Counter = Counter(lst2)

        totalSimilarityScore = 0
        for num in lst1:
            # Check if the number exists in the second list
            if num in lst2Counter:
                # Add the product of the number and its count in the second list
                totalSimilarityScore += (num * lst2Counter[num])

        # Return the total similarity score
        return totalSimilarityScore

    @staticmethod
    def main():
        '''
        Main method to read input data, process the lists using part1 and part2, and print the results.
        '''
        lst1 = [] # List to store the first column of the input
        lst2 = [] # List to store the second column of the input

        # try-except block to handle file not found error
        try:
            # Open the input file and read its contents
            with open("Day 1\input.txt", "r") as f:
                f = f.readlines() # Read all lines from the files

                for line in f:
                    # split the line into two parts (space-separated values)
                    line = line.split()

                    # Append the first part to the first list
                    lst1.append(int(line[0]))

                    # Append the second part to the second list
                    lst2.append(int(line[1]))
        except FileNotFoundError:
            print("File not found!")

        # Create an instance of the Day1 class
        Day1_instance = Day1()

        # Calculate the total distance using part1
        totalDistance = Day1_instance.part1(lst1, lst2)

        # Calculate the total similarity score using part2
        totalSimilarityScore = Day1_instance.part2(lst1, lst2)

        # Print the results
        print("Total Distance: ", totalDistance)
        print("Total Similarity Score: ", totalSimilarityScore)

# Check if the script is being run as the main module and call the main method
if __name__ == "__main__":
    Day1.main()