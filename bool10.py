from math import sqrt
def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    x = sqrt(a)
    return  x % 1 == 0
print(main(9))