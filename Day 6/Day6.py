class Day6:
    def find_guard_position(self, mapped_area):
        """
        Locate the starting position of the guard in the mapped area.
        The guard's position is represented by '^' in the grid.

        Parameters
        ----------
        mapped_area : list of str
            The grid (2D area) where the guard patrols.

        Returns
        -------
        tuple
            Coordinates (row, column) of the guard's position.
        """
        for i, row in enumerate(mapped_area):
            if '^' in row:
                return i, row.index('^')

    def part1(self, mapped_area):
        """
        Simulate the guard's patrol and calculate the number of distinct spots patrolled.

        The guard moves in the directions 'N', 'E', 'S', 'W' (clockwise order).
        If the guard encounters a wall ('#'), it turns 90 degrees to the right.
        The simulation ends when the guard exits the grid.

        Parameters
        ----------
        mapped_area : list of str
            The grid (2D area) where the guard patrols.

        Returns
        -------
        int
            The total number of distinct spots visited by the guard during the patrol.
        """
        rows, cols = len(mapped_area), len(mapped_area[0])

        # Find the initial position of the guard
        gx, gy = self.find_guard_position(mapped_area)

        # Directions: North, East, South, West (clockwise)
        directions = ['N', 'E', 'S', 'W']
        direction = 0 # Start facing North
        
        # Set to keep track of visited positions
        patrolled = set()

        # Simulate the guard's movement until it exits the grid
        while 0 <= gx < rows and 0 <= gy < cols:
            patrolled.add((gx, gy)) # Mark the current position as visited

            # Move based on the current direction
            if directions[direction] == 'N':
                # If a wall is encounted, turn 90 degrees to the right
                if 0 <= gx - 1 < rows and mapped_area[gx-1][gy] == '#':
                    direction = (direction + 1) % 4
                else:
                    gx -= 1
            elif directions[direction] == 'E':
                if 0 <= gy + 1 < cols and mapped_area[gx][gy+1] == '#':
                    direction = (direction + 1) % 4
                else:
                    gy += 1
            elif directions[direction] == 'S':
                if 0 <= gx + 1 < rows and mapped_area[gx+1][gy] == '#':
                    direction = (direction + 1) % 4
                else:
                    gx += 1
            else: # West direction
                if 0 <= gy - 1 < cols and mapped_area[gx][gy-1] == '#':
                    direction = (direction + 1) % 4
                else:
                    gy -= 1

        return len(patrolled)

    def part2(self, mapped_area):
        """
        Simulate the guard's patrol and find the number of spots where the guard gets stuck in a loop.

        The guard moves in the directions 'N', 'E', 'S', 'W' (clockwise order).
        If the guard encounters a wall ('#'), it turns 90 degrees to the right.
        The simulation ends when the guard exits the grid.

        Parameters
        ----------
        mapped_area : list of str
            The grid (2D area) where the guard patrols.

        Returns
        -------
        int
            The total number of spots where the guard gets stuck in a loop.
        """
        # Using the same logic as part 1, we find the number of distinct patrolled spots
        rows, cols = len(mapped_area), len(mapped_area[0])

        gx, gy = self.find_guard_position(mapped_area)

        directions = ['N', 'E', 'S', 'W']
        direction = 0

        patrolled = set()

        while 0 <= gx < rows and 0 <= gy < cols:
            patrolled.add((gx, gy))

            if directions[direction] == 'N':
                if 0 <=  gx - 1 < rows and mapped_area[gx-1][gy] == '#':
                    direction = (direction + 1) % 4
                else:
                    gx -= 1
            elif directions[direction] == 'E':
                if 0 <= gy + 1 < cols and mapped_area[gx][gy+1] == '#':
                    direction = (direction + 1) % 4
                else:
                    gy += 1
            elif directions[direction] == 'S':
                if 0 <= gx + 1 < rows and mapped_area[gx+1][gy] == '#':
                    direction = (direction + 1) % 4
                else:
                    gx += 1
            else:
                if 0 <= gy - 1 < cols and mapped_area[gx][gy-1] == '#':
                    direction = (direction + 1) % 4
                else:
                    gy -= 1
        # End of part 1 logic implementation

        # By the end of this simuation, (gx, gy) don't point to guard's start position anymore.

        totalLoopSpots = 0 # Initialize the count of loop spots (spots where, if obstacle is placed, guard gets stuck in a loop)
        for position in patrolled:
            startX, startY = self.find_guard_position(mapped_area) # Find the guard's start position
            posX, posY = position # Get the position where obstacle is to be placed

            if posX == startX and posY == startY: # If the obstacle is placed at the guard's start position, we skip it
                continue
            mapped_area[posX] = mapped_area[posX][:posY] + '#' + mapped_area[posX][posY+1:] # Place the obstacle at the given position
            direction = 0 # Note: the list 'directions' was not changed during previous simulation, hence we don't define it again
            
            patrolStates = set() # Set to keep track of visited states with their directions this time
            noLoop = True # Flag to check if loop is detected

            while 0 <= startX < rows and 0 <= startY < cols:
                state = (startX, startY, direction) # Store the current state of the guard

                if state in patrolStates: # Loop detected
                    noLoop = False # Set the flag to False
                    break

                patrolStates.add(state) # Add the current state to the set

                if directions[direction] == 'N':
                    if 0 <= startX - 1 < rows and mapped_area[startX-1][startY] == '#':
                        direction = (direction + 1) % 4
                    else:
                        startX -= 1
                elif directions[direction] == 'E':
                    if 0 <= startY + 1 < cols and mapped_area[startX][startY+1] == '#':
                        direction = (direction + 1) % 4
                    else:
                        startY += 1
                elif directions[direction] == 'S':
                    if 0 <= startX + 1 < rows and mapped_area[startX+1][startY] == '#':
                        direction = (direction + 1) % 4
                    else:
                        startX += 1
                else: # West direction
                    if 0 <= startY - 1 < cols and mapped_area[startX][startY-1] == '#':
                        direction = (direction + 1) % 4
                    else:
                        startY -= 1

            mapped_area[posX] = mapped_area[posX][:posY] + '.' + mapped_area[posX][posY+1:] # Remove the obstacle after simulation (resetting)
            if not noLoop: # If loop is detected, increment the count of loop spots
                totalLoopSpots += 1

        return totalLoopSpots # Return the total number of loop spots

    @staticmethod
    def main():
        """
        Read input from a file, execute the patrol simulation, and print results.

        Input file format:
        - Each line represents a row in the grid.
        - The guard starts at a position marked with '^'.
        - Walls are marked as '#'.
        """
        mapped_area = []

        # Read input from file and construct the grid
        with open("Day 6/input.txt", "r") as f:
            file = f.readlines()

            for line in file:
                line = line.strip()
                mapped_area.append(line)

        # Create an instance of the Day6 class
        Day6_instance = Day6()

        # Part 1: Simulate the patrol and calculate distinct spots
        distinctSpots = Day6_instance.part1(mapped_area)
        print(f"The number of distinct spots the guard patrols is: {distinctSpots}")

        # Part 2: Simulate the patrol and calculate the number of loops
        loopSpots = Day6_instance.part2(mapped_area)
        print(f"The number of spots, that if an obstacle is placed, can loop the guard's patrolling is: {loopSpots}")


if __name__ == '__main__':
    Day6.main()