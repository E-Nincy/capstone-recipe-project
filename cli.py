# command-line interface logic

import click
from rich.console import Console
from rich.table import Table

from models import Ingredient
from utils import search_recipe_online

console = Console()


@click.group()
def run_cli():
    """ Welcome to the Recipe Generator CLI"""
    console.print("[bold green] Welcome to the Recipe Generator![/bold green]")


@run_cli.command()
@click.option("--ingredient", prompt="Enter an ingredient", help="Name of the ingredient")
def search(ingredient):
    """Search for recipes online using an ingredient"""
    ing = Ingredient(ingredient, 1)
    console.print(
        f"[cyan]Searching for recipes with [bold]{ingredient}[/bold]...[/cyan]")
    search_recipe_online(ingredient)


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
