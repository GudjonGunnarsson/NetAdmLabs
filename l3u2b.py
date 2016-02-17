#!/usr/bin/python
# -*- coding: utf-8 -*-

# Labb 3 Uppgift 2b - ggn14002
# Räknar genom 1-100 i två olika loops. Först i en for-loop, sedan i en while-loop

count = 1
for num in range(1,101):
    print '(for) %d' % (num)
while (count < 101):
    print '(while) ', count
    count = count + 1
