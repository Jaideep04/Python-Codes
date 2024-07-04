# Creating a tuple
my_tuple = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)

# 1. len(): Returns the length of the tuple
length_of_tuple = len(my_tuple)
print(f"Length of the tuple: {length_of_tuple}")

# 2. count(): Returns the number of occurrences of a specified value in the tuple
count_of_5 = my_tuple.count(5)
print(f"Number of occurrences of 5: {count_of_5}")

# 3. index(): Returns the index of the first occurrence of a specified value
index_of_9 = my_tuple.index(9)
print(f"Index of the first occurrence of 9: {index_of_9}")

# 4. sorted(): Returns a new sorted list from elements of the tuple
sorted_tuple = sorted(my_tuple)
print(f"Sorted tuple: {sorted_tuple}")

# 5. max(), min(), sum(): Returns the maximum, minimum, and sum of the tuple elements
max_value = max(my_tuple)
min_value = min(my_tuple)
sum_of_elements = sum(my_tuple)

print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
print(f"Sum of elements: {sum_of_elements}")
