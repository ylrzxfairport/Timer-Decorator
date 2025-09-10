# Python Timer Decorator

This repository provides a simple Python script that implements a timer using a decorator to measure function execution time.

## Features

- **Easy to use:** Just decorate any function with `@timer` to measure how long it takes to execute.
- **No dependencies:** Uses Python's built-in `time` module.

## Usage

1. Import or copy the `timer` decorator into your project.
2. Decorate the function you want to time:

    ```python
    @timer
    def my_function():
        # Your code here
        pass
    ```

3. Run your script and see the execution time printed in the console.

## Example

The provided `timer_decorator.py` includes an example:

```python
@timer
def example_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

if __name__ == "__main__":
    example_function()
```

When you run the script, you'll see output like:

```
Function 'example_function' executed in 0.046872 seconds
```

## License

This project is open source and available under the [MIT License](LICENSE).
