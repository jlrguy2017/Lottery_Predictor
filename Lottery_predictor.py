import random

# Historical winning numbers
winning_numbers = [
    [5, 45, 55, 58, 68, 7],
    [19, 23, 39, 42, 67, 18],
    [1, 3, 19, 25, 58, 20],
    [17, 22, 29, 46, 69, 1],
    [2, 10, 31, 44, 57, 10],
    [11, 22, 42, 64, 69, 18],
    [3, 5, 16, 58, 59, 11],
    [14, 31, 34, 50, 61, 13],
    [21, 28, 58, 69, 70, 20],
    [1, 9, 16, 17, 30, 17],
    [2, 10, 42, 49, 54, 13],
    [19, 34, 35, 45, 67, 7],
    [12, 15, 32, 33, 53, 24],
    [5, 23, 26, 38, 44, 25],
    [3, 18, 27, 29, 64, 1],
    [11, 27, 30, 62, 70, 10],
    [8, 10, 22, 58, 64, 21],
    [10, 26, 36, 54, 69, 4],
    [17, 26, 50, 58, 61, 11],
    [10, 20, 28, 40, 54, 12]
]

# Calculate frequency of each number in the main draw and Powerball
main_draw_frequency = {}
powerball_frequency = {}

for numbers in winning_numbers:
    main_draw, powerball = numbers[:-1], numbers[-1]
    for number in main_draw:
        main_draw_frequency[number] = main_draw_frequency.get(number, 0) + 1
    powerball_frequency[powerball] = powerball_frequency.get(powerball, 0) + 1

# Function to select numbers based on their frequency
def select_by_frequency(frequency_dict, num_to_pick, selection_pool_size):
    # Sort the numbers by frequency and take the top N for the selection pool
    sorted_by_frequency = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
    selection_pool = [number for number, frequency in sorted_by_frequency[:selection_pool_size]]

    # Randomly pick numbers from the selection pool
    return sorted(random.sample(selection_pool, num_to_pick))

# Generate 3 sets of lottery numbers based on frequency analysis
def generate_frequency_based_sets(num_sets=3):
    for _ in range(num_sets):
        main_numbers = select_by_frequency(main_draw_frequency, 5, 20)  # Select from the top 20 most frequent for variability
        powerball = select_by_frequency(powerball_frequency, 1, 10)[0]  # Select from the top 10 for the Powerball
        print(f"Main numbers: {main_numbers}, Powerball: {powerball}")

# Generate and print 3 sets of lottery numbers
generate_frequency_based_sets(3)
