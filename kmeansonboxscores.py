# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 10:55:25 2021

@author: yaobv
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Calculating features to classify players

totals = players21.groupby('Player').agg({'GameID': 'count',
                                 'PlayerFP' : 'sum',
                                 'MIN' : 'sum',
                                 'PTS' : 'sum',
                                 'TOT' : 'sum',
                                 'A' : 'sum',
                                 'ST' : 'sum',
                                 'BL' : 'sum',
                                 '3P' : 'sum',
                                 'Usage': 'median'})



totals['PTS/48'] = [(x/y) * 48 for x, y in zip(totals['PTS'], totals['MIN'])]
totals['TOT/48'] = [(x/y) * 48 for x, y in zip(totals['TOT'], totals['MIN'])]
totals['A/48'] = [(x/y) * 48 for x, y in zip(totals['A'], totals['MIN'])]
totals['STBL/48'] = [((x+y)/z) * 48 for x, y, z in zip(totals['ST'], totals['BL'], totals['MIN'])]

# Applying a filter to remove outliers

gamemin = totals['MIN'] >= 100
totals = totals[gamemin][['Usage', 'PTS/48', 'TOT/48', 'A/48', 'STBL/48']]

# Figuring out how many clusters to use

inertias = []

for k in range(1,12):
    
    model = KMeans(n_clusters = k)
    model.fit(totarr)
    inertias.append(model.inertia_)

plt.scatter(range(1,12), inertias)

# Clustering players and assigning labels

scaler = StandardScaler()
model = KMeans(n_clusters=4)
pipeline = make_pipeline(scaler, model)

labels = pipeline.fit_predict(totals)

totals['pipelabel'] = labels
