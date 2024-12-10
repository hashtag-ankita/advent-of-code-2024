class Day2:
    def is_safe(self, report):
        '''Determines if a given report is "safe" (i.e., strictly increasing or decreasing and with differences between consecutive elements of 1, 2, or 3).'''
        if len(report) < 2: # A single element or empty report is trivially "safe"
            return True

        # first check: increasing or decreasing?
        # Skip the report if it is neither increasing nor decreasing
        if report != sorted(report) and report != sorted(report, reverse=True):
            return False

        # second check: difference lies between [1, 2, 3]?
        for i in range(len(report)-1):
            if not 1 <= abs(report[i+1] - report[i]) <= 3:
                return False
        
        return True

    def part1(self, reports):
        '''
        Calculate the total number of safe reports from a given list of reports.

        Reports are considered "safe" if they are strictly increasing or decreasing and
        with differences between consecutive elements of 1, 2, or 3.

        Parameters
        ----------
        reports : list
            A list of reports, each of which is a list of integers.

        Returns
        -------
        int
            The total number of safe reports.
        '''
        numOfSafeReports = 0 # Initialize a variable to count the number of safe reports

        for report in reports:
            if self.is_safe(report): # If all conditions were met, the report is considered safe
                numOfSafeReports += 1 # Increment the safe reports count

        return numOfSafeReports # Return the total number of safe reports

    def part2(self, reports):
        '''
        Calculate the total number of safe reports from a given list of reports.

        Reports are considered "safe" if they are strictly increasing or decreasing and
        with differences between consecutive elements of 1, 2, or 3. If a report is not
        safe, then it is considered safe if any single element is removed from it.

        Parameters
        ----------
        reports : list
            A list of reports, each of which is a list of integers.

        Returns
        -------
        int
            The total number of safe reports.
        '''
        totalSafeReports = 0 # Initialize a variable to count the total safe reports

        for report in reports:
            if self.is_safe(report): # Check if the entire report is safe
                totalSafeReports += 1
            else:
                # Attempt to fix the report by removing one element at a time
                for i in range(len(report)):
                    # Check if removing the i-th element results in a safe subreport
                    if self.is_safe(report[:i] + report[i+1:]):
                        totalSafeReports += 1
                        break # Stop further checks for this report as it is now considered safe

        return totalSafeReports # Return the total number of safe reports
            

    @staticmethod
    def main():
        """
        Main method to read reports from an input file, process them to determine the number of safe reports,
        and print the results. Reports are considered "safe" if they are strictly increasing or decreasing
        with differences between consecutive elements of 1, 2, or 3. If not initially safe, reports can be
        considered safe by removing one element.

        This method reads the input data from "Day 2/input.txt", creates an instance of the Day2 class,
        and utilizes the part1 and part2 methods to calculate and display the number of safe reports.

        The results are printed to the console, showing the number of safe reports and the total number
        of safe reports after applying a problem dampening technique.
        """
        reports = [] # Initialize an empty list to store the reports

        with open("Day 2/input.txt", "r") as f:
            file = f.readlines() # Read all lines from the file

            for report in file:
                report = report.split() # Split the report line into individual numbers (as strings)
                report = [int(num) for num in report] # Convert the strings to integers
                reports.append(list(report)) # Append the processed report to the reports list

            Day2_instance = Day2() # Create an instance of the Day2 class

            # Call the part1 method to get the number of safe reports
            numOfSafeReports = Day2_instance.part1(reports)

            totalNumOfSafeReports = Day2_instance.part2(reports)

            print("The number of Safe reports are: ", numOfSafeReports) # Print the number of safe reports
            print("Due to Problem Dampener, the total number of Safe reports are: ", totalNumOfSafeReports)

if __name__ == "__main__":
    Day2.main() # Call the main function to run the program