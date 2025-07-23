# command-line interface logic

from database import add_ingredient, get_ingredients, delete_ingredient
from utils import search_recipe_online


def run_cli():
    while True:
        print("Recipe Generator Menu")
        print("1. Add an ingredient")
        print("2. Search recipes online")
        print("3. View saved ingredients")
        print("4. Delete an ingredient")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            name = input("Enter ingredient name: ")
            amount = input("Enter amount (e.g. '2 cups'): ")
            add_ingredient(name, amount)
            print(f"Ingredient '{name}' added.")

        elif choice == "2":
            name = input("Enter ingredient to search recipes for: ")
            search_recipe_online(name)

        elif choice == "3":
            ingredients = get_ingredients()
            if ingredients:
                print("Saved Ingredients:")
                for name, amount in ingredients:
                    print(f"- {name}: {amount}")
            else:
                print("No ingredients saved.")

        elif choice == "4":
            name = input("Enter the name of the ingredient to delete: ")
            delete_ingredient(name)
            print(f"Ingredient '{name}' deleted (if it existed).")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 5.")