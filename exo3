TA = float(input("Total amount: "))
if TA <= 0:
    exit("Total amount can't be negative !!")

nb_i = int(input("Number of items: "))
if nb_i <= 0:
    exit("Number of items can't be negative !!")

Day = input("Day of the week: ").lower()
weekDays = ["monday", "thursday", "wednesday", "tuesday", "friday"]
weekEnds = ["saturday", "sunday"]

if Day not in weekDays + weekEnds:
    exit("Invalid Day !!!!!!!")

dis = 0.2 if Day in weekEnds else 0.1
if nb_i > 5:
    dis += 0.05

print("Total price after discount: ", TA * (1 - dis), " dinars")
