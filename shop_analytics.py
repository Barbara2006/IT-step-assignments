
inventory = {
    "laptop": {"price": 2500, "stock": 5},
    "phone": {"price": 1800, "stock": 10},
    "headphones": {"price": 250, "stock": 15},
    "keyboard": {"price": 150, "stock": 0},
    "monitor": {"price": 800, "stock": 3}
}

active_users = {"ana@gmail.com", "gio@gmail.com", "nino@gmail.com", "luka@gmail.com"}
vip_users = {"ana@gmail.com", "nino@gmail.com", "mari@gmail.com"}

print("===== INVENTORY MANAGEMENT =====")
print("1. Add a new product or update stock")
print("2. Skip")

choice = input("Choose an option (1/2): ")

if choice == "1":
    product_name = input("Enter product name: ").strip().lower()

    if product_name in inventory:
        print(f"Current stock: {inventory[product_name]['stock']}")

        try:
            quantity = int(input("Enter quantity to add: "))

            if quantity < 0:
                print("Quantity cannot be negative.")
            else:
                inventory[product_name]["stock"] += quantity
                print("Product quantity updated successfully.")

        except ValueError:
            print("Please enter a valid whole number.")

    else:
        try:
            price = float(input("Enter product price: "))
            stock = int(input("Enter product quantity: "))

            if price <= 0 or stock < 0:
                print("Price must be positive and quantity cannot be negative.")
            else:
                inventory[product_name] = {
                    "price": price,
                    "stock": stock
                }
                print("New product added successfully.")

        except ValueError:
            print("Please enter a valid price and whole-number quantity.")

print("\n===== FULL INVENTORY =====")

total_value = 0

for product, details in inventory.items():
    price = details["price"]
    stock = details["stock"]
    product_value = price * stock
    total_value += product_value

    print(
        f"Product: {product.title():<15} "
        f"Price: {price:>8.2f} GEL | "
        f"Stock: {stock:>3} | "
        f"Total: {product_value:>9.2f} GEL"
    )

print("-" * 75)
print(f"Total inventory value: {total_value:.2f} GEL")

print("\n===== AVAILABLE PRODUCTS =====")

available_products = {
    product: details
    for product, details in inventory.items()
    if details["stock"] > 0
}

if available_products:
    for product, details in available_products.items():
        print(f"{product.title()}: {details['stock']} units available")
else:
    print("No products are currently available.")

print("\n===== MOST EXPENSIVE PRODUCT =====")

if inventory:
    most_expensive = max(
        inventory,
        key=lambda product: inventory[product]["price"]
    )

    print(f"Product: {most_expensive.title()}")
    print(f"Price: {inventory[most_expensive]['price']:.2f} GEL")
else:
    print("Inventory is empty.")

print("\n===== USER ANALYTICS =====")

all_users = active_users.union(vip_users)
print(f"\nAll unique users ({len(all_users)}):")
print(all_users)

active_vip_users = active_users.intersection(vip_users)
print("\nActive VIP users:")
print(active_vip_users)

active_non_vip_users = active_users.difference(vip_users)
print("\nActive non-VIP users:")
print(active_non_vip_users)

print("\n===== ANALYSIS COMPLETED =====")
