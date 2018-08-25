from converter import uni2win, uni2zg, win2uni, zg2uni


def convert(from_encoding='from_zawgyi', to_encoding='to_unicode', input=''):
    result = ''
    if from_encoding[5:] == to_encoding[3:]:
        return input
    if from_encoding == 'from_unicode':
        if to_encoding == 'to_zawgyi':
            result = uni2zg.convert(input)
        elif to_encoding == 'to_win':
            result = uni2win.convert(input)
    elif from_encoding == 'from_zawgyi':
        if to_encoding == 'to_unicode':
            result = zg2uni.convert(input)
        elif to_encoding == 'to_win':
            result = uni2win.convert(zg2uni.convert(input))
    elif from_encoding == 'from_win':
        if to_encoding == 'to_unicode':
            result = win2uni.convert(input)
        elif to_encoding == 'to_zawgyi':
            result = uni2zg.convert(win2uni.convert(input))
    return result
