def add(a, b):
    sum = a+b
    print(str(a) + " + "+str(b) + " = "+str(sum))


def sub(a, b):
    sum = a-b
    print(str(a) + " + " + str(b) + " = " + str(sum))


def div(a, b):
    sum = a/b
    print(str(a) + " + " + str(b) + " = " + str(sum))


def mult(a, b):
    sum = a*b
    print(str(a) + " + " + str(b) + " = " + str(sum))


def mod(a, b):
    sum = a % b
    print(str(a) + " + " + str(b) + " = " + str(sum))


print("A. ADDITION")
print("B. SUBTRACTION")
print("C. DIVISION")
print("D. MULTIPLICATION")
print("E. MODULUS")
x = input("Enter you choice: ")
if (x == 'a' or x == 'A'):
    a = int(input("enter the number 1 : "))
    b = int(input("enter the number 2 : "))
    add(a, b)
elif (x == 'b' or x == 'B'):
    a = int(input("enter the number 1 : "))
    b = int(input("enter the number 2 : "))
    sub(a, b)
elif (x == 'c' or x == 'C'):
    a = int(input("enter the number 1 : "))
    b = int(input("enter the number 2 : "))
    div(a, b)
elif (x == 'd' or x == 'D'):
    a = int(input("enter the number 1 : "))
    b = int(input("enter the number 2 : "))
    mult(a, b)
elif (x == 'e' or x == 'E'):
    a = int(input("enter the number 1 : "))
    b = int(input("enter the number 2 : "))
    mod(a, b)
else:
    print("wrong choice")
