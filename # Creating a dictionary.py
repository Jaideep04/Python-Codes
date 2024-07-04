# Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York', 'grade': 'A'}

# 1. len(): Returns the number of key-value pairs in the dictionary
length_of_dict = len(my_dict)
print(f"Number of key-value pairs in the dictionary: {length_of_dict}")

# 2. keys(): Returns a list of all keys in the dictionary
keys_list = my_dict.keys()
print(f"All keys in the dictionary: {keys_list}")

# 3. values(): Returns a list of all values in the dictionary
values_list = my_dict.values()
print(f"All values in the dictionary: {values_list}")

# 4. items(): Returns a list of key-value pairs as tuples
items_list = my_dict.items()
print(f"All key-value pairs in the dictionary: {items_list}")

# 5. get(): Returns the value associated with a specified key
age_value = my_dict.get('age')
print(f"Value associated with the key 'age': {age_value}")

# 6. pop(): Removes the item with the specified key and returns its value
removed_item = my_dict.pop('grade')
print(f"Removed item with key 'grade' and its value: {removed_item}")
print(f"Dictionary after pop operation: {my_dict}")

# 7. update(): Updates the dictionary with elements from another dictionary or iterable
new_data = {'city': 'San Francisco', 'grade': 'B'}
my_dict.update(new_data)
print(f"Updated dictionary: {my_dict}")

# 8. clear(): Removes all items from the dictionary
my_dict.clear()
print(f"Dictionary after clear operation: {my_dict}")
