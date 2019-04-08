import random

from tqdm import tqdm


# Draws and returns a random set of 7 numbers without duplicates.
def draw():
    return random.sample(elements, 7)


def duplicates(seq):
    return len(seq) - len(set(seq))


if __name__ == '__main__':

    maxval = 45  # The maximum number for the lottery
    count = int(1e8)  # How many times the simulation should be run per thread

    elements = range(1, maxval + 1)
    tip = [1, 2, 3, 4, 5, 6]

    print(count, 'draws, Tip: 1,2,3,4,5,6')
    print('Drawing from a pool of 1 -', maxval)

    n = 6

    # (ignore these german notes)
    # 1. Rang = 6 richtige Gewinnzahlen
    # 2. Rang = 5 richtige Gewinnzahlen + Zusatzzahl
    # 3. Rang = 5 richtige Gewinnzahlen
    # 4. Rang = 4 richtige Gewinnzahlen + Zusatzzahl
    # 5. Rang = 4 richtige Gewinnzahlen
    # 6. Rang = 3 richtige Gewinnzahlen + Zusatzzahl
    # 7. Rang = 3 richtige Gewinnzahlen
    # 8. Rang = 0 richtige Gewinnzahlen + Zusatzzahl
    wins = [0] * 8

    for i in tqdm(range(count)):
        numbers = draw()  # Lottery draw

        matches = duplicates(numbers[:-1] + tip)
        bonus = numbers[-1] <= 6

        if bonus:
            if matches == 5:
                wins[6] += 1
            if matches == 4:
                wins[4] += 1
            if matches == 3:
                wins[2] += 1
            else:
                wins[0] += 1
        else:
            if matches == 6:
                wins[7] += 1
            if matches == 5:
                wins[5] += 1
            if matches == 4:
                wins[3] += 1
            if matches == 3:
                wins[1] += 1

    # Print the results
    print("6 Correct Numbers:               ", str(wins[7]), 'wins, or',
          "%.8f" % (float(wins[7]) / float(count) * 100), '%')
    print("5 Correct Numbers + Bonus Number:", str(wins[6]), 'wins, or',
          "%.8f" % (float(wins[6]) / float(count) * 100), '%')
    print("5 Correct Numbers:               ", str(wins[5]), 'wins, or',
          "%.8f" % (float(wins[5]) / float(count) * 100), '%')
    print("4 Correct Numbers + Bonus Number:", str(wins[4]), 'wins, or',
          "%.8f" % (float(wins[4]) / float(count) * 100), '%')
    print("4 Correct Numbers:               ", str(wins[3]), 'wins, or',
          "%.8f" % (float(wins[3]) / float(count) * 100), '%')
    print("3 Correct Numbers + Bonus Number:", str(wins[2]), 'wins, or',
          "%.8f" % (float(wins[2]) / float(count) * 100), '%')
    print("3 Correct Numbers:               ", str(wins[1]), 'wins, or',
          "%.8f" % (float(wins[1]) / float(count) * 100), '%')
    print("Only Bonus Number:               ", str(wins[0]), 'wins, or',
          "%.8f" % (float(wins[0]) / float(count) * 100), '%')
