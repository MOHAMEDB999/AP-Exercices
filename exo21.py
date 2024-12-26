def length(lst):

    if not isinstance(lst, list):
        raise TypeError("Input must be a list of numbers.")
    return len(lst)

def mean(lst):

    if not isinstance(lst, list):
        raise TypeError("Input must be a list of numbers.")
    if not lst:
        return None
    return sum(lst) / len(lst)

def range_of_list(lst):

    if not isinstance(lst, list):
        raise TypeError("Input must be a list of numbers.")
    if not lst:
        return 0
    return max(lst) - min(lst)

def standard_deviation(data):


    if not isinstance(data, list):
        raise TypeError("Input must be a list of numbers.")
    n = len(data)
    if n < 2:
        print("Standard deviation requires at least two data points.")
        return None
    
    mean_value = mean(data)
    variance = sum((x - mean_value) ** 2 for x in data) / (n - 1)  # Sample variance
    return variance ** 0.5

test_cases = {
    "Test Case 1 (Empty list)": [],
    "Test Case 2 (Negative and positive numbers)": [-3, -2, -4, 1, 2, 3],
    "Test Case 3 (Floating-point numbers)": [0.5, 0.5, 0.6, 0.3],
    "Test Case 4 (Single element)": [2]
}

for description, lst in test_cases.items():
    print(f"\n{description}: {lst}")
    try:
        print(f"Length: {length(lst)}")
        print(f"Mean: {mean(lst)}")
        print(f"Range: {range_of_list(lst)}")
        print(f"Standard Deviation: {standard_deviation(lst)}")
    except Exception as e:
        print(f"Error: {e}")
