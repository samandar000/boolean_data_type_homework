def main(a):
    """Check the natural number.Natural numbers are numbers used in counting.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    x1 = int(a > 0)
    x2 = int (a%1 == 0)

    return x1 + x2 > 1
print(main(5)) 
