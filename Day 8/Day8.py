from collections import defaultdict
from itertools import combinations

class Day8:
    def part1(self, townMap):
        """
        Simulate the propagation of antennas in a town map and calculate the total number of unique antinodes.

        The town map is represented as a 2D list of characters, where each character represents a type of antenna.
        The propagation of each antenna is simulated by finding all unique pairs of antenna locations and computing
        the potential antinodes based on the pattern formed by the two antennas.

        Parameters
        ----------
        townMap : list of list of str
            The town map, represented as a 2D list of characters.

        Returns
        -------
        int
            The total number of unique antinodes.
        """
        n = len(townMap)  # Get the size of the town map (assumed to be a square).

        # Dictionary to store coordinates of each type of antenna found in the town map.
        antennas = defaultdict(list)
        for i in range(n):  # Iterate over rows.
            for j in range(n):  # Iterate over columns.
                if townMap[i][j] != ".":  # If the cell contains an antenna (not empty).
                    antennas[townMap[i][j]].append((i, j))  # Append its coordinates to the corresponding list.

        antinodes = set()  # Set to store unique potential antinode coordinates.

        # Process each type of antenna.
        for antenna in antennas:
            locations = antennas[antenna]  # Get all locations for this antenna type.

            # Find all unique pairs of antenna locations.
            for a, b in combinations(locations, 2):
                ax, ay = a  # First antenna coordinates.
                bx, by = b  # Second antenna coordinates.

                # Compute potential antinodes based on the pattern formed by the two antennas.
                cx, cy = ax - (bx - ax), ay - (by - ay)  # Antinode extrapolated "before" the line segment.
                dx, dy = bx + (bx - ax), by + (by - ay)  # Antinode extrapolated "after" the line segment.

                # Add valid antinode coordinates (within bounds of the map) to the set.
                if 0 <= cx < n and 0 <= cy < n:
                    antinodes.add((cx, cy))
                if 0 <= dx < n and 0 <= dy < n:
                    antinodes.add((dx, dy))

        return len(antinodes)  # Return the total number of unique antinodes.

    def part2(self, townMap):
        """
        Simulate the propagation of antennas in a town map and calculate the total number of unique antinodes.

        The town map is represented as a 2D list of characters, where each character represents a type of antenna.
        The propagation of each antenna is simulated by finding all unique pairs of antenna locations and computing
        the potential antinodes based on the pattern formed by the two antennas. The propagation is done indefinitely
        in both directions.

        Parameters
        ----------
        townMap : list of list of str
            The town map, represented as a 2D list of characters.

        Returns
        -------
        int
            The total number of unique antinodes.
        """
        n = len(townMap)  # Get the size of the town map.

        # Dictionary to store coordinates of each type of antenna found in the town map.
        antennas = defaultdict(list)
        for i in range(n):  # Iterate over rows.
            for j in range(n):  # Iterate over columns.
                if townMap[i][j] != ".":  # If the cell contains an antenna (not empty).
                    antennas[townMap[i][j]].append((i, j))  # Append its coordinates to the corresponding list.

        antinodes = set()  # Set to store unique potential antinode coordinates.

        # Process each type of antenna.
        for antenna in antennas:
            locations = antennas[antenna]  # Get all locations for this antenna type.

            # Find all unique pairs of antenna locations.
            for a, b in combinations(locations, 2):
                ax, ay = a  # First antenna coordinates.
                bx, by = b  # Second antenna coordinates.

                # Include the actual antenna locations as part of the antinodes.
                antinodes.add((ax, ay))
                antinodes.add((bx, by))

                # Compute potential antinodes extrapolated before and after the segment indefinitely.
                cx, cy = ax - (bx - ax), ay - (by - ay)  # Antinode extrapolated "before" the line segment.
                dx, dy = bx + (bx - ax), by + (by - ay)  # Antinode extrapolated "after" the line segment.

                # Iterate to include all antinodes along the extrapolated direction (within bounds).
                while 0 <= cx < n and 0 <= cy < n:
                    antinodes.add((cx, cy))
                    cx -= (bx - ax)  # Move further in the direction of extrapolation.
                    cy -= (by - ay)

                while 0 <= dx < n and 0 <= dy < n:
                    antinodes.add((dx, dy))
                    dx += (bx - ax)  # Move further in the direction of extrapolation.
                    dy += (by - ay)

        return len(antinodes)  # Return the total number of unique antinodes.

    @staticmethod
    def main():
        """
        Main method to read input from a file, process it to determine the total number of unique antinodes, and print the results.
        """
        townMap = []  # List to store the town map read from the input file.

        # Read the town map from the input file.
        with open("Day 8/input.txt", "r") as f:
            file = f.readlines()  # Read all lines from the file.
            for line in file:
                townMap.append(line.strip())  # Strip leading/trailing whitespace from each line.

            Day8_instance = Day8()  # Create an instance of the Day8 class.

            # Calculate the result for part 1 and display the output.
            antinodes = Day8_instance.part1(townMap)
            print(f"All unique spots for the antinodes are: {antinodes}")

            # Calculate the result for part 2 and display the output.
            moreAntinodes = Day8_instance.part2(townMap)
            print(f"All unique spots for the total antinodes are: {moreAntinodes}")

# If the script is run directly, execute the main function.
if __name__ == '__main__':
    Day8.main()
