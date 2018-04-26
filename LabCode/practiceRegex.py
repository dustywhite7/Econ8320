#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 14:52:31 2018

@author: dusty
"""

import pandas as pd
import re

data = pd.read_csv("/home/dusty/Downloads/Enron/enronSmall.csv").drop("Unnamed: 0", axis=1)

def emailText(email):
    return email[re.search(r'\n{2}', data.loc[0,'text']).span()[0]:]