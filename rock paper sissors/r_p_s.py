import random


def main():
    exit = False
    user_points = 0
    comp_points = 0
    while (exit == False):
        options = ["rock", "paper", "scissors"]
        user_option = input(
            "enter your choice : rock, paper, scissors or exit:")
        computer_option = random.choice(options)

        if (user_option == "exit"):
            print("game ended")
            print("you won a total score of ", user_points,
                  " & computer won a total score of ", comp_points)
            exit = True

        if (user_option == "rock"):
            if (computer_option == "rock"):
                print("user input is rock")
                print("computer input is rock")
                print("its a tie")
            elif (computer_option == "paper"):
                print("user input is rock")
                print("comp input is paper")
                print("computer has won")
                comp_points += 1
            elif (computer_option == "scissors"):
                print("user input is rock")
                print("comp input is scissors")
                print("user has won")
                user_points += 1
        elif (user_option == "paper"):
            if (computer_option == "rock"):
                print("user input is paper")
                print("computer input is rock")
                print("user has won")
                user_points += 1
            elif (computer_option == "paper"):
                print("user input is paper")
                print("comp input is paper")
                print("its a tie")
            elif (computer_option == "scissors"):
                print("user input is paper")
                print("comp input is scissors")
                print("computer has won")
                comp_points += 1
        elif (user_option == "scissors"):
            if (computer_option == "rock"):
                print("user input is scissors")
                print("computer input is rock")
                print("computer has won")
                comp_points += 1
            elif (computer_option == "paper"):
                print("user input is scissors")
                print("comp input is paper")
                print("user has won")
                user_points += 1
            elif (computer_option == "scissors"):
                print("user input is scissors")
                print("comp input is scissors")
                print("it is a tie")
        if (user_option != "rock" or user_option != "paper" or user_option != "scissors" or user_option != "exit"):
            print("invalid input")


main()
