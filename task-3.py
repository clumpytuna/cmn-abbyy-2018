import math
import re

# Задача 2. Порождение подсказок по словарю (со звездочкой) (В конце второй презентации)


def text_to_word_list(sentence):
    regexp = "[^а-яА-Яё]"
    sentence = re.sub(regexp, " ", sentence)
    words = sentence.lower().split()
    return words


class TrieNode:
    best_match = ("", math.inf)

    def __init__(self):
        self.word_ = None
        self.children_ = {}

    def insert(self, word):
        node = self
        for letter in word:
            if letter not in node.children_:
                node.children_[letter] = TrieNode()

            node = node.children_[letter]

        node.word_ = word

    def _search_recursive(self, node, letter, word, previous_cost_array, best_match):

        columns = len(word) + 1
        current_cost_array = [previous_cost_array[0] + 1]

        for column in range(1, columns):

            insert_cost = current_cost_array[column - 1] + 1
            delete_cost = previous_cost_array[column] + 1

            if word[column - 1] != letter:
                replace_cost = previous_cost_array[column - 1] + 1
            else:
                replace_cost = previous_cost_array[column - 1]

            current_cost_array.append(min(insert_cost, delete_cost, replace_cost))

        if node.word_ is not None and current_cost_array[-1] < best_match[0][1]:
            best_match[0] = (node.word_, current_cost_array[-1])

        for letter in node.children_:
            self._search_recursive(node.children_[letter], letter, word, current_cost_array, best_match)

    def search(self, word):

        current_cost_array = [x for x in range(len(word) + 1)]
        best_match = [("", math.inf)]
        for letter in self.children_:
            self._search_recursive(self.children_[letter], letter, word, current_cost_array, best_match)
        return best_match


def main():

    trie = TrieNode()

    with open("wp.txt", encoding='UTF-8') as file:
        word_list = text_to_word_list(file.read())
        for word in word_list:
            trie.insert(word)

    best_match = trie.search('мир')[0]
    print("Наилучшее совпадение: {} \nРасстояние Левенштейна: {}".format(best_match[0], best_match[1]))


main()
