import random

def play_game():
    filed = ['rock', 'paper', 'scissors']
    your_score = 0
    robot_score = 0
    print(" welcome to the Rock, Paper, Scissors game")
    print("Enter 'stop' to exit the game.\n")

    while True:
        print(f"score = your score : {your_score}  and  robot score : {robot_score}")
        your_choice = input("choose rock, paper or scissors : ")

        if your_choice == "stop":
            print("game is stopped")

            print(f"final score : your score : {your_score}  and  robot score : {robot_score}")
            if your_score > robot_score:
                print("you won the game")
            elif your_score < robot_score:
                print("you lost the game")
            else:
                print("it's a tie")
            break

        if your_choice not in filed:
            print("invalid choice! try again.\n")
            continue

        robot_choice = random.choice(filed)
        print(f"\nyou chose : {your_choice}")
        print(f"robot chose : {robot_choice}")

        if (your_choice == "rock" and robot_choice == "scissors") or (your_choice == "paper" and robot_choice == "rock") or (your_choice == "scissors" and robot_choice == "paper"):
            print("you win this round!\n")
            your_score += 1
        elif your_choice == robot_choice:
            print("it's a tie!\n")
        else:
            print("robot wins this round!\n")
            robot_score += 1       


if __name__ == "__main__":  
    play_game()

    