# Задача 1: решение в лоб (В конце третьей презентации)

vowels = {'a', 'e', 'i', 'o', 'u'}
voiced_consonants = {'b', 'v', 'g', 'd', 'z', 'l', 'm', 'n', 'r'}
consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}


def get_plural(word):
    word = word.lower()

    if word[-1:] in vowels or word[-1:] in voiced_consonants:
        return word + 's'

    if word[-1:] == 's' or word[-1:] == 'x':
        return word + 'es'

    if len(word) > 2:
        if word[-2:] in {'ss', 'sh', 'ch'}:
            return word + 'es'
        if word[-1] == 'y' and word[-2] in consonants:
            return word[:-1] + 'ies'

        if word[-1] == 'y' and word[-2] in vowels:
            return word + 's'


print(get_plural('formula'))
