from typing import List, Any, Tuple

# 1) Concatenate two lists
def concat_lists(a: List[Any], b: List[Any]) -> List[Any]:
    """Return a new list that is a + b (does not modify inputs)."""
    return a + b

# 2) Largest and smallest elements
def min_max(nums: List[float]) -> Tuple[float, float]:
    """Return (smallest, largest) in the list. Raises ValueError on empty list."""
    if not nums:
        raise ValueError("min_max() requires a non-empty list")
    return (min(nums), max(nums))

# 3) Square every number
def square_list(nums: List[float]) -> List[float]:
    """Return a list with each number squared."""
    return [x ** 2 for x in nums]

# 4) Common elements between two lists (keeps order from the first list)
def common_elements(a: List[Any], b: List[Any]) -> List[Any]:
    """Return elements that appear in both lists. Order follows a."""
    b_set = set(b)
    return [x for x in a if x in b_set]

# 5) Longest word and its length
def longest_word(words: List[str]) -> Tuple[str, int]:
    """Return (longest_word, length). Raises ValueError on empty list."""
    if not words:
        raise ValueError("longest_word() requires a non-empty list")
    w = max(words, key=len)
    return (w, len(w))

# 6) Count occurrences of each element (preserve first-seen order)
def count_occurrences(items: List[Any]) -> dict:
    """Return a dict {item: count} preserving first-seen order."""
    counts = {}
    for it in items:
        counts[it] = counts.get(it, 0) + 1
    # Preserve order by rebuilding using first-seen order
    ordered = {}
    for it in items:
        if it in counts and it not in ordered:
            ordered[it] = counts[it]
    return ordered

# 7) Remove duplicate names (preserve order)
def unique_names(names: List[str]) -> List[str]:
    """Return names with duplicates removed, keeping first occurrence order."""
    seen = set()
    unique = []
    for n in names:
        if n not in seen:
            unique.append(n)
            seen.add(n)
    return unique

# 8) Sort strings by their length (ascending). Ties keep alphabetical order.
def sort_by_length(strings: List[str]) -> List[str]:
    """Return a new list sorted by (length, alphabetical)."""
    return sorted(strings, key=lambda s: (len(s), s))

# 9) Check if a list is sorted in ascending order (non-decreasing)
def is_sorted_ascending(lst: List[Any]) -> bool:
    """Return True if each element <= next element."""
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

# 10) Union of two lists: all unique elements, preserving first-seen order
def union_lists(a: List[Any], b: List[Any]) -> List[Any]:
    """Return unique elements from both lists in the order they appear."""
    out = []
    seen = set()
    for x in a + b:
        if x not in seen:
            out.append(x)
            seen.add(x)
    return out

if __name__ == "__main__":
    print("1) concat_lists:", concat_lists([1, 2, 3], [4, 5]))
    print("2) min_max:", min_max([3, 7, -1, 9, 2]))
    print("3) square_list:", square_list([2, 4, 6]))
    print("4) common_elements:", common_elements([1, 2, 3, 4], [3, 4, 5]))
    lw, ln = longest_word(["apple", "banana", "kiwi", "strawberry"])
    print("5) longest_word:", (lw, ln))
    print("6) count_occurrences:", count_occurrences(
        ["apple", "banana", "apple", "orange", "banana", "apple"]))
    print("7) unique_names:", unique_names(
        ["John", "Alice", "John", "Bob", "Alice", "Cara"]))
    print("8) sort_by_length:", sort_by_length(["a", "pear", "banana", "apple"]))
    print("9) is_sorted_ascending:", is_sorted_ascending([1, 2, 2, 5]))
    print("10) union_lists:", union_lists([1, 2, 3], [3, 4, 1, 5]))