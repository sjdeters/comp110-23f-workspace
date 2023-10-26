"""Practice using dictionaries."""

# Create a new dictionary.
ice_cream: dict[str, float] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print(ice_cream)

# Adding a key, value pair to a dictionary.
ice_cream["mint"] = 3
print("Added mint to the dictionary.")
print(ice_cream)

# Removing a key, value pair.
ice_cream.pop("mint")
print("Removed mint:")
print(ice_cream)

# Accessing a value.
print(f"There are {ice_cream['chocolate']} orders of chocolate.")

# Updating a value.
ice_cream["vanilla"] = 10
ice_cream["vanilla"] += 2
print("After updating vanilla:")
print(ice_cream)

# Print the length.
print(f"There are {len(ice_cream)} key-value pairs.")

# Checking if values are in a dictionary.
print("Chocolate in dictionary?")
print("chocolate" in ice_cream)
print("Mint in dictionary?")
print("mint" in ice_cream)

# Using "in" in a conditional.
if "mint" in ice_cream:
    print(f"There are {ice_cream['mint']} orders of mint.")
else:
    print("There are no orders of mint.")
if "chocolate" in ice_cream:
    print(f"There are {ice_cream['chocolate']} orders of chocolate.")

# Loop through dictionary and print out each flavor and number of orders.
for flavor in ice_cream:
    print(f"{flavor} has {ice_cream[flavor]} orders.")