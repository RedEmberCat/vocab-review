import random
import time

import quiz_config as qc

def main():
    words = get_words()
    while words:
        words = study(words)

def get_words():
    with open(qc.filename, 'r', encoding='utf8') as lines:
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
        user = input(query + '\t')
        if user: review_words.append(previous_word)
        # if user input, then mark the word for additional review
        print(f'  {reply:<18}', end='')
        previous_word = [_, initial, final]
    print('\n\nDONE\n\n')
    return review_words

main()

