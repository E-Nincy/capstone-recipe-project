# Recipe Generator

**Recipe Generator** is an interactive Python application that allows users to:
- Search for online recipes by ingredient
- Store and manage their own ingredients
- Learn about Python OOP, databases, CLI interfaces, and more

---

## Features

- Object-Oriented structure using classes (`Ingredient`, `Recipe`)
- SQLite database for storing ingredients
- Web search for recipes via `webbrowser`
- Simple CLI interface using `click` and `rich`
- Easy-to-extend modular project structure
- Exception handling (planned)
- Bonus: file I/O, decorators, and custom data analysis (optional)

---

## Technologies Used

- Python 3.x
- Standard libraries: `sqlite3`, `webbrowser`, `urllib.parse`
- External libraries: `click` (command-line interface), `rich` (pretty printing in terminal), `requests` (handling HTTP calls)

---

## Project Structure
recipe_generator/

├── cli.py # CLI interface logic

├── models.py # Ingredient and Recipe classes

├── database.py # Database setup and CRUD functions

├── utils.py # Web search and helper functions

├── main.py # Entry point

└── README.md # Project documentation


