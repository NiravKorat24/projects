import random
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except RuntimeError:
        print("[Warning] Speech engine is busy.")

def play_game():
    choices = ['rock', 'paper', 'scissors']
    your_score = 0
    robot_score = 0

    print("Welcome to the Rock, Paper, Scissors game")
    print("Enter 'stop' to exit the game.\n")
    speak("Welcome to the Rock, Paper, Scissors game. Enter stop to exit the game.")

    for i in range(5):
        print(f"\nRound {i + 1}")
        print(f"Score - You: {your_score}, Robot: {robot_score}")
        your_choice = input("Choose rock, paper, or scissors: ").lower()

        if your_choice == "stop":
            print("\nGame is stopped.")
            speak("Game is stopped.")
            print(f"Final score - You: {your_score}, Robot: {robot_score}")
            if your_score > robot_score:
                print("You won the game!")
                speak("You won the game.")
            elif your_score < robot_score:
                print("You lost the game.")
                speak("You lost the game.")
            else:
                print("It's a tie.")
                speak("It's a tie.")
            break

        if your_choice not in choices:
            print("Invalid choice! Try again.")
            continue

        robot_choice = random.choice(choices)
        print(f"\nYou chose: {your_choice}")
        print(f"Robot chose: {robot_choice}")

        if (your_choice == "rock" and robot_choice == "scissors") or (your_choice == "paper" and robot_choice == "rock") or (your_choice == "scissors" and robot_choice == "paper"):
           
            print("You win this round!\n")
            speak("You win this round!")
            your_score += 1
        elif your_choice == robot_choice:
            print("It's a tie!\n")
            speak("It's a tie.")
        else:
            print("Robot wins this round!\n")
            speak("Robot wins this round.")
            robot_score += 1

if __name__ == "__main__":
    play_game()
