import random
my_random_number = random.randint(1, 10)
print("I'm thinking of a number between 1 and 10.")
while True:
    guess = int(input("what's the number? "))
    if guess == my_random_number:
        print("Yes! You win!")
        break
    else:
        print("nope, try again.")