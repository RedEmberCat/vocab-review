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
        words = pc.study(words)

def get_words():
    with open(pc.filepath, 'r', encoding='utf8') as lines:
        # split lines into [#, initial, en]
        words = [l.strip().split('\t') for l in lines if l.strip()]
    random.shuffle(words)
    return words

def generate_audio():
    def audio_in_path(filepath, path):
        return filepath in path.iterdir()
    from gtts import gTTS
    from pathlib import Path
    audiopath = Path('./audio')
    audio_generated = False
    print('generating audio for')
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
