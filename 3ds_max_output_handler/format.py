from const import *


def format(dict):
    """
    itype: Dict
    rtype: String, formatted dict
    """
    res = ['\t\t<object>']
    for (key, val) in dict.items():
        line = '\t\t\t<{}>"{}"</{}>'.format(key, val, key)
        res.append(line)
    res.append('\t\t</object>\n')

    return '\n'.join(res)


def keyFormat(key):
    key = key.strip()
    for (k, v) in keyMap.items():
        key = key.replace(k, v)
    if key and key[0].isnumeric():
        key = '_' + key
    return key


def valFormat(val):
    val = val.strip()
    for (k, v) in valMap.items():
        val = val.replace(k, v)
    return val
