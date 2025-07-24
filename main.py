# Entry point for the Recipe Generator project

from cli import run_cli
from database import init_db

if __name__ == "__main__":
    init_db()
    run_cli()
