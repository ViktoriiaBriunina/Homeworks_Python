def sum_numbers(*args: int) -> int:
    """Find a sum of numbers"""
    i = 0
    for a in args:
        i = i + a
    return i

print(sum_numbers(1, 2, 3, 4, 5))
