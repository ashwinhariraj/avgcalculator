def calculate_average(numbers):
    if not numbers:
        print("Error: The list is empty!")
        return None
    
    total = 0
    for num in numbers:
        try:
            total += float(num)
        except ValueError:
            print(f"Error: {num} is not a valid number!")
            return None  
    
    average = total / len(numbers)
    return average

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [1, 2, 'a', 4]
numbers3 = []
numbers4 = [1, 2, 3.5, 4]

print(f"Average of numbers1: {calculate_average(numbers1)}")
print(f"Average of numbers2: {calculate_average(numbers2)}")
print(f"Average of numbers3: {calculate_average(numbers3)}")
print(f"Average of numbers4: {calculate_average(numbers4)}")
