# Importing the math module
import math

# 1. ceil(): Returns the ceiling value (smallest integer greater than or equal to x)
ceil_value = math.ceil(4.25)
print(f"Ceiling value of 4.25: {ceil_value}")

# 2. floor(): Returns the floor value (largest integer less than or equal to x)
floor_value = math.floor(4.75)
print(f"Floor value of 4.75: {floor_value}")

# 3. factorial(): Returns the factorial of a number
factorial_value = math.factorial(5)
print(f"Factorial of 5: {factorial_value}")

# 4. isqrt(): Returns the integer square root of a non-negative number
sqrt_value = math.isqrt(25)
print(f"Integer square root of 25: {sqrt_value}")

# 5. pow(): Returns x to the power of y (x**y)
power_value = math.pow(2, 3)
print(f"2 to the power of 3: {power_value}")

# Additional examples with floating-point values
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Exponential function of 2: {math.exp(2)}")
print(f"Natural logarithm of 10: {math.log(10)}")
print(f"Sine of 30 degrees: {math.sin(math.radians(30))}")
