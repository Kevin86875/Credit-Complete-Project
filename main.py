###############################################################################
#Title: Credit Complete Project
#Name: Kevin Gao
#Assignment: Credit Complete Project
#Class: Computer Science
#Date: Sometime in our lifetime
###############################################################################
'''
This program is going to be a farming game where the player can be a farmer and farm in a maop with an inventory included.
'''

###############################################################################
#Imports and Global Variables--------------------------------------------------

from farming_game import Farmer, FarmMap, store_menu

def main():
    print("Welcome to the Farming Game!")
    player = Farmer()
    farm_map = FarmMap()
    player.map = farm_map

    player.set_name()

    while True:
        print("\nMain Menu:")
        print("1. View Map")
        print("2. Visit Store")
        print("3. Check Balance")
        print("4. View Seeds")
        print("5. Plant Crop")
        print("6. Harvest Crop")
        print("7. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            farm_map.view_map()
        elif choice == "2":
            store_menu(player)
        elif choice == "3":
            player.view_balance()
        elif choice == "4":
            player.view_seeds()
        elif choice == "5":
            crop = input("What crop do you want to plant (Corn/Wheat)? ").capitalize()
            field_coords = tuple(map(int, input("Enter field coordinates (row, col): ").split(',')))
            farm_map.plant_crop(player, crop, field_coords)
        elif choice == "6":
            field_coords = tuple(map(int, input("Enter field coordinates (row, col): ").split(',')))
            farm_map.harvest_crop(player, field_coords)
        elif choice == "7":
            print("Thanks for playing the Farming Game!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
