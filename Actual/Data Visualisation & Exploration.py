""" Script for Data Visualisation & Exploration """

# Standard Libraries Imported
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import os

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'Employee Engagement Survey(1-151).xlsx')

# Import Survey Results 
model_data = pd.read_excel(filename, header = None)

# Cleans last question survey data for model training
import clean_last
drivers = clean_last.clean_last_qns(model_data)

# Clean remaining questions survey data for model training
import clean_others
df, features = clean_others.clean(model_data)

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