# class definitions for the Recipe Generator

class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"{self.name}, {self.amount}"


class Recipe:
    def __init__(self, title, ingredients, link=None):
        self.title = title
        self.ingredients = ingredients  # List of ingrediets objects
        self.link = link

    def __str__(self):
        return f"{self.title}, {self.link}"
