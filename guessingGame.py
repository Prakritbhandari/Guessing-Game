import random

rand = random.randint(1,9)
chanceUsed = 0

while chanceUsed<5 :
    guess = int(input("Guess A number between 1 and 9"))
    if guess == rand:
        print("Congratulations you have won")
        break
    elif guess < rand:
        print("Your guess was too low guess a higher number ",guess)
    else :
        print("Your guess was too high guess a lower number ",guess)
    chanceUsed = chanceUsed+1

if not chanceUsed<5 :
    print ("You Lose the number is ",rand)