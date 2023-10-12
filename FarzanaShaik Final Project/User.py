class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

    def update_profile(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

    def view_order_history(self):
        if not self.orders:
            print("No order history.")
        else:
            print("Order History:")
            for order in self.orders:
                print(order)

class FoodItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.quantity}) [INR {self.price}]"

class Order:
    def __init__(self, user):
        self.user = user
        self.items = []

    def add_item(self, food_item):
        self.items.append(food_item)

    def __str__(self):
        order_summary = "\n".join([str(item) for item in self.items])
        return f"Order by {self.user.full_name}:\n{order_summary}"

class RestaurantMenu:
    def __init__(self):
        self.food_items = [
            FoodItem("Tandoori Chicken", "4 pieces", 240),
            FoodItem("Vegan Burger", "1 Piece", 320),
            FoodItem("Truffle Cake", "500gm", 900)
        ]

    def show_food_list(self):
        print("List of Food Items:")
        for i, food_item in enumerate(self.food_items, start=1):
            print(f"{i}. {food_item}")

# Create a sample user and restaurant menu
user = User("John Doe", "1234567890", "john@example.com", "123 Main St", "password")
menu = RestaurantMenu()

while True:
    print("\nMenu:")
    print("1. Register")
    print("2. Log in")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Registration
        full_name = input("Full Name: ")
        phone_number = input("Phone Number: ")
        email = input("Email: ")
        address = input("Address: ")
        password = input("Password: ")
        user = User(full_name, phone_number, email, address, password)
        print("Registration successful!")

    elif choice == "2":
        # Log in
        email = input("Email: ")
        password = input("Password: ")

        if user.email == email and user.password == password:
            print(f"Welcome, {user.full_name}!")
            while True:
                print("\nUser Options:")
                print("1. Place New Order")
                print("2. Order History")
                print("3. Update Profile")
                print("4. Log out")
                user_choice = input("Enter your choice: ")

                if user_choice == "1":
                    # Place New Order
                    menu.show_food_list()
                    selected_items = input("Enter the numbers of the items you want to order (comma-separated): ")
                    selected_items = [int(item) for item in selected_items.split(",")]
                    order = Order(user)
                    for item in selected_items:
                        if 1 <= item <= len(menu.food_items):
                            order.add_item(menu.food_items[item - 1])
                        else:
                            print(f"Invalid item number {item}.")
                    print("Your selected items:")
                    print(order)
                    confirm = input("Place the order? (yes/no): ")
                    if confirm.lower() == "yes":
                        user.orders.append(order)
                        print("Order placed successfully!")

                elif user_choice == "2":
                    # Order History
                    user.view_order_history()

                elif user_choice == "3":
                    # Update Profile
                    full_name = input("Full Name: ")
                    phone_number = input("Phone Number: ")
                    email = input("Email: ")
                    address = input("Address: ")
                    password = input("Password: ")
                    user.update_profile(full_name, phone_number, email, address, password)
                    print("Profile updated successfully!")

                elif user_choice == "4":
                    # Log out
                    print("Logged out.")
                    break

                else:
                    print("Invalid choice.")

        else:
            print("Invalid email or password.")

    elif choice == "3":
        print("Exiting the application.")
        break

    else:
        print("Invalid choice.")
