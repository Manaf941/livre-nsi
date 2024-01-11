import random
import math

number = random.randint(0, 100)

print("Devine le nombre !")
while True:
    guess = int(input(""))
    if math.isnan(guess):
        print("Nombre invalide")
        pass
    
    if guess > number:
        print("plus petit")
    elif guess < number:
        print("plus grand")
    else:
        print("Gagné!")
        break