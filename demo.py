import math

def calculate_average(numbers: list[float]) -> float:
    total: float = 0
    for num in numbers:
        total += num
    
    average: float = total / len(numbers)
    return average


data: list[str] = input("Enter numbers separated by space: ").split()

print("Average is:", calculate_average(data))