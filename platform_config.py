import random
import sys

# languages
initial = 'es'
final = 'en'

def show_query_and_wait(query, review_words):
    response = {'which': 'neutral'}
    while 'neutral' in response.values():  # := doesn't work on phone
        print(play(query))
        android.dialogCreateAlert(title=query)  # title, message
        # this button configuration makes it easier to press when
        #   holding the phone in the right hand, as i do.
        if review_words:
            android.dialogSetPositiveButtonText("review")
        else:
            android.dialogSetPositiveButtonText("exit")
        android.dialogSetNeutralButtonText("again")
        android.dialogShow()
        # response :: {'[which|canceled]' : '[positive|negative]'}
        response = android.dialogGetResponse().result
        android.dialogDismiss() # ? seems to work without this line
    if response.get('which') == 'positive':
        if review_words:
            return 'review'
        else:
            sys.exit()
    else:
        return ''

def show_reply_get_difficulty(reply, review_words):
    response = {'which': 'neutral'}
    while 'neutral' in response.values():  # := doesn't work on phone
        print(play(reply))
        android.dialogCreateAlert(title=reply)  # title, message
        # this button configuration makes it easier to press when
        #   holding the phone in the right hand, as i do.
        if review_words:
            android.dialogSetPositiveButtonText("review")
        else:
            android.dialogSetPositiveButtonText("exit")
        android.dialogSetNeutralButtonText("again")
        android.dialogSetNegativeButtonText("hard")
        android.dialogShow()
        # response :: {'[which|canceled]' : '[positive|negative|neutral]'}
        response = android.dialogGetResponse().result
        android.dialogDismiss() # ? seems to work without this line
    if response.get('which') == 'positive':
        if review_words:
            return 'review'
        else:
            sys.exit()
    if response.get('which') == 'negative':
        return 'non-empty'
    else:
        return ''

def study_pc(words):
    """provide CLI interface"""
    review_words = []
    previous_word = ['', '', '']
    print(' '*20, end='')  # initialize query to the right column
    for word in words:
        number, initial, final = word
        # shuffle asking final--initial or initial--final
        query, reply = (initial, final) if random.randint(0,1) else (final, initial)
        user = input(query + '\t')
        if user: review_words.append(previous_word)
        print(f'  {reply:<18}', end='')
        previous_word = word
    print('\n\nDONE\n\n')
    return review_words

def study_android(words):
    """provide study on android"""
    # play query audio and await user
    # on button press, play reply audio and await user
    # if user selects hard, add word to review list
    review_words = []
    for word in words:
        number, initial, final = word
        # shuffle asking final--initial or initial--final
        query, reply = (initial, final) if random.randint(0,1) else (final, initial)
        user = show_query_and_wait(query, review_words)
        if user == 'review': break
        user = show_reply_get_difficulty(reply, review_words)
        if user == 'review': break
        if user: review_words.append(word)
    return review_words

try:
    from androidhelper import Android
    onAndroid = True
    android = Android()
    study = study_android
    dir = r'/storage/emulated/0/user/docs/code/vocab-review/words/'
    audiodir = r'/storage/emulated/0/user/docs/code/vocab-review/audio/'
    play = lambda file: android.mediaPlay(audiodir + file + '.mp3')
except ModuleNotFoundError:
    onAndroid = False
    study = study_pc
    dir = 'words/'

