# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:12:55 2018

@author: nikhi
"""

import random
import pandas as pd

df = pd.read_csv('links.csv')

links_all = list(df.url)


sample_size = 50
links_sample = random.sample(links_all, k = sample_size)
print(links_sample)


sample = open("rand_urls.csv",'w')

# Write data to file
for r in links_sample:
    sample.write(r + "\n")
sample.close()
