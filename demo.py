import math

def calculate_average(numbers: list[float]) -> float:
    total: float = 0
    for n in numbers:
        total += n
    
    average: float = total / len(numbers)
    return average


data: list[float] = list(map(float, input("Enter numbers separated by space: ").split()))

print("Average is:", calculate_average(data))