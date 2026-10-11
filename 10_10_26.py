height = int(input("How tall are you in cm? ")) #the height needed to be 120 and above

if height >= 120:
    age = int(input("How old are you? ")) #age needed to be 12 and above
    if age >= 12:
        if age < 14:
            ask = input("Do you have a adult with you? (y or n)").lower()
            if ask == "y":
                print("Enjoy the ride!")
            else:
                print("Sorry you cannot ride, you must have a parent or guardian.")
        else:
            print("Enjoy the ride!")
    else:
        print("You're too young")
else:
    print("Haha you're too short,please watch kai sotto ginulat ang munggo.")