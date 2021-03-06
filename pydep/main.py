import click
import os

@click.group()
def pydep():
    "Create pyproject.toml & poetry.lock dependency files from requirements.txt"

