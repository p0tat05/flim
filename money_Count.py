
def money(quant:float, currency:float) -> float:
    total = quant * currency  
    return total
    

#Coins (CAD)
penny = 0.01
nickle = 0.05
dime = 0.10
quarter = 0.25
loonie = 1.00
toonie = 2.00

#Bills (CAD)
five_bill = 5.00
ten_bill = 10.00
twenty_bill = 20.00
fifty_bill = 50.00
hund_bill = 100.00

currency: float = [penny, nickle, dime, quarter, loonie, toonie, five_bill, ten_bill, twenty_bill, fifty_bill, hund_bill]

Check: bool = True
running: bool = True
total_amount: float = 0.0
total:float = 0.0

print("Options")
print("1. Calculate the amount of money you have.\n2.how many bills can you get.")

while Check:
    try:
        opt = int(input("Enter your option: "))
        if (opt == 1 or opt == 2):
            Check = False
        else:
            print("Enter new value!")
    except ValueError:
        print("Value error")


if (opt == 1):
    print("list the amount collected (CAD)")
    for runs in range(len(currency)):
        while running:
            amount = input(f"Enter amount ${currency[runs]} you have: ")
            if (amount.isdigit()):
                amount = float(amount)
                running = False
            else:
                print("Try another value")
        running = True
        total_amount = money(amount, currency[runs])

        total += total_amount

    while running:
        online_money = input("Enter amount in online bank: ")
        if (online_money.isdigit()):
            online_money = float(online_money)
            running = False
        else:
            print("Enter valid amount!")

    total_money = total + online_money

    print(f"You have $ {total:.2f} in cash")
    print(f"and ${online_money:.2f} online")
    print(f"You have $ {total_money:.2f}")

if (opt == 2):
    while running:
        base_value = input("Enter your total value: $")
        if base_value.isdigit():
            base_value = float(base_value)
            running = False
        else:
            print("Enter a valid value")

    print(f"Your total is ${base_value}")
    print("optinons:")
    print(" 1. penny\n 2. nickle\n 3. dime\n 4. quarter\n 5. loonie\n 6. toonie\n 7. $5 bill\n 8. $10 bill\n 9. $20 bill\n 10. $50 bill\n 11. $100 bill")

    Check = True

    while Check:
        curr = input("Enter your option: ")

        if (curr.isdigit()):
            curr = int(curr)
            if (curr <= len(currency) and curr > 0):
                Check = False
            
        else:
            print("Enter a proper value.")

    

    Bills = float(base_value / currency[curr-1])

    print(f"You will get {Bills:.0f}, ${currency[curr-1]} bills with ${base_value}")

