# TAX PROGRAM
#  1) CAD
#  2) ANY OTHER TAX %

def adding_tax(price, tax):
    final_price = (1+tax/100)*price
    return final_price

print("ADDING TAX PROGRAM")
print("1. Canada\n2. other")
choice = int(input("Enter your choice: "))

if choice == 1:
    tax = 13
    print("The Canadian tax is 13% sales tax")
    price = float(input("Enter your price: $"))

    taxed_price = round(adding_tax(price, tax),ndigits=2)

    print(f"your final price is ${taxed_price}")

if choice == 2:
    tax = int(input(f"Enter tax %: "))  # ENTER  A WHOLE NUMBER
    print(f"Tax = {tax}")
    price = float(input("Enter your price: $"))

    taxed_price = round(adding_tax(price=price, tax=tax), ndigits=2)

    print(f"your final taxed price with {tax}% tax is {taxed_price}")