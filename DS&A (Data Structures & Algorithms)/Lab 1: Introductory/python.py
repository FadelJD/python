stored_name = "achmed"
stored_pass = "123"
correct = False
count = 0
sec_que = "Are you Mr. Ackerman?"

while not correct and count < 3:
    user = input("Enter Username: ")
    password = input("Enter Password: ")

    if user == stored_name and password == stored_pass:
        print("Access Granted!")
        correct = True
    else:
        print("Login Failed")
        count += 1

while not correct:
    ans = input(f"{sec_que} Ans = 'Yes/No' only: ").upper()

    if ans == "Y":
        print("Access Granted!")
        print(f"Your username: {stored_name} & Your password: {stored_pass}")
        print("Successfully sent details to Email!")
        break
    else:
        count = 0

while True:
    bank = input("Enter bank type: 'same' OR 'different' only")
    if bank in ["same", "different"]:
        break

amount = float(input("Enter amount: "))

if bank == "same":
    fee_total = amount * 0.01 if amount > 10000 else 0
else:
    fee_total = 50 + amount * 0.01

print(f"For your total amount = {amount} and your total fee = {fee_total}")

cust_type = input("Enter the type of customer you are: 'preferred' OR 'regular'").lower()
order_price = float(input("Enter the price of items that you ordered (Total): "))
charge_card = input("Did you use a charge card: (Y/N) only ").upper() == "Y"

if cust_type == "preferred":
    if order_price > 1000:
        bonus_coup = 0
        fin_price = order_price * 0.95
        if charge_card:
            fin_price *= 0.95
    elif 0 < order_price <= 1000:
        bonus_coup = 25
        fin_price = order_price
else:
    bonus_coup = 5
    fin_price = order_price

print(f"Your FinPrice = {fin_price} with a bonus coupon of: {bonus_coup}")
