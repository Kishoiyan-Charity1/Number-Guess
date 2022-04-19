import random

random_number = random.randint(1, 10) 

guess_number = 0

while guess_number_!= random_number:
    guess_number = int(input("Please guess a number between 1 and 10: "))

    if(random_number < guess_number):
        print("The number is smaller than your number")
        elif(random_number > guess_number):
            print("The number is greater than your number")
        else:
            print("This is the number!") 