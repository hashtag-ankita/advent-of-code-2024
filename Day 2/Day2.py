class Day2:
    def part1(self, reports):
        """
        Method to calculate the total number of safe reports, given a list of reports, each report being a list of integers.
        A report is considered safe if it satisfies two conditions: 
        1. The list of integers is in increasing or decreasing order.
        2. The difference between any two consecutive numbers is either 1, 2, or 3.
        The method iterates over all the reports and checks for the above two conditions. If a report satisfies both
        conditions, it is considered as a safe report and the count of safe reports is incremented by 1. The method finally
        returns the total number of safe reports.
        :param reports: A list of lists of integers.
        :return: Total number of safe reports.
        """
        numOfSafeReports = 0 # Initialize a variable to count the number of safe reports
        check = False # Flag to determine if a report is safe based on the conditions

        for report in reports:
            # first check: increasing or decreasing?
            # Skip the report if it is neither increasing nor decreasing
            if report != sorted(report) and report != sorted(report, reverse=True):
                continue

            # second check: difference lies between [1, 2, 3]?
            numOfLevels = len(report) # Get the length of the current report
            for i in range(numOfLevels - 1):
                # Check if the consecutive numbers are the same or if their difference is greater than 3
                if (report[i] == report[i+1]) or abs(report[i] - report[i+1]) > 3:
                    check = False # Set check to False if conditions are violated
                    break # Exit the loop early as the report failed the conditions
                else:
                    check = True # If conditions are met, set check to True

            if check: # If all conditions were met, the report is considered safe
                numOfSafeReports += 1 # Increment the safe reports count

        return numOfSafeReports # Return the total number of safe reports

    @staticmethod
    def main():
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
            print(numOfSafeReports) # Print the number of safe reports

if __name__ == "__main__":
    Day2.main() # Call the main function to run the program