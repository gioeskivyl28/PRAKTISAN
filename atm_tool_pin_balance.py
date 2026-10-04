correct_pin = 4321
balance = 5000
ask1 = int(input("Please enter your 4 digit PIN: "))
ask2 = int(input("Please enter the amount you want to withdraw: "))

if ask1== correct_pin:
    if ask2 <= balance:
        balance -= ask2
        print(f"Transaction successful! Your new balance is {balance}.")
    else:
        print("Insufficient funds for this transaction.")