from math import pi
from typing import List, Tuple


# 1) Given a list of numbers, find the sum and average.
def sum_and_average(nums: List[float]) -> Tuple[float, float]:
    total = sum(nums)
    avg = total / len(nums) if nums else 0.0
    return total, avg


# 2) Convert Celsius to Kelvin.
def celsius_to_kelvin(c: float) -> float:
    return c + 273.15


# 3) Check if a string is a palindrome (ignoring case & non‑alphanumerics).
def is_palindrome(s: str) -> bool:
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


# 4) Reverse a given string.
def reverse_string(s: str) -> str:
    return s[::-1]


# 5) Concatenate a list of names into a single string separated by spaces.
def join_names(names: List[str]) -> str:
    return " ".join(name.strip() for name in names if name.strip())


# 6) Check if a string is a pangram (contains all letters a–z).
def is_pangram(s: str) -> bool:
    letters = {ch for ch in s.lower() if "a" <= ch <= "z"}
    return len(letters) == 26


# 7) Calculate the area and circumference of a circle given its radius.
def circle_metrics(radius: float) -> Tuple[float, float]:
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    return area, circumference


# 8) Convert minutes to hours and minutes.
def minutes_to_hours_minutes(minutes: int) -> Tuple[int, int]:
    sign = -1 if minutes < 0 else 1
    m = abs(minutes)
    hours, mins = divmod(m, 60)
    return sign * hours, sign * mins if sign > 0 else -mins


# 9) Count the number of vowels in a string.
def count_vowels(s: str) -> int:
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in s if ch in vowels)


# 10) Check if a number is prime.
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i, step = 5, 2
    # Check factors up to sqrt(n) using 6k ± 1 pattern
    while i * i <= n:
        if n % i == 0:
            return False
        i += step
        step = 6 - step
    return True


if __name__ == "__main__":
    # Tiny demos you can run quickly.
    print("1) sum_and_average([1, 2, 3, 4]) ->", sum_and_average([1, 2, 3, 4]))
    print("2) celsius_to_kelvin(25) ->", celsius_to_kelvin(25))
    print("3) is_palindrome('Racecar!') ->", is_palindrome("Racecar!"))
    print("4) reverse_string('hello') ->", reverse_string("hello"))
    print("5) join_names(['Ada', 'Lovelace']) ->", join_names(["Ada", "Lovelace"]))
    print("6) is_pangram('The quick brown fox jumps over a lazy dog') ->",
          is_pangram("The quick brown fox jumps over a lazy dog"))
    print("7) circle_metrics(3) ->", circle_metrics(3))
    print("8) minutes_to_hours_minutes(135) ->", minutes_to_hours_minutes(135))
    print("9) count_vowels('Hello, World!') ->", count_vowels("Hello, World!"))
    print("10) is_prime(97) ->", is_prime(97))
