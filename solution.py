# Exercise 11 — Pure Functions vs Side Effects

# ── Part A: Rewrite as pure functions ────────────────────────────────────────
# Each function below has a side effect. Read the comment, then write a
# PURE version with the same name that produces the correct result without
# the side effect.


def double_all(numbers):
    """CURRENTLY IMPURE: modifies the input list in place.
    Rewrite to return a NEW list with each number doubled,
    leaving the original list unchanged.
    """
    for i in range(len(numbers)):
        numbers[i] *= 2
    # This function currently returns None — fix it too.


total = 0

def add_to_total(value):
    """CURRENTLY IMPURE: modifies the global variable `total`.
    Rewrite as a pure function that takes a current_total and a value,
    and returns the new total.
    Rename the parameters as needed; change the signature to:
        add_to_total(current_total, value)
    """
    global total
    total += value
    return total


# ── Part B: Implement pure functions from scratch ─────────────────────────────

def remove_item(lst, item):
    """Return a NEW list with the first occurrence of item removed.
    If item is not in the list, return a copy of the original.
    Do NOT modify the input list.
    """
    pass


def increment_all(d, amount):
    """Return a NEW dictionary with every value increased by amount.
    Do NOT modify the input dictionary.
    Example: increment_all({"a": 1, "b": 2}, 10) -> {"a": 11, "b": 12}
    """
    pass


def merge(dict1, dict2):
    """Return a NEW dictionary that merges dict1 and dict2.
    If a key exists in both, dict2's value wins.
    Do NOT modify either input.
    """
    pass
