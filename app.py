import random

num = random.randint(1,9)
guess = 0
count = 0

while guess != num and guess != 'exit':
    guess = input("Pick a number ")

    if guess == 'exit':
        break

    guess = int(guess)
    count += 1

    if guess  < num:
        print("No, too low. ")
    elif  guess > num:
        print("No, too high.")
    else:
        print("BINGO!")
        print("And it only too you", count, "tries.")