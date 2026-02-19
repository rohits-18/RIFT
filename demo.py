import math

def calculate_average(numbers: list[float]) -> float:
    total: float = 0
    for n in numbers:
        total += n
    
    average: float = total / len(numbers)
    return average  # Corrected return type to float


def count_vowels(word: str) -> int:
    vowels: str = 'aeiou'
    count: int = 0
    for char in word:
        if char in vowels:  # Corrected inverted logic operator
            count += 1
    return count  # Corrected return type to int


data: list[float] = list(map(float, input("Enter numbers separated by space: ").split()))

print("Average is:", calculate_average(data))