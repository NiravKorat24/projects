import random

def play_game():

    print("Welcome to the Math Quiz!")
    yourscorcard = 0
    for i in range(5):
        print(f"round {i+1}") 
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        ans = num1 + num2
        yourans = int(input(f"what is the sum of {num1} and {num2}? "))

        if yourans == ans:
            print("Correct!")
            yourscorcard += 1
        else:
            print(f"Wrong! The correct answer is {ans}.")

    print(f"your final scorecard is {yourscorcard} /5.")

if __name__ == '__main__':
    play_game()
