def Interest_cal():
    print("this is a monthly interest calculator")
    print("")

    principle = float(input("enter the principle amount :"))
    rate = float(input("enter the interest rate :"))
    time = float(input("enter the time"))
    amount_of_months = time * 12
    rate_per_month = rate / 1200
    monthly_payments = principle * rate_per_month / \
        (1-(1+rate_per_month)**(-amount_of_months))

    print("the montly interest rate is =", monthly_payments)


Interest_cal()
