
def count(values, elt):
    result = 0
    for val in values:
        if val == elt:
            result = result + 1
    return result

def reverse(values):
    """Will reverse the passed in list."""
    left = 0
    right = len(values) - 1
    while left < right:
        tmp = values[left]
        values[left] = values[right]
        values[right] = tmp
        left = left + 1
        right = right - 1


def main():
    values = [5, 2, 8, 8, 0, -1, 10]
    reverse(values)


if __name__ == "__main__":
    main()