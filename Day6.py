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

# Create a lambda that calculates the area of a rectangle
# Formula: area = length × width

rectangle_area = lambda x,y: x*y

print(rectangle_area(5, 10))  # Should print: 50
print(rectangle_area(7, 3))   # Should print: 21

# Create a lambda that returns "Even" if a number is even, "Odd" if odd
# Hint: Use this pattern: value_if_true if condition else value_if_false
# Remember: even numbers have x % 2 == 0

check_even_odd = lambda x: "even" if x % 2 == 0 else "odd"

print(check_even_odd(4))   # Should print: Even
print(check_even_odd(7))   # Should print: Odd

# BONUS: Use it with map!
numbers = [1, 2, 3, 4, 5, 6]
results = list(map(check_even_odd,numbers))
print(results)  # Should print: ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']


# filter() works like map(), but keeps only items where the lambda returns True

# You have a list of temperatures in Celsius
temperatures = [-5, 0, 10, 15, 20, 25, 30, 35]

# Use filter with a lambda to get only temperatures above 20°C
hot_days = list(filter(lambda x:x > 20,temperatures))

print(hot_days)  # Should print: [25, 30, 35]

# BONUS: Get temperatures below 10°C (cold days)
cold_days = list(filter(lambda x:x < 10,temperatures ))
print(cold_days)  # Should print: [-5, 0]