"""
A target game:
    - A field of 5 letters is generated
    - The user enters words that has the first letter from the field
        and is <= 5 chars
    - The user enters words until he enters ctrl+d
"""
import random


def generate_grid() -> list[list[str]]:
    """
    Generate a grid of 5 unique ukrainian letters

    Returns
    -------
    list[str]
        The generated grid
    """
    letters = "абвгґдеєжзиіїйклмнопрстуфхцчшщюя"
    grid: list = random.sample(letters, 5)
    return grid
