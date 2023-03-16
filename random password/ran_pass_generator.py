import string
import random
characters = list(string.ascii_letters + string.digits + "~!@#$%^&*()_")


def Generate_pass():
    pass_length = int(input("enter the password length: "))
    random.shuffle(characters)

    password = []
    for x in range(pass_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)


options = input("Do you want to generate a password (YES / NO) ? ")
if (options == 'YES'.lower()):
    Generate_pass()
elif (options == 'NO'.lower()):
    print("The Program has ended.")
    quit()
else:
    print("Invalid input choose yes or no. ")
    quit()
