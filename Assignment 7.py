from typing import Any, Dict, List, Optional, Sequence, Tuple, Iterable, Set


# 1) Given two dictionaries, merge them into a single dictionary.
def merge_dicts(d1: Dict[Any, Any], d2: Dict[Any, Any]) -> Dict[Any, Any]:
    """Return a new dict with items of d1 and d2 (d2 overrides on conflicts)."""
    out = d1.copy()
    out.update(d2)
    return out


# 2) Find the most frequent element in a list.
def most_frequent(items: Sequence[Any]) -> Tuple[Any, int]:
    """
    Return (element, count) for the most common element.
    If the list is empty, raise ValueError.
    """
    if not items:
        raise ValueError("most_frequent() needs a non-empty list")
    counts: Dict[Any, int] = {}
    for x in items:
        counts[x] = counts.get(x, 0) + 1
    # max over counts by value
    elem = max(counts, key=lambda k: counts[k])
    return elem, counts[elem]


# 3) Remove a key-value pair from a dictionary.
def remove_pair(d: Dict[Any, Any], key: Any) -> Dict[Any, Any]:
    """Return a copy of d without 'key' (no error if missing)."""
    out = d.copy()
    out.pop(key, None)
    return out


# 4) Check if two sets have any elements in common.
def sets_have_common(a: Set[Any], b: Set[Any]) -> bool:
    """Return True if a and b share at least one element."""
    return len(a.intersection(b)) > 0


# 5) Given a list of dictionaries, find the dict with the highest value for a key.
def max_by_key(rows: List[Dict[str, Any]], key: str) -> Optional[Dict[str, Any]]:
    """
    Return the dictionary with the highest numeric value at 'key'.
    Ignores rows missing the key or with non-numeric values.
    Returns None if nothing qualifies.
    """
    filtered: List[Dict[str, Any]] = []
    for r in rows:
        v = r.get(key)
        if isinstance(v, (int, float)):
            filtered.append(r)
    if not filtered:
        return None
    return max(filtered, key=lambda r: r[key])


# 6) Count character occurrences in a string using a dictionary.
def char_counts(s: str) -> Dict[str, int]:
    """Return a dict mapping each character to its count."""
    counts: Dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


# 7) Given two sets, find the union, intersection, and differences.
def set_ops(a: Set[Any], b: Set[Any]) -> Tuple[Set[Any], Set[Any], Set[Any], Set[Any]]:
    """
    Return (union, intersection, a_minus_b, b_minus_a).
    """
    return a | b, a & b, a - b, b - a


# 8) Sort a list of dictionaries by a specified key.
def sort_dicts(rows: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Return a new list sorted by 'key'.
    Rows missing the key are placed at the end.
    """
    def key_fn(r: Dict[str, Any]):
        return (0, r[key]) if key in r else (1, None)
    return sorted(rows, key=key_fn, reverse=reverse)


# 9) Find the average value of all the elements for a key in a list of dictionaries.
def average_of_key(rows: List[Dict[str, Any]], key: str) -> Optional[float]:
    """
    Compute the mean of numeric values at 'key' across rows.
    Ignores rows missing the key or with non-numeric values.
    Return None if no valid values exist.
    """
    vals: List[float] = []
    for r in rows:
        v = r.get(key)
        if isinstance(v, (int, float)):
            vals.append(float(v))
    if not vals:
        return None
    return sum(vals) / len(vals)


# 10) From a list of strings, return the set of unique characters present in ALL strings.
def unique_chars_all(strings: Iterable[str]) -> Set[str]:
    """
    Return characters that appear in every string.
    Empty input yields an empty set.
    """
    it = iter(strings)
    try:
        first = next(it)
    except StopIteration:
        return set()
    common = set(first)
    for s in it:
        common &= set(s)
    return common


if __name__ == "__main__":
    print("1) merge_dicts:", merge_dicts({"a": 1, "b": 2}, {"b": 9, "c": 3}))

    elem, cnt = most_frequent([1, 2, 2, 3, 2, 1, 3, 3, 3])
    print("2) most_frequent:", (elem, cnt))

    print("3) remove_pair:", remove_pair({"x": 1, "y": 2}, "y"))

    print("4) sets_have_common:", sets_have_common({1, 2, 3}, {3, 4, 5}))

    people = [
        {"name": "Ana", "score": 88},
        {"name": "Ben", "score": 92},
        {"name": "Cal", "score": 86},
        {"name": "Dot"},  # missing key
    ]
    print("5) max_by_key:", max_by_key(people, "score"))

    print("6) char_counts:", char_counts("banana!"))

    u, i, d1, d2 = set_ops({"a", "b", "c"}, {"b", "c", "d"})
    print("7) set_ops:")
    print("   union       :", u)
    print("   intersection:", i)
    print("   a - b       :", d1)
    print("   b - a       :", d2)

    print("8) sort_dicts:", sort_dicts(people, "score"))

    print("9) average_of_key:", average_of_key(people, "score"))

    print("10) unique_chars_all:", unique_chars_all(["alphabet", "lambda", "lab"]))
