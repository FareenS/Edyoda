import json

# Initialize user data
users = []
current_user = None

# Function to load user data from a JSON file
def load_users():
    global users
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []

# Function to save user data to a JSON file
def save_users():
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

# Function to register a new user
def register_user():
    full_name = input("Enter your full name: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    password = input("Create a password: ")
    
    user = {
        "Full Name": full_name,
        "Phone Number": phone_number,
        "Email": email,
        "Address": address,
        "Password": password,
        "Order History": []
    }
    users.append(user)
    save_users()
    print("Registration successful!")

# Function to log in a user
def login_user():
    global current_user
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    for user in users:
        if user["Email"] == email and user["Password"] == password:
            current_user = user
            print(f"Welcome, {user['Full Name']}!")
            return
    print("Invalid email or password. Please try again.")

# Function to display the menu
def display_menu():
    print("🍽️ Menu:")
    for i, item in enumerate(menu, start=1):
        print(f"{i}. {item['Name']} ({item['Quantity']}) [INR {item['Price']}]")

# Function to place a new order
def place_order():
    if not current_user:
        print("Please log in to place an order.")
        return
    
    display_menu()
    
    selected_items = []
    while True:
        try:
            choice = int(input("Enter the number of the item to order (0 to finish): "))
            if choice == 0:
                break
            elif 1 <= choice <= len(menu):
                selected_items.append(menu[choice - 1])
            else:
                print("Invalid choice. Please enter a valid item number.")
        except ValueError:
            print("Invalid input. Please enter a valid item number.")
    
    if not selected_items:
        print("No items selected. Order canceled.")
        return
    
    total_price = sum(item["Price"] for item in selected_items)
    current_user["Order History"].append({
        "Ordered Items": selected_items,
        "Total Price": total_price
    })
    save_users()
    print("Order placed successfully!")

# Function to view order history
def view_order_history():
    if not current_user:
        print("Please log in to view your order history.")
        return
    
    order_history = current_user.get("Order History", [])
    if not order_history:
        print("No order history found.")
        return
    
    print("📜 Order History:")
    for i, order in enumerate(order_history, start=1):
        print(f"Order {i}:")
        for item in order["Ordered Items"]:
            print(f"{item['Name']} ({item['Quantity']}) [INR {item['Price']}]")
        print(f"Total Price: INR {order['Total Price']}")

# Function to update user profile
def update_profile():
    if not current_user:
        print("Please log in to update your profile.")
        return
    
    print("Update your profile:")
    current_user["Full Name"] = input("Full Name: ")
    current_user["Phone Number"] = input("Phone Number: ")
    current_user["Address"] = input("Address: ")
    current_user["Password"] = input("Password: ")
    save_users()
    print("Profile updated successfully!")

# Load menu data from a JSON file
with open("menu.json", "r") as file:
    menu = json.load(file)

# Main user panel
def user_panel():
    load_users()
    
    while True:
        print("\n👉 User Panel 👈")
        print("1. Register")
        print("2. Log in")
        print("3. Place New Order")
        print("4. Order History")
        print("5. Update Profile")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            place_order()
        elif choice == "4":
            view_order_history()
        elif choice == "5":
            update_profile()
        elif choice == "6":
            break

# Run the user panel
user_panel()
