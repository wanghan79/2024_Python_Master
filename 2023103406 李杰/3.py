from functools import wraps

def stats_decorator(function):
    """Decorator to add statistics reporting to functions."""
    @wraps(function)
    def decorator(*args, **kwargs):
        # Before the function execution
        print(f"{function.__name__} is running...")

        # Perform some statistics (example: calculating sum)
        args_sum = sum(args)
        print(f"The sum of arguments is: {args_sum}")

        # Execute the function
        result = function(*args, **kwargs)

        # After function execution
        print(f"{function.__name__} finished.")

        return result

    return decorator

# Example using the decorator
@stats_decorator
def calculate_sum(*args):
    """Calculates the sum of given arguments."""
    return sum(args)

@stats_decorator
def calculate_mean(*args):
    """Calculates the mean of given arguments if not empty, otherwise returns 0."""
    if args:
        return sum(args) / len(args)
    return 0

# Testing the decorated functions
print(calculate_sum(1, 2, 3, 4, 5))  # Output: 15
print(calculate_mean(1, 2, 3, 4, 5))  # Output: 3.0
