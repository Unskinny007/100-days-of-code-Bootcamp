print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")

    want_photo = input("Do youw want to have a photo take? Type y for yes or n for no: ")
    if want_photo == "y":
        bill += 3

    print(f"You final bills is ${bill} ")
else:
    print("Sorry you have to grow taller before you can ride.")
