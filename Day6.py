# Use a lambda to create a function that checks if a number is positive

is_positive = lambda x: x > 0

print(is_positive(5))   # Should print: True
print(is_positive(-3))  # Should print: False

# 1. Create a lambda function called 'double' that multiplies a number by 2
double = lambda x: x*2

# 2. Use your 'double' function with map to double all numbers in this list
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(double, numbers))

print(double(7))           # Should print: 14
print(doubled_numbers)     # Should print: [2, 4, 6, 8, 10]