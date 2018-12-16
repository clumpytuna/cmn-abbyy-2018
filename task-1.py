import re

# Задача 1. Исправление опечаток на основе триграмм. (В конце второй презентации)


def text_to_word_list(sentence):
    regexp = "[^а-яА-Яё]"
    sentence = re.sub(regexp, " ", sentence)
    result = sentence.lower().split()
    return result


def get_n_grams(n, words):
    result = {}

    assert n > 1

    for word in words:
        word = '#' * (n - 1) + word + '#' * (n - 1)
        for i in range(0, len(word)):
            if (i + n - 1) >= len(word):
                break
            n_gram = word[i: i + 3]
            if n_gram in result:
                result[n_gram] += 1.0 / len(words)
            else:
                result[n_gram] = 1.0 / len(words)

    return result


def spell_checker(n_gram_frequency, word, border_frequency, n):
    for i in range(0, len(word)):
        if (i + n - 1) >= len(word):
            break
        n_gram = word[i: i + 3]
        if n_gram in n_gram_frequency:
            if border_frequency > n_gram_frequency[n_gram]:
                return False
        else:
            return False

    return True


def main():
    with open("wp.txt", encoding='UTF-8') as file:
        word_list = text_to_word_list(file.read())
        n_grams_frequency = get_n_grams(3, word_list)
        print(spell_checker(n_grams_frequency, 'мир', 0.00001, 3))


main()


