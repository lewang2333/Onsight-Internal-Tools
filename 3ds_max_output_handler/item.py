from const import THRESHOLD
from collections import OrderedDict
from format import *

class Item:

    def __init__(self, number, s, threshold=THRESHOLD, filter=set(), format=str):
        self.number = str(number)
        self.dict = self.__parseAttribute(s)
        self.threshold = threshold
        self.filter = filter
        self.format = format

    def __parseAttribute(self, s):
        dict = OrderedDict({'No.': self.number})
        for line in s.split('\n'):
            att, val = line.strip().split(' = ')
            dict[keyFormat(att.strip())] = valFormat(val.strip())
        return dict

    def __str__(self):
        printAttributes = OrderedDict({'No.': self.number})
        for (key, val) in self.dict.items():
            if key.lower() in self.filter:
                printAttributes[key] = val

        if len(printAttributes) <= self.threshold + 1:
            return self.format(self.dict)
        else:
            return self.format(printAttributes)
