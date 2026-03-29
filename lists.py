# A list can be modified (mutable)

tasks_list = ["Clean the house", "Buy groceries", "Walk the dog"]

# Add a task to the list
tasks_list.append("Pay bills")
print("After adding a task:", tasks_list)

# Remove a task from the list
tasks_list.remove("Buy groceries")
print("After removing a task:", tasks_list)

# Update a task in the list
tasks_list[1] = "Take the dog to the vet"
print("After updating a task:", tasks_list)

# Sort the tasks alphabetically
tasks_list.sort()
print("After sorting tasks:", tasks_list)


# A tuple cannot be modified (Immutable)

tasks_tuple = ("Clean the house", "Buy groceries", "Walk the dog")

# Adding a task by creating a new tuple
tasks_tuple = tasks_tuple + ("Pay bills",)
print("\nAfter adding a task to tuple:", tasks_tuple)

# Removing a task (convert to list → modify → convert back)
temp_list = list(tasks_tuple)
temp_list.remove("Buy groceries")
tasks_tuple = tuple(temp_list)
print("After removing a task from tuple:", tasks_tuple)

# Updating a task
temp_list = list(tasks_tuple)
temp_list[1] = "Take the dog to the vet"
tasks_tuple = tuple(temp_list)
print("After updating a task in tuple:", tasks_tuple)

# Sorting a tuple
temp_list = list(tasks_tuple)
temp_list.sort()
tasks_tuple = tuple(temp_list)
print("After sorting tasks in tuple:", tasks_tuple)