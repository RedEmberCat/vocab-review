import sys

filename = 'es-.txt'

# languages
initial = 'es'
final = 'en'

def input_from_button(_):
    response = {'canceled': True}
    while 'canceled' in response:  # := doesn't work on phone
        android.dialogCreateAlert()  # title, message
        android.dialogSetPositiveButtonText("okay")
        android.dialogSetNeutralButtonText("hard")
        android.dialogSetNegativeButtonText("exit")
        android.dialogShow()
        # response :: {'[which|canceled]' : '[positive|negative]'}
        response = android.dialogGetResponse().result
        android.dialogDismiss() # ? seems to work without this line
    if response['which'] == 'positive':
        return ''
    if response['which'] == 'neutral':
        return 'non-empty'
    else:
        sys.exit()


try:
    from androidhelper import Android
    onAndroid = True
    android = Android()
    get_input = input_from_button
    dir = r'/storage/emulated/0/user/docs/code/vocab-review/words/'
    audiodir = r'/storage/emulated/0/user/docs/code/vocab-review/audio/'
    play = lambda file: android.mediaPlay(audiodir + file + '.mp3')
except ModuleNotFoundError:
    onAndroid = False
    get_input = input
    dir = 'words/'

filepath = dir + filename
