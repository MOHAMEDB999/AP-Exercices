numbers = [1, 2, 3, 4, 5]

while True:
    index = int(input("Enter index (-1 to quit): "))

    if index == -1:
        break

    if 0 <= index < len(numbers):
        new_value = int(input("Enter new value: "))
        numbers[index] = new_value
        print(numbers)
    else:
        print("Invalid index. Try again.")

print("Program terminated.")
