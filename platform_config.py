filename = 'es-.txt'

def input_from_button(_):
    reponse = {'canceled': True}
    while 'canceled' in response:  # := doesn't work on phone
        droid.dialogCreateAlert()  # title, message
        droid.dialogSetPositiveButtonText("okay")
        droid.dialogSetNegativeButtonText("hard")
        droid.dialogShow()
        # response :: {'[which|canceled]' : '[positive|negative]'}
        response = droid.dialogGetResponse().result
        droid.dialogDismiss() # ? seems to work without this line
    return '' if response['which'] == 'positive' else 'non-empty'

try:
    from androidhelper import Android
    droid = Android()
    get_input = input_from_button
    dir = r'/storage/emulated/0/user/docs/code/vocab-review/words/'
except ModuleNotFoundError:
    get_input = input
    dir = 'words/'

filepath = dir + filename
