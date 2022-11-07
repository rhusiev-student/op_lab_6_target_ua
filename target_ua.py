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


def get_words(file: str, letters: list) -> list[tuple[str, str]]:
    """
    Get all possible words that have the first letter from the field
    and are <= 5 chars
    Also get their part of language

    Parameters
    ----------
    file : str
        The file to read the words from
    letters : list
        The letters to use

    Returns
    -------
    list
        The words that consist of these letters
    """
    with open(file, encoding="utf-8") as dictionary:
        words = dictionary.read().splitlines()
        valid_words = []
        for word in words:
            word, language_part = word.split(' ')[0:2]
            if language_part[0] == '/':
                language_part = language_part[1:]
            if language_part[0] == 'n' and not language_part[1:3] == 'no':
                language_part = 'noun'
            elif language_part[0] == 'v':
                language_part = 'verb'
            elif language_part[0] == 'a':
                if language_part[:3] == 'adj':
                    language_part = 'adjective'
                elif language_part[:3] == 'adv':
                    language_part = 'adverb'
            else:
                language_part = 'other'
            if 0 < len(word) <= 5 and word[0] in letters and language_part != 'other':
                valid_words.append((word, language_part))
        return valid_words


def _get_words_to_dict(words: list[tuple[str, str]]) -> dict[str, str]:
    """
    Get a dictionary of words and their part of language

    Parameters
    ----------
    words : list
        The words, got from the get_words function

    Returns
    -------
    dict
        The dictionary of words
    """
    dict_of_words = {}
    for word in words:
        dict_of_words[word[0]] = word[1]
    return dict_of_words


def check_user_words(user_words: list[str], language_part: str, letters: list[str],
                     dict_of_words: dict) -> tuple[list[str], list[str]]:
    """
    Check if the user's words are valid

    Parameters
    ----------
    user_words : list
        The user's words
    language_part : str
        The part of language to check
    letters : list
        The letters to use
    dict_of_words : dict
        The dictionary of words

    Returns
    -------
    list
        The valid words
    """
    valid_words = []
    forgotten_words = []
    for word in user_words:
        if word[0] in letters and word in dict_of_words\
                and dict_of_words[word] == language_part:
            valid_words.append(word)
    for word in dict_of_words:
        if word not in valid_words:
            forgotten_words.append(word)
    return valid_words, forgotten_words


def get_user_words():
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter
    for Windows.
    Note: the user presses the enter key after entering each word.

    Returns
    -------
    list
        The words entered by the user
    """
    user_words = []
    while True:
        try:
            user_words.append(input("Enter a word: "))
        except EOFError:
            return user_words


def main():
    """
    The main function
    """
    grid = generate_grid()
    print(' '.join(grid))
    language_part = random.choice(['noun', 'verb', 'adjective', 'adverb'])
    print(f'Enter {language_part}s:')
    words = get_words('base.lst', grid)
    dict_of_words = _get_words_to_dict(words)
    user_words = get_user_words()
    valid_words, forgotten_words = check_user_words(user_words, language_part,
                                                    grid, dict_of_words)
    print()
    print('Valid words:')
    for i in valid_words:
        print(f'  {i}')
    print('Forgotten words:')
    for i in forgotten_words:
        print(f'  {i}')


if __name__ == '__main__':
    main()
