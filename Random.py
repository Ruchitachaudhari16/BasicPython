import random

def flip_coin(num_flips):
    # Initialize counters
    heads_count = 0
    tails_count = 0

    # Simulate flipping the coin num_flips times
    for _ in range(num_flips):
        if random.random() < 0.5:
            tails_count += 1
        else:
            heads_count += 1

    # Calculate percentages
    heads_percentage = (heads_count / num_flips) * 100
    tails_percentage = (tails_count / num_flips) * 100

    # Return the calculated percentages
    return heads_percentage, tails_percentage

# Main logic to execute the coin flip simulation
try:
    num_flips = int(input("Enter the number of times to flip the coin: "))
    if num_flips <= 0:
        raise ValueError("Number of flips must be a positive integer.")
    
    heads_percentage, tails_percentage = flip_coin(num_flips)
    print(f"Heads: {heads_percentage:.2f}%")
    print(f"Tails: {tails_percentage:.2f}%")
except ValueError as e:
    print(e)
