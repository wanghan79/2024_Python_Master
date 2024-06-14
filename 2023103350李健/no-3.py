from functools import wraps


def statistic_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Before function execution
        print(f"{func.__name__} is running...")

        # Perform some statistics (example: calculating sum)
        total_sum = sum(args)
        print(f"The sum of arguments is: {total_sum}")

        # Execute the function
        result = func(*args, **kwargs)

        # After function execution
        print(f"{func.__name__} finished.")

        return result

    return wrapper


# Example of using the decorator
@statistic_decorator
def calculate_sum(*args):
    return sum(args)


@statistic_decorator
def calculate_mean(*args):
    if args:
        return sum(args) / len(args)
    else:
        return 0


# Testing the decorated functions
print(calculate_sum(1, 2, 3, 4, 5))  # Output: 15
print(calculate_mean(1, 2, 3, 4, 5))  # Output: 3.0
