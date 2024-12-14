def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid input types")
        return None
    except OverflowError:
        print("Error: Integer overflow occurred")
        return None

#Example usage
print(function_with_uncommon_error(10, 2))
print(function_with_uncommon_error(10, 0))
print(function_with_uncommon_error(10, "a"))

#Improved handling of OverflowError using Decimal
from decimal import Decimal
import sys

try:
    result = Decimal(sys.maxsize) + 1
    print(result)
except OverflowError:
    print("Error: Integer overflow occurred")

#Improved handling of RecursionError with iteration
def iterative_function(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

print(iterative_function(1000))

#Additional error handling for RecursionError
try:
    print(iterative_function(1000))
except RecursionError:
    print("Error: Maximum recursion depth exceeded")
