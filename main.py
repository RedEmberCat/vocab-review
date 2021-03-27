# note: for the word con, i'm using kon because this is a reserved
# word in windows and can't be used for filenames

import random
import time

import platform_config as pc

def main():
    if not pc.onAndroid:
        generate_audio()
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

def audio_in_path(filepath, path):
    return filepath in path.iterdir()

def generate_audio():
    print('generating audio for')
    from gtts import gTTS
    from pathlib import Path
    audiopath = Path('./audio')
    audio_generated = False
    for word in get_words():
        for index in range(1, 3):
            item = word[index]
            filepath = audiopath / f'{item}.mp3'
            if not audio_in_path(filepath, audiopath):
                audio_generated = True
                language = pc.initial if index == 1 else pc.final
                tts = gTTS(text=item, lang=language)
                tts.save(filepath)
                print(f'  {item}')
    if not audio_generated:
        print('  None')
    print()


main()
