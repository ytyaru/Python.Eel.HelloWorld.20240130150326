#!/usr/bin/env python3
# coding: utf8
import eel, os
if __name__ == '__main__':
    #eel.init('web')
    eel.init(os.path.join(os.path.dirname(__file__), 'web'))
    eel.start('index.html')

