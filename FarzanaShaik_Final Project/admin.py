import json

# Initialize an empty menu
menu = []

# Function to load the menu from a JSON file
def load_menu():
    global menu
    try:
        with open("menu.json", "r") as file:
            menu = json.load(file)
    except FileNotFoundError:
        menu = []

# Function to save the menu to a JSON file
def save_menu():
    with open("menu.json", "w") as file:
        json.dump(menu, file, indent=4)

# Function to add a new food item to the menu
def add_food_item(name, quantity, price, discount, stock):
    food_id = len(menu) + 1
    food_item = {
        "FoodID": food_id,
        "Name": name,
        "Quantity": quantity,
        "Price": price,
        "Discount": discount,
        "Stock": stock,
    }
    menu.append(food_item)
    save_menu()
    return f"Food item '{name}' added with FoodID: {food_id}"

# Function to edit a food item using FoodID
def edit_food_item(food_id, name, quantity, price, discount, stock):
    for food_item in menu:
        if food_item["FoodID"] == food_id:
            food_item["Name"] = name
            food_item["Quantity"] = quantity
            food_item["Price"] = price
            food_item["Discount"] = discount
            food_item["Stock"] = stock
            save_menu()
            return f"Food item '{name}' (FoodID: {food_id}) updated successfully"
    return f"Food item with FoodID {food_id} not found"

# Function to view the list of all food items
def view_menu():
    for food_item in menu:
        print(f"🔴 {food_item['Name']} ({food_item['Quantity']}) [INR {food_item['Price']}]")

# Function to remove a food item from the menu using FoodID
def remove_food_item(food_id):
    for food_item in menu:
        if food_item["FoodID"] == food_id:
            menu.remove(food_item)
            save_menu()
            return f"Food item '{food_item['Name']}' (FoodID: {food_id}) removed from the menu"
    return f"Food item with FoodID {food_id} not found"

# Main function for the admin panel
def admin_panel():
    load_menu()
    
    while True:
        print("\n👉 Admin Panel 👈")
        print("1. Add new food item")
        print("2. Edit food item")
        print("3. View menu")
        print("4. Remove food item")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter food name: ")
            quantity = input("Enter quantity (e.g., 100ml, 250gm, 4 pieces): ")
            price = float(input("Enter price: INR "))
            discount = float(input("Enter discount: "))
            stock = int(input("Enter stock amount: "))
            result = add_food_item(name, quantity, price, discount, stock)
            print(result)
        
        elif choice == "2":
            food_id = int(input("Enter FoodID to edit: "))
            name = input("Enter updated food name: ")
            quantity = input("Enter updated quantity: ")
            price = float(input("Enter updated price: INR "))
            discount = float(input("Enter updated discount: "))
            stock = int(input("Enter updated stock amount: "))
            result = edit_food_item(food_id, name, quantity, price, discount, stock)
            print(result)
        
        elif choice == "3":
            view_menu()
        
        elif choice == "4":
            food_id = int(input("Enter FoodID to remove: "))
            result = remove_food_item(food_id)
            print(result)
        
        elif choice == "5":
            break

# Run the admin panel
admin_panel()
