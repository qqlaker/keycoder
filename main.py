from config import keys

def text_to_bin(text):
    textbin = bin(ord(text))
    return textbin

def bin_to_text(text):
    revert = ''.join([chr(int(s, 2)) for s in text.split()])
    return revert

s = ''
l = keys.__len__()
for i in range(1, l+1):
    x = str(i)
    key_text = keys[x]
    if len(key_text) > 1:
        list = []
        for i in key_text:
            list.append(i)
        for i in range(len(list)):
            list[i] = text_to_bin(list[i])
        sl = ''
        for i in range(len(list)):
            if i != (len(list)-1):
                sl += list[i]
                sl += '$'
            else:
                sl += list[i]
        s += '@'
        s += sl
    elif len(key_text) == 0:
        s += '@'
        s += '00000000'

