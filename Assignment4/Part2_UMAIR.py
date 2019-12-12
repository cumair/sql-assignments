# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 19:56:15 2019

@author: mkalo
"""

'''
***********************************
         UMAIR CHAANDA
DSC 450   ASSIGNMENT-4    PART-2
***********************************
'''

import re
import json

datafile = open('Chicago.txt','r', encoding='utf8')
ChicagoData = datafile.read()
ChicagoData1 = str(ChicagoData)
datafile.close()

#****************PART-2 (a)************************
match = re.findall(r'.edit.[A-Z][a-z]+',ChicagoData1)
if match:
    print ('There are total ' +str(len(match))+ ' sections in this text')
else:
    print ('Did not find any match')

#****************PART-2 (b)*************************
CrimeSec = re.search(r'.edit.Crime\n.+\n.+\n\n.+\n\n.+',ChicagoData1)
if CrimeSec:
    CrimeSecStr = str(CrimeSec.group(0))

match2 = re.findall(r'[0-9]{4}',CrimeSecStr)
if match2:
    print ('All Years in Crime Section: '+str(sorted(set(match2))))
else:
    print ('Did not find any match')

#****************PART-3 (c)*************************'''
match3 = re.findall(r'[A-Z]?[a-z]?[A-Z][a-z]+.County',ChicagoData1)
if match3:
    print ('All County Names: '+str(set(match3)))
else:
    print ('Did not find any match')








