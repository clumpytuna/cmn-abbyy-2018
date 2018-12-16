import pymorphy2
import re

# 2.1
"""
morph = pymorphy2.MorphAnalyzer()

hand = morph.parse('руки')[0]

print("2.1")
print(hand.normal_form)
print()

# 2.2
print("2.2")
print(morph.parse('руки'))
print()

# 2.3
three = morph.parse('три')

print("2.3")

for each in three:
    print(each.tag, each.normal_form, each.score)

print()

# 2.4
be = morph.parse('стать')
print("2.4")

for each in be:
    print(each.lexeme, each.score)

print()

# 2.5
turkey = morph.parse('турком')[0]

print("2.5")
print(turkey.inflect({'plur', 'ablt'}))
print()

# 2.6
mine = morph.parse('майню')[0]

print("2.6")
print(mine.tag.POS)
print()


# 3
"""


def text_to_wordlist(sentence):
    regexp = "[^а-яА-Яё]"
    sentence = re.sub(regexp, " ", sentence)
    result = sentence.lower().split()
    return result


with open("wp.txt", encoding='UTF-8') as file:
    wordlist = text_to_wordlist(file.read())
    print(len(wordlist))
    print(wordlist)

    noun_lemmas = []

