# command-line interface logic

import click
from rich.console import Console
from rich.table import Table

from models import Ingredient
from utils import search_recipe_online
from database import init_db, add_ingredient, get_ingredients, delete_ingredient

console = Console()


@click.group()
def run_cli():
    """ Welcome to the Recipe Generator CLI 👨‍🍳"""
    init_db()
    console.print(
        "[bold green] 👋 Welcome to the Recipe Generator![/bold green]")

# --------------------------
# 1. Search for online recipes
# --------------------------


@run_cli.command()
@click.option("--ingredient", prompt="Enter an ingredient", help="Name of the ingredient")
def search(ingredient):
    """Search for recipes online using an ingredient"""
    ing = Ingredient(ingredient, 1)
    console.print(
        f"[cyan]🔍 Searching for recipes with [bold]{ingredient}[/bold]...[/cyan]")
    search_recipe_online(ingredient)

# ---------------
# 2. Show CLI info
# ---------------


@run_cli.command()
def info():
    """Show information about the project"""
    table = Table(title="Recipe Generator Info")

    table.add_column("Feauture", style="magenta", no_wrap=True)
    table.add_column("Description", style="green")

    table.add_row("Search Recipes",
                  "Searches Google for recipes with a chosen ingredient.")
    table.add_row("Interactive CLI", "Built using Click and styled with Rich.")
    table.add_row("Modular Code", "Organized into separate files for clarity.")
    table.add_row("Database Ready", "Prepared to store and retrieve recipes.")

    console.print(table)

# ---------------------------
# 3. Add ingredient to database
# ---------------------------


@run_cli.command()
@click.option("--name", prompt="Ingrediet, name", help="Name of the ingredient")
@click.option("--amount", prompt="Amount", help="Amount of the ingredients")
def add(name, amount):
    """Add ingredient to database"""
    add_ingredient(name, amount)
    console.print(
        f"[bold green]✅ Added {amount} of {name} to the database![/bold green]")

# ------------------
# 4. List ingredients
# ------------------


@run_cli.command()
def list():
    """List all ingredients from the database."""
    ingredients = get_ingredients()

    if not ingredients:
        console.print(
            "[bold red]⚠ No ingredients found in the database.[/bold red]")
        return

    table = Table(title="🧾 Ingredients in Database")
    table.add_column("Name", style="cyan")
    table.add_column("Amount", style="magenta")

    for name, amount in ingredients:
        table.add_row(name, amount)

    console.print(table)

# ------------------
# 5. Delete ingredient
# ------------------


@run_cli.command()
@click.option('--name', prompt='Name of ingredient to delete', help='Name of the ingredient to delete')
def delete(name):
    """Delete an ingredient from the database by name."""
    delete_ingredient(name)
    console.print(
        f"[bold red]🗑 Ingredient '{name}' deleted from the database.[/bold red]")


# --------------
# Run CLI
# --------------
if __name__ == "__main__":
    run_cli()
