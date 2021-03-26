import random
import time

import platform_config as pc

def main():
    words = get_words()
    while words:
        words = study(words)

def get_words():
    with open(pc.filepath, 'r', encoding='utf8') as lines:
        # split lines into [#, initial, en]
        words = [l.strip().split('\t') for l in lines if l.strip()]
    random.shuffle(words)
    return words

def study(words):
    review_words = []
    previous_word = ['', '', '']
    print(' '*20, end='')  # initialize query to the right column
    for _, initial, final in words:
        # shuffle asking final--initial or initial--final
        query, reply = (initial, final) if random.randint(0,1) else (final, initial)
        user = pc.get_input(query + '\t')
        # if user input, then mark the word for additional review
        if user: review_words.append(previous_word)
        print(f'  {reply:<18}', end='')
        previous_word = [_, initial, final]
    print('\n\nDONE\n\n')
    return review_words

main()


