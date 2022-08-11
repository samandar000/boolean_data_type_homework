def main(a):
    """
    check the whole number. Integers are 0 and a positive number.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    x1 = int(a >= 0)
    x2 = int (a%1 == 0)

    return x1 + x2 > 1
print(main(5)) 
