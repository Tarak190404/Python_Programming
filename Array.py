# Initialize an empty list to store the array elements
user_array = []

# Ask the user how many elements they want to enter
n = int(input("How many elements do you want to enter: "))

# Collect elements from the user
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    user_array.append(element)  # Append the element as a string

# Optionally, convert elements to integers if they are numeric
# Uncomment the following lines if you want to convert to integers
# user_array = [int(el) for el in user_array]

# Print the resulting array
print("The array you created is:", user_array)

#Print second and last item in my tuple
print("Second item:", user_array[1])
print("Last item:", user_array[-1])
