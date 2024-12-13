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
            print(middleSum)


if __name__ == "__main__":
    Day5.main()