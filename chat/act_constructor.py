import re




def com_catcher(author,text):
    message = None
    try:
        command = re.findall(r'/(.+?)\s', text)[0]
        to_send = re.findall(r'/\w+\s+(\w.*)', text)[0]
        if command == 'me':
            message = f'*{author} {to_send}'
    except IndexError:
        pass
    return message
