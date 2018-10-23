import os

from item import *
from format import *
from const import *

def getInputFiles():
    '''
    itype: None
    rtype: The input file in this dir
    '''
    for file in os.listdir('.'):
        if file.endswith('.txt') and file != 'filter.txt':
            return file
    raise Exception('No input file!')

def itemParser(data):
    """
    itype: String, raw data from input file
    rtype: List[String], item list
    """
    itemList = []
    item = None
    for line in data.strip().split('\n'):
        if line.startswith('id'):
            item = [line]
        elif line == '' and item:
            itemList.append('\n'.join(item))
            item = None
        elif item:
            item.append(line)
    if item:
        itemList.append('\n'.join(item))
    return itemList


def readItemsFile(fileName):
    """
    itype: String, items file name
    rtype: String, raw data of items file
    """
    with open(fileName, 'r', encoding='utf-8') as f:
        data = f.read().strip()

    # remove 3ds header
    if data and ord(data[0]) == 65279:
        data = data[1:]

    return data


def readStopWordsFile(fileName):
    """
    itype: String, stop words file name
    rtype: Set(String), stop words list
    """
    with open(fileName, 'r', encoding='utf-8') as f:
        stopWordsList = f.read().strip().split(',')
    res = set()
    for s in stopWordsList:
        res.add(keyFormat(s).lower())
    return res
