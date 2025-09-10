import time

def timer(func):
    """
    Decorator that measures the execution time of a function.
    Prints the function's name and how long it took to run.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"Function '{func.__name__}' executed in {elapsed:.6f} seconds")
        return result
    return wrapper

# Example usage:
@timer
def example_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

if __name__ == "__main__":
    example_function()
