numbers = [1, 2, 3, 4, 5]

def display_menu():
    print("\nMenu:")
    print("1. Add an element (at the end of the list) ")
    print("2. Insert an element at a specific position")
    print("3. Delete an element ")
    print("4. Remove an element")
    print("5. Quit")

def main():
    while True:
        print("\nCurrent List:", numbers)
        display_menu()

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            try:
                value = int(input("Enter value to append: "))
                numbers.append(value)
                print("Updated List:", numbers)
            except ValueError:
                print("Invalid input! Please enter an integer.")

        elif choice == 2:
            try:
                value = int(input("Enter value to insert: "))
                index = int(input("Enter index to insert at: "))
                if 0 <= index <= len(numbers):
                    numbers.insert(index, value)
                    print("Updated List:", numbers)
                else:
                    print("Index out of range!")
            except ValueError:
                print("Invalid input! Please enter integers.")

        elif choice == 3:
            try:
                index = int(input("Enter index to pop (or leave blank to pop last): ") or -1)
                popped = numbers.pop(index) if index != -1 else numbers.pop()
                print(f"Popped element: {popped}")
                print("Updated List:", numbers)
            except ValueError:
                print("Invalid input! Please enter an integer.")
            except IndexError:
                print("Index out of range!")

        elif choice == 4:
            try:
                value = int(input("Enter value to remove: "))
                numbers.remove(value)
                print("Updated List:", numbers)
            except ValueError:
                print("Invalid input! Please enter an integer.")
            except ValueError:
                print("Value not found in the list!")

        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option! Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
