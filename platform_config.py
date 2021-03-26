import sys

filename = 'es-.txt'

def input_from_button(_):
    response = {'canceled': True}
    while 'canceled' in response:  # := doesn't work on phone
        droid.dialogCreateAlert()  # title, message
        droid.dialogSetPositiveButtonText("okay")
        droid.dialogSetNeutralButtonText("hard")
        droid.dialogSetNegativeButtonText("quit")
        droid.dialogShow()
        # response :: {'[which|canceled]' : '[positive|negative]'}
        response = droid.dialogGetResponse().result
        droid.dialogDismiss() # ? seems to work without this line
    if response['which'] == 'positive':
        return ''
    if response['which'] == 'neutral':
        return 'non-empty'
    else:
        sys.exit()


try:
    from androidhelper import Android
    droid = Android()
    get_input = input_from_button
    dir = r'/storage/emulated/0/user/docs/code/vocab-review/words/'
except ModuleNotFoundError:
    get_input = input
    dir = 'words/'

filepath = dir + filename
