name = input("What is your name?")
age = int(input(f"How old are you,{name}? "))
height = float(input("What is your height in centimeters? "))

if height >= 120:
    print("You are tall enough to ride the roller coaster.")
    if age < 12:
        ask = input("Do you have an adult with you? ")
        if ask =="Yes":
            print("You can ride the roller coaster, enjoy!")
        else:
            print("Sorry, you cannot ride the roller coaster without an adult.")
    if age>= 12:
        ask1 = input("Do you have a health condition that prevents riding? (Yes/No): ")
        if ask1 == "Yes":
            print("Sorry, it can be dangerous for your health.")
        else:
            print(f"Enjoy the ride {name}!")
