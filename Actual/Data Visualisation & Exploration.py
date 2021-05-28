# -*- coding: utf-8 -*-
"""
Created on Wed May 19 13:44:33 2021

@author: uknow
"""
# Libraries Imported
import pandas as pd
import numpy as np
import seaborn as sns
import sklearn
import scipy
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from yellowbrick.cluster import KElbowVisualizer
from matplotlib import pyplot as plt
import os

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'Employee Engagement Survey(1-73).xlsx')

""" Start of Module 1 - Import, Clean Data & Data Manipulation (Works) """
# Import Survey Results 
# To change to pull request function
survey = pd.read_excel(filename, header = None)

# Pull out relevant columns in the excel
df = survey.iloc[1:,6:35]

# Rename Dataframe Columns
# i -> Individual
# w-> Wellbeing
# o -> Opinions & Emotions
# p_xn -> Neuroticism
# p_xa -> Agreeableness
# c -> Core Values
names = ["i_0", "i_1", "i_2", "i_3", "i_4", "i_5", "w_1", "w_2", "w_3", "w_4", "w_5", "o_1", "o_2", "o_3", "o_4", "o_5", "p_1n", "p_2n", "p_3n", "p_4n", "p_5a", "p_6a", "p_7a", "c_1", "c_2", "c_3", "c_4", "c_5", "c_6"]
df.columns = names

# Encoding of Categorical Data to Ranked Numerical Order
encode = { "i_1": {"20-29": 1, "30-39": 2, "40-49": 3, "50-59": 4, "60 and above": 5 },
            "i_2": {"Below 2 years": 1, "Below 3 years": 1, "3-5 years": 2, "6-10 years": 3, "11-19 years": 4, "20 years and above": 5},
            "i_3": {"Below 2 years": 1, "Below 3 years": 1, "3-5 years": 2, "6-10 years": 3, "11-19 years": 4, "20 years and above": 5},
}
df = df.replace(encode)

# Reverse Scoring for Neuroticism as it is found to have a negative relation with Employee Engagement
mapping = {1:5, 2: 4, 3: 3, 4: 2, 5: 1}
df["p_1n"] = df["p_1n"].map(mapping)
df["p_2n"] = df["p_2n"].map(mapping)
df["p_3n"] = df["p_3n"].map(mapping)
df["p_4n"] = df["p_4n"].map(mapping)

# Extract Features for Prediction & Clustering
features = df.drop(['i_0', 'i_4', 'i_5'], axis=1)

# Convert all relevant columns to numeric for clustering
cols = ["i_1", "i_2", "i_3", "w_1", "w_2", "w_3", "w_4", "w_5", "o_1", "o_2", "o_3", "o_4", "o_5", "p_1n", "p_2n", "p_3n", "p_4n", "p_5a", "p_6a", "p_7a", "c_1", "c_2", "c_3", "c_4", "c_5", "c_6"]
features[cols] = features[cols].apply(pd.to_numeric, errors='coerce', axis=1)
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce', axis=1)

# Univariate Analysis to understand Distribution of Data
features.hist(color='steelblue', edgecolor='black', linewidth=1.0,
           xlabelsize=8, ylabelsize=8, grid=False)    
plt.tight_layout(rect=(0, 0, 1.2, 1.2)) 

# Correlation Analysis
# Plot Heatmap of all correlation values
corr = features.corr()
f1, ax1 = plt.subplots(figsize=(10, 6))
mask = np.triu(np.ones_like(corr, dtype=bool))
hm_1 = sns.heatmap(round(corr,2), mask = mask, annot=True, ax=ax1, cmap="coolwarm",fmt='.2f',
                 linewidths=.5)
f1.subplots_adjust(top=0.93)
t1= f1.suptitle('Correlation Heatmap', fontsize=14)

# Plot Heatmap of high correlation values
high_corr = corr[corr >= 0.7]
f2, ax2 = plt.subplots(figsize=(10, 6))
mask = np.triu(np.ones_like(high_corr, dtype=bool))
hm_2 = sns.heatmap(round(high_corr,2), mask = mask, annot=True, ax=ax2, cmap="autumn_r",fmt='.2f',
                 linewidths=.5)
f2.subplots_adjust(top=0.93)
t2= f2.suptitle('Correlation Heatmap', fontsize=14)
