from math import sqrt


def is_prime(number: int) -> bool:
    """
    Return True if the given integer is a prime number, False otherwise.
    """
    divisor: int
    result: bool

    if number <= 1:
        result = False
    else:
        result = True
        divisor = 2
        while divisor <= sqrt(number) and result:
            if number % divisor == 0:
                result = False
            divisor += 1

    return result


def fibonacci_iterative(k: int) -> int:
    """
    Compute and return the k-th Fibonacci number iteratively.
    """
    result: int = 1
    prev_val: int = 0
    curr_val: int = 1
    next_val: int

    if k == 0:
        result = 0
    elif k == 1:
        result = curr_val
    else:
        for _ in range(2, k + 1):
            next_val = prev_val + curr_val
            result = next_val
            prev_val = curr_val
            curr_val = next_val

    return result


def fibonacci_recursive(k: int) -> int:
    """
    Compute and return the k-th Fibonacci number recursively.
    """
    result: int

    if k == 1:
        result = 1
    elif k == 0:
        result = 0
    else:
        result = fibonacci_recursive(k - 1) + fibonacci_recursive(k - 2)

    return result


def factorial(number: int) -> int:
    """
    Compute and return the factorial of the given integer (number!).
    """
    result: int

    if number <= 1:
        result = 1
    else:
        result = number * factorial(number - 1)

    return result
