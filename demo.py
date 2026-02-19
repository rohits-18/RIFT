def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    
    average = total / len(numbers)
    return average


data = input("Enter numbers separated by space: ").split()

print("Average is:", calculate_average(data))
