# Helper functions for the Recipe Generator

import webbrowser
from urllib.parse import quote


def search_recipe_online(ingredient_name):
    query = f"recipes with {ingredient_name}"
    url = f"https://www.google.com/search?q={quote(query)}"
    print(f"Searching for recipes wih '{ingredient_name}'...")
    webbrowser.open(url)
