def search4vowels(phrase: str) -> set:
    """ returns set vowels in phrase """
    lowels = set('aeiou')
    return lowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """ returns set letters in phrase """
    return set(letters).intersection(set(phrase))
