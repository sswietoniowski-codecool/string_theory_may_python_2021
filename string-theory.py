import string


def get_letters(text):
    letters = []
    for character in text:
        lowercase_character = character.lower()
        if lowercase_character in string.ascii_lowercase:
            letters.append(lowercase_character)

    return letters


def is_palindrome(text):
    """
    >>> is_palindrome('Mr. Owl ate my metal worm')
    True
    >>> is_palindrome('Eva, can I see bees in a cave?')
    True
    """
    letters = get_letters(text)

    return letters == letters[::-1]


def is_isogram(text):
    """
    >>> is_isogram('uncopyrightables')
    True
    """
    pass


def is_pangram(text):
    """
    >>> is_pangram('The quick brown fox jumps over the lazy dog')
    True
    """
    pass


def is_anagram(text1, text2):
    """
    >>> is_anagram('Justin Timberlake', "I'm a jerk but listen")
    True
    """
    pass


def is_blanagram(text1, text2):
    """
    >>> is_blanagram('Justin Timberlake', "I'm a berk but listen")
    True
    """
    pass


def main():
    print(is_palindrome("Mr. Owl ate my metal worm"))
    print(is_palindrome("XYZ"))


if __name__ == "__main__":
    main()
