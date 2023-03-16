import random


def dice_roll():

    dice_drawing = {
        1: (
            "---------",
            "|   1   |",
            "|   *   |",
            "---------",
        ),
        2: (
            "---------",
            "|   2   |",
            "|   **  |",
            "---------",
        ),
        3: (
            "---------",
            "|   3   |",
            "|  ***  |",
            "---------",
        ),
        4: (
            "---------",
            "|   4   |",
            "| ****  |",
            "---------",
        ),
        5: (
            "---------",
            "|   5   |",
            "| ***** |",
            "---------",
        ),
        6: (
            "---------",
            "|   6   |",
            "|   VI  |",
            "---------",
        )
    }
    roll = input("roll dice (YES / NO): ")
    while roll.lower() == "YES".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        print("dice rolled: {} and {}".format(dice1, dice2))

        roll = input("roll again? (yes/no) :")


dice_roll()
