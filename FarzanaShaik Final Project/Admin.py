class FoodItem:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

    def __str__(self):
        return f"{self.name} ({self.quantity}) [INR {self.price}]"

class RestaurantMenu:
    def __init__(self):
        self.food_items = []
        self.food_id_counter = 1

    def add_food_item(self, name, quantity, price, discount, stock):
        food_item = FoodItem(self.food_id_counter, name, quantity, price, discount, stock)
        self.food_id_counter += 1
        self.food_items.append(food_item)
        print(f"Food item '{name}' has been added to the menu.")

    def show_food_list(self):
        if not self.food_items:
            print("The menu is empty.")
        else:
            print("List of Food Items:")
            for food_item in self.food_items:
                print(str(food_item))

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                print(f"Food item with FoodID {food_id} has been updated.")
                return
        print(f"Food item with FoodID {food_id} not found.")

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                print(f"Food item with FoodID {food_id} has been removed from the menu.")
                return
        print(f"Food item with FoodID {food_id} not found in the menu.")

# Create an instance of the RestaurantMenu class
menu = RestaurantMenu()

# Add new food items
menu.add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 10)
menu.add_food_item("Vegan Burger", "1 Piece", 320, 10, 5)
menu.add_food_item("Truffle Cake", "500gm", 900, 5, 8)

# Show the initial list of food items
menu.show_food_list()

# Edit a food item by FoodID
menu.edit_food_item(2, "Vegan Burger Deluxe", "1 Piece", 350, 15, 5)

# Show the updated list of food items
menu.show_food_list()

# Remove a food item by FoodID
menu.remove_food_item(1)

# Show the final list of food items
menu.show_food_list()
