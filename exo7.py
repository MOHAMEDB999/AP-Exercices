print("this is a program that checks whether a given year is a leap year")
year = float(input("please enter a year : "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("yes its good year")
else:
    print("its not good year")
