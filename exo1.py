ismok = input("Please enter your name: ")

if ismok == "VIP":
    print("Enjoy the show for free!")
else:
    tickets = int(input("How many tickets would you like to buy? "))
    ticketprix = 15.50
    price_total = tickets * ticketprix
    print(f"The total cost is {price_total}")
    print("Enjoy your tickets!")
