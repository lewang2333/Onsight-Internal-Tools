from item import *
from format import *
from const import *

def itemParser(data):
    """
    itype: String, raw data from input file
    rtype: List[String], item list
    """
    itemList = data.strip().split('\n\n')
    while itemList and not itemList[-1].startswith('id'):
        itemList.pop()
    return itemList


def readItemsFile(fileName):
    """
    itype: String, items file name
    rtype: String, raw data of items file
    """
    with open(fileName, 'r', encoding='utf-8') as f:
        data = f.read().strip()
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
