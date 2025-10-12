# 1. Calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width


# 2. Greeting message with user's name and age
def greet_user(name, age):
    return f"Hello {name}, you are {age} years old!"


# 3. Check if a number is even or odd
def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


# 4. Find maximum and minimum in a list
def find_max_min(numbers):
    return max(numbers), min(numbers)


# 5. Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]


# 6. Calculate compound interest
def compound_interest(principal, rate, time):
    return principal * ((1 + rate/100) ** time)


# 7. Convert days into years, weeks, and days
def convert_days(days):
    years = days // 365
    weeks = (days % 365) // 7
    remaining_days = (days % 365) % 7
    return years, weeks, remaining_days


# 8. Find the sum of all positive numbers in a list
def sum_positive_numbers(numbers):
    return sum(num for num in numbers if num > 0)


# 9. Count the number of words in a sentence
def word_count(sentence):
    return len(sentence.split())


# 10. Swap values of two variables
def swap_values(a, b):
    return b, a


if __name__ == "__main__":
    # Tiny demos for the assignment
    print("1) rectangle_area(5, 10) ->", rectangle_area(5, 10))
    print("2) greet_user('Alice', 30) ->", greet_user("Alice", 30))
    print("3) check_even_odd(7) ->", check_even_odd(7))
    print("4) find_max_min([3, 1, 9, 7, 2]) ->", find_max_min([3, 1, 9, 7, 2]))
    print("5) is_palindrome('madam') ->", is_palindrome("madam"))
    print("6) compound_interest(1000, 5, 2) ->", compound_interest(1000, 5, 2))
    print("7) convert_days(800) ->", convert_days(800))
    print("8) sum_positive_numbers([-1, 2, -3, 4, 5]) ->", sum_positive_numbers([-1, 2, -3, 4, 5]))
    print("9) word_count('Hello world from Python') ->", word_count("Hello world from Python"))
    print("10) swap_values(10, 20) ->", swap_values(10, 20))
