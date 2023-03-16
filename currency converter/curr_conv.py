def main():
    print("this is a program to convert Dollars to Pounds:")

    Dollars = float(input("enter the amount in dollars"))

    pounds = convert_dollar(Dollars)

    print("that is", pounds, "pounds.")


def convert_dollar(Dollars): return Dollars * 0.82


main()
