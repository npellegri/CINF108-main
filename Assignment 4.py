# 1. Check if a year is a leap year
def is_leap_year(year: int) -> bool:
    if not isinstance(year, int) or year < 0:
        raise ValueError("Year must be a positive integer")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# 2. Find even numbers in a list
def find_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

# 3. Check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 4. Generate Fibonacci sequence
def fibonacci(n_terms: int) -> list:
    if not isinstance(n_terms, int) or n_terms < 0:
        raise ValueError("Number of terms must be a positive integer")
    if n_terms == 0:
        return []
    sequence = []
    a, b = 0, 1
    for _ in range(n_terms):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# 5. Print names starting with 'A'
def names_starting_with_a(names):
    return [name for name in names if name.startswith("A")]

# 6. Multiplication table of a number
def multiplication_table(n):
    return [f"{n} x {i} = {n*i}" for i in range(1, 11)]

# 7. Factorial of a number
def factorial(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 8. Prime numbers between 1 and 50
def primes_up_to_50():
    return [n for n in range(2, 51) if is_prime(n)]

# 9. Count words with more than 5 characters
def count_long_words(words):
    return sum(1 for word in words if len(word) > 5)

# 10. Sum of digits of a number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))


# Example runs
if __name__ == "__main__":
    try:
        print(is_leap_year(2024))               # True
        print(find_even_numbers([1,2,3,4,5,6])) # [2, 4, 6]
        print(is_prime(29))                     # True
        print(fibonacci(7))                     # [0, 1, 1, 2, 3, 5, 8]
        print(names_starting_with_a(["Alice","Bob","Amy","John"])) # ['Alice', 'Amy']
        print(multiplication_table(5))
        print(factorial(5))                     # 120
        print(primes_up_to_50())                # [2, 3, 5, 7, 11, ... , 47]
        print(count_long_words(["apple","banana","cherry","kiwi"])) # 2
        print(sum_of_digits(12345))             # 15
        print(factorial(-5))  # Will raise ValueError
    except ValueError as e:
        print(f"Error: {e}")
