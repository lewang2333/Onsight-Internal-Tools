# -*- coding: utf-8 -*-
from collections import OrderedDict
from sys import argv

class Item(object):
    """Formalized item info"""
    def __init__(self, str_data):
        self.info = OrderedDict()
        self.__extract__(str_data)

    def __extract__(self, str_data):
        """Extract item info from the raw text"""
        data = str_data.strip().split('\n')
        for line in data:
            try:
                para, val = line.strip().split('=')
            except:
                pass
            self.info[para.strip()] = val.strip()

    def __str__(self):
        res = []
        for keyval in self.info.items():
            res.append(' = '.join(keyval))
        return '\n'.join(res)


def read_data(name, norm=None):
    f = open(name, 'r')
    raw_data = f.read()
    f.close()
    if norm:
        return norm(raw_data)
    return raw_data

def remove_irrelevant(raw_data):
    res = []
    for line in raw_data.split("\n\n"):
        if line.strip().lower().startswith("id"):
            res.append(line)
    return res

def normalize(data):
    res = set()
    for line in data.strip().split(','):
        res.add(line.strip().lower())
    return res

def validate(item, words):
    res = []
    for keyval in item.info.items():
        if keyval[0].lower() in words:
            res.append( keyval[0].replace(' ','') + '=\"' + keyval[1] + '\"')
    return '        <Object ' + ' '.join(res) + ' />'

if __name__ == '__main__':
    raw_data = read_data(argv[1])
    filter_words = read_data(argv[2], normalize)
    data_by_item = remove_irrelevant(raw_data)
    items = []
    for item_data in data_by_item:
        items.append(Item(item_data))
    f = open("output.xml", 'w')
    f.write('<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n')
    f.write('    <' + argv[1].split('.')[0] + '>\n')
    for item in items:
        f.write(validate(item, filter_words) + '\n')
    f.write('    </' + argv[1].split('.')[0] + '>')
    f.close()
