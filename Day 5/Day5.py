from collections import defaultdict
class Day5:
    def part1(self, rules, updates):
        middleSum = 0

        for update in updates:
            idx = {}
            correct = True
            n = len(update)
            # print(update)
            for i, num in enumerate(update):
                idx[num] = i

            for a, b in rules:
                if a in idx and b in idx:
                    if idx[a] > idx[b]:
                        correct = False
                        break

            if correct:
                middleSum += update[n//2]

        return middleSum
    
    def part2(self, rules, updates):
        totalMidSum = 0 # the total mid sum of the incorrect updates after correctly ordering them

        for update in updates:
            n = len(update)

            # filtering out rules as per the current update
            current_rules = []
            for a, b in rules:
                if a in update and b in update:
                    current_rules.append((a, b))

            # finding the indegrees of each number in the update (to find number of dependencies for each page, if any)
            indeg = defaultdict(int)
            for a, b in current_rules:
                indeg[b] += 1

            # finding the correct order of the update
            correct_order = []

            while len(correct_order) < len(update):
                for x in update:
                    if x in correct_order:
                        continue
                    if indeg[x] <= 0:
                        correct_order.append(x)
                        for a, b in current_rules:
                            if a == x:
                                indeg[b] -= 1

            # finding the mid sum of the correct orders
            totalMidSum += correct_order[n//2]
            

        return totalMidSum

    @staticmethod
    def main():
        with open("Day 5/input.txt", "r") as f:
            raw_rules, raw_updates = f.read().split("\n\n")
            rules = []

            for rule in raw_rules.split("\n"):
                num1, num2 = rule.split("|")
                rules.append((int(num1), int(num2)))

            raw_updates = raw_updates.split("\n")
            updates = []

            for update in raw_updates:
                temp = update.split(",")
                updates.append(list(map(int, temp)))

            Day5_instance = Day5()

            middleSum = Day5_instance.part1(rules, updates)
            print(f"Middle sum of the correct updates: {middleSum}")

            totalMidSum = Day5_instance.part2(rules, updates) - middleSum
            print(f"Middle sum of the incorrect updates, after correction: {totalMidSum}")


if __name__ == "__main__":
    Day5.main()