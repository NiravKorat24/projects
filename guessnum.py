import random

def chose_num():
    num = random.randint(1,100)

def guess_num():
    num = chose_num()
    while True:
        your_num = int(input(f"guess a number between 1 and 100: "))
        if your_num == num:
            print("Congratulations! You guessed the number.")
            break
        elif your_num < num:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == '__main__':   
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    chose_num()
    guess_num()         
    