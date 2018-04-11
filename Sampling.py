# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 21:41:31 2018

@author: nikhi
"""

import random
import pandas as pd

df = pd.read_csv('links111.csv')

links_all = list(df.url)
print(links_all)
sample_size = 0.05*(int(len(links_all)))

lsample = random.sample(links_all, k = int(sample_size))
print(links_sample)


sample = open("rand_urls.csv",'w')

# Write data to file
for r in lsample:
    sample.write(r + "\n")
sample.close()