# utils.py
# Helper functions for the Recipe Generator

import webbrowser
from urllib.parse import quote
from rich import print


def search_recipe_online(ingredient_name):
    query = f"recipes with {ingredient_name}"
    url = f"https://www.google.com/search?q={quote(query)}"
    print(f"🔎 [bold]Searching for recipes with:[/bold] '{ingredient_name}'...")
    webbrowser.open(url)
