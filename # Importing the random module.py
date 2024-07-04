# Importing the random module
import random

# 1. choice(): Returns a random element from the given sequence
colors = ['red', 'green', 'blue', 'yellow']
random_color = random.choice(colors)
print(f"Random color chosen: {random_color}")

# 2. sample(): Returns a specified number of unique elements randomly chosen from the sequence
random_samples = random.sample(range(1, 10), 3)
print(f"Random samples: {random_samples}")

# 3. randint(): Returns a random integer between the specified range (inclusive)
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")

# 4. shuffle(): Shuffles the elements of a sequence in place
deck_of_cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
random.shuffle(deck_of_cards)
print(f"Shuffled deck of cards: {deck_of_cards}")
