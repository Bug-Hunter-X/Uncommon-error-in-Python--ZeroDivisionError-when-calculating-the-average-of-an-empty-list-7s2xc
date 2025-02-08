def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0  # Handle empty list
    average = total / count
    return average

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")