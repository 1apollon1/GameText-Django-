




def com_catcher(author,text):
    try:
        endind = text.index(' ')
    except:
        return


    command = text[1:endind]
    if command == 'me':
        return f'*{author}{text[endind:]}'