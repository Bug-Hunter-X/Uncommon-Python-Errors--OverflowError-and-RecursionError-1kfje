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

#Example usage
print(function_with_uncommon_error(10, 2))
print(function_with_uncommon_error(10, 0))
print(function_with_uncommon_error(10, "a"))

#Uncommon error : OverflowError

#Let's use the sys module to demonstrate the OverflowError
import sys

#For very very large numbers
max_int = sys.maxsize

#Trying to exceed the maximum value by adding 1
#This will raise an OverflowError
#print(max_int + 1)

#Similarly, for very very small numbers (negative side)
min_int = -sys.maxsize -1
#print(min_int -1)

#Handling OverflowError

try:
    result = max_int + 1
    print(result)
except OverflowError:
    print("Error: Integer overflow occurred")

#Handling OverflowError with arbitrary precision libraries
from decimal import Decimal

#Using the Decimal class for arbitrary precision arithmetic
large_number = Decimal(sys.maxsize) + 1
print(large_number)

#Recursions errors
def recursive_function(n):
    if n == 0:
        return 0
    else:
        return recursive_function(n-1) + n

#print(recursive_function(1000)) # This might cause RecursionError

#Handling RecursionError:

try:
    print(recursive_function(1000))
except RecursionError:
    print("Error: Maximum recursion depth exceeded")
