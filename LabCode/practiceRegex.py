#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 14:52:31 2018

@author: dusty
"""

import pandas as pd
import re

data = pd.read_csv("/home/dusty/DatasetsDA/Enron/assignment12.csv")

def emailText(email):
    return email[re.search(r'X-FileName.*\n\n', email).span()[1]:]

def worried(text):
    return bool(re.search(r'\b(worry.*|worri.*)\b', text, re.IGNORECASE))

def troubled(text):
    return bool(re.search(r'\b(trouble.*|troubli.*)\b', text))

def sent(row):
    try:
      return bool(re.search(row['user'].split("-")[0], re.search(r'\nFrom:.*\nTo:', row['text']).group()))
    except:
      return False

def numRecip(row):
    try:
      return len(re.findall(r'@',re.search(r'\nTo:[\w\W]*\nX-From', row['text']).group()))
    except:
      return 0
    
data['email'] = data['text'].apply(emailText)
data['worry'] = data['email'].apply(worried)
data['trouble'] = data['email'].apply(troubled)
data['sent'] = data.apply(sent, axis=1)
data['recipients'] = data.apply(numRecip, axis=1)