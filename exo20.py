
def write_list_to_file(numbers_list, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write(' '.join(map(str, numbers_list)) + '\n')
        print(f"Successfully wrote the list to '{file_path}'.")
    except Exception as error:
        print(f"An error occurred while writing to the file: {error}")

def calculate_mean(numbers_list):
    return sum(numbers_list) / len(numbers_list)

def calculate_median(sorted_list):
    list_length = len(sorted_list)
    if list_length % 2 == 1:
        return sorted_list[list_length // 2]
    else:
        mid1, mid2 = sorted_list[(list_length // 2) - 1], sorted_list[list_length // 2]
        return (mid1 + mid2) / 2

def main():
    numbers = []
    while True:
        try:
            user_input = int(input("Enter a number [0 to exit]: "))
            if user_input != 0:
                numbers.append(user_input)
                print(f"Current list: {numbers}")
                ascending_numbers = sorted(numbers)
                descending_numbers = sorted(numbers, reverse=True)
                print(f"Sorted list in ascending order: {ascending_numbers}")
                print(f"Sorted list in descending order: {descending_numbers}")
            else:
                print("Finished looping.")
                break
        except ValueError:
            print("Input must be an integer.")

    if numbers:
        mean_value = calculate_mean(numbers)
        ascending_numbers = sorted(numbers)
        median_value = calculate_median(ascending_numbers)

        print(f"\nSummary:")
        print(f"Mean: {mean_value}")
        print(f"Median: {median_value}")

        save_decision = input("Do you want to save the list to a file? [y/n]: ").strip().lower()
        if save_decision == "y":
            file_path = input("Enter a file path: ").strip()
            write_list_to_file(numbers, file_path)
    else:
        print("No numbers were entered.")

if __name__ == "__main__":
    main()
