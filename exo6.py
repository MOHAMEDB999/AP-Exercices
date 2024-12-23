prix = float(input("Please type in a price: "))
if prix < 0 :
    print("the price cannot be negative ")
    exit()
dinar = int(prix)
centime = round((prix - dinar) * 100)

print(f"Dinars: {dinar}")
print(f"Centimes: {centime}")
