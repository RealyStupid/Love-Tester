import random
import time

print("Welcome to the Love Calculator!")

name1 = input("What is your name? ")
name2 = input("What is your lovers name? ")

for i in range(1, 6):
    print(f"Processing Love Value: {i}/5", end="\r", flush=True)
    time.sleep(random.uniform(0.1, 1))

print("\nCalculating love percentage...")

love_percentage = random.randint(-10, 100)

time.sleep(2)

print(f"{name1} and {name2} have a love percentage of {love_percentage}%!")