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
    letters = get_letters(text)

    return len(letters) == len(set(letters))


def is_pangram(text):
    """
    >>> is_pangram('The quick brown fox jumps over the lazy dog')
    True
    """
    letters = get_letters(text)
    # string.ascii_lowercase
    all_letters = set(string.ascii_lowercase)

    return set(letters) == all_letters


def is_anagram(text1, text2):
    """
    >>> is_anagram('Justin Timberlake', "I'm a jerk but listen")
    True
    """
    letters1 = get_letters(text1)
    letters2 = get_letters(text2)

    return sorted(letters1) == sorted(letters2)


def is_blanagram(text1, text2):
    """
    >>> is_blanagram('Justin Timberlake', "I'm a berk but listen")
    True
    """
    pass


def main():
    # print(is_palindrome("Mr. Owl ate my metal worm"))
    # print(is_palindrome("XYZ"))
    # print(is_isogram('uncopyrightables'))
    # print(is_isogram('abba'))
    # print(is_pangram("The quick brown fox jumps over the lazy dog"))
    # print(is_pangram("The quick brown the lazy dog"))
    print(is_anagram("Justin Timberlake", "I'm a jerk but listen"))
    print(is_anagram("abc", "def"))


if __name__ == "__main__":
    main()
