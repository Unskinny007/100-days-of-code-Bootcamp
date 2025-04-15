print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("you can ride a rollercoster")
    age = int(input("What is your age?: "))
    if age <=12:
        print("Please pay 5$")
    elif age <=18:
        print("Please pay 7$")
    else:
        print("You must pay 12$")
else:
    print("sorry yo have to grow taller before you can ride")
