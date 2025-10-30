# 🏪 Inventory Manager

# Sample inventory list
inventory = [
    ["TCL TV", 10, 45000],
    ["Router", 15, 3500],
    ["Laptop", 8, 78000],
    ["Camera", 5, 22000]
]

# Show all items
for item in inventory:
    print(f"{item[0]} - Qty: {item[1]} - Price: {item[2]} KSH")

# Add new item
new_item = ["Smart Watch", 20, 5500]
inventory.append(new_item)  # add item

# Remove item
inventory.remove(["Camera", 5, 22000])  # remove by exact match

# Update quantity
for item in inventory:
    if item[0] == "Laptop":
        item[1] += 2  # add 2 more

# Find item
search = "Router"
for item in inventory:
    if item[0] == search:
        print(f"{search} found: {item}")

# Calculate total stock value
total = sum(item[1] * item[2] for item in inventory)
print("Total Stock Value:", total, "KSH")

# Sort by price high → low
inventory.sort(key=lambda x: x[2], reverse=True)

# Display sorted list
print("\nSorted Inventory:")
for item in inventory:
    print(item)
