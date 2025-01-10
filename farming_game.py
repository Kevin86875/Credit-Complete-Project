class Farmer:
    def __init__(self):
        self.name = ""
        self.money = 10
        self.seeds = {"Corn": 0, "Wheat": 0}
        self.map = None  # To be assigned a FarmMap object

    def set_name(self):
        self.name = input("Choose your name: ")
        print(f"Welcome, {self.name}!")

    def view_balance(self):
        print(f"\nYour current balance is ${self.money}.")

    def view_seeds(self):
        print("Your seed inventory:")
        for crop, quantity in self.seeds.items():
            print(f"{crop}: {quantity} seeds")


class FarmMap:
    HARVEST_PRICES = {"Corn": 60, "Wheat": 40, "Dirt": 1}  # Prices for harvested crops

    def __init__(self):
        self.map = [
            ["Farm House", "Barn", "Field"],
            ["Field", "Field", "Field"],
            ["Field", "Field", "Field"]
        ]
        self.fields = {  # Keeps track of what is planted in each field
            (0, 2): None, (1, 0): None, (1, 1): None,
            (1, 2): None, (2, 0): None, (2, 1): None, (2, 2): None
        }

    def view_map(self):
        print("\nFarm Map")
        for row in self.map:
            print("|".join(row))
            print()

    def plant_crop(self, farmer, crop, field_coords):
        if field_coords not in self.fields:
            print("Hopefully it's somewhere on this planet. But wherever it is, ur not going to plant seeds in there.")
            return
        if self.fields[field_coords] is not None:
            print("Whoa the place is already occupied! If u put it in there they will start killing each other! ")
            return
        if farmer.seeds.get(crop, 0) <= 0:
            print(f"You don't have enough {crop} seeds!")
            return

        # Plant the crop
        self.fields[field_coords] = crop
        farmer.seeds[crop] -= 1
        self.map[field_coords[0]][field_coords[1]] = crop
        print(f"You planted {crop} in the field at {field_coords}!")

    def harvest_crop(self, farmer, field_coords):
        if field_coords not in self.fields:
            print("Invalid field coordinates!")
            return
        if self.fields[field_coords] is None:
            print("The field is empty. Selling the dirt for $1.")
            farmer.money += 1
            return
        crop = self.fields[field_coords]
        farmer.money += self.HARVEST_PRICES.get(crop, 0)
        self.fields[field_coords] = None
        self.map[field_coords[0]][field_coords[1]] = "Field"
        print(f"You harvested {crop} and earned ${self.HARVEST_PRICES[crop]}!")

def store_menu(farmer):
    store_items = [
        {"name": "Corn Seed", "price": 10, "type": "seed"},
        {"name": "Wheat Seed", "price": 8, "type": "seed"},
    ]

    while True:
        print("\nWelcome to the Store! What would you like to buy?")
        for i, item in enumerate(store_items, 1):
            print(f"{i}. {item['name']} - ${item['price']}")
        print("3. Leave the store")

        choice = input("Choose an option (1-3): ")

        if choice == "3":
            print("Leaving the store. Come back soon!")
            break
        try:
            selected_item = store_items[int(choice) - 1]
            if farmer.money >= selected_item["price"]:
                farmer.money -= selected_item["price"]
                if selected_item["type"] == "seed":
                    crop = selected_item["name"].replace(" Seed", "")
                    farmer.seeds[crop] += 1
                print(f"You bought {selected_item['name']} for ${selected_item['price']}.")
            else:
                print(f"You don't have enough money to buy {selected_item['name']}.")
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")
