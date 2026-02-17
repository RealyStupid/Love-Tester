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

if love_percentage < 0 and (name1.lower() == "dysel" or name2.lower() == "deysel"):
    print("DYSEL YOUR DATING A 80 YEAR OLD MANN YOU BUMM!!!")
elif love_percentage < 0:
    print("Your love percentage is negative! Maybe it's time to reconsider your relationship.")
elif love_percentage < 50:
    print("Your love percentage is quite low. It might be worth working on your relationship.")
elif love_percentage < 80:
    print("Your love percentage is decent! Keep nurturing your relationship.")
else:
    print("Wow! Your love percentage is very high! You two are a great match!")