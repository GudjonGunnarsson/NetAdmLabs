#!/usr/bin/python
# -*- coding: utf-8 -*-

# Labb 3 Uppgift 2a - ggn14002
# Accepterar två argument, ger felmeddelande om endast 1 eller fler än 2 argument skickas in

import sys

arguments = sys.argv[1:]
count = len(arguments)
if ( count == 1 ):
    print 'Err: Only 1 Argument'
elif ( count >= 3 ):
    print 'Err: More than 2 Arguments'
elif ( count == 2 ):
    print sys.argv[1:]
