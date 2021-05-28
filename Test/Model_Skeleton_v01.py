# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:49:12 2021

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

filename = os.path.join(here, 'EES Survey Test 1.xlsx')
"""
Skeleton Code for main functionality, not yet broken down into modular functions
"""

""" Start of Module 1 - Import, Clean Data & Data Manipulation (Works) """
# Import Survey Results 
# To change to pull request function
survey = pd.read_excel(filename, header = None)

# Pull out relevant columns in the excel
df = survey.iloc[1:,5:29]

# Rename Dataframe Columns
# i -> Individual, w-> Wellbeing, o -> Opinions & Emotions, p_xn -> Neuroticism, p_xa -> Agreeableness
names = ["i_0", "i_1", "i_2", "i_3", "i_4", "w_1", "w_2", "w_3", "o_1", "o_2", "o_3", "o_4", "o_5", "o_6", "o_7", "o_8", "o_9", "p_1n", "p_2n", "p_3n", "p_4n", "p_5a", "p_6a", "p_7a"]
df.columns = names

# Encoding of Categorical Data to Ranked Numerical Order
encode = { "i_1": {"20-29": 1, "30-39": 2, "40-49": 3, "50-59": 4, "60 and above": 5 },
            "i_2": {"Below 2 years": 1, "3-5 years": 2, "6-10 years": 3, "11-19 years": 4, "20 years and above": 5},
            "i_3": {"Below 2 years": 1, "3-5 years": 2, "6-10 years": 3, "11-19 years": 4, "20 years and above": 5},
            "i_4": {"Below SGD $2000": 1, "SGD $2000-2800": 2, "SGD $2800-3500": 3, "SGD $3500-5500": 4, "SGD $5500-8000": 5, "Above SGD $8000": 6}
}
df = df.replace(encode)

# Reverse Scoring for Neuroticism
mapping = {1:5, 2: 4, 3: 3, 4: 2, 5: 1}
df["p_1n"] = df["p_1n"].map(mapping)
df["p_2n"] = df["p_2n"].map(mapping)
df["p_3n"] = df["p_3n"].map(mapping)
df["p_4n"] = df["p_4n"].map(mapping)

# Convert all columns to numeric
cols = ["i_1", "i_2", "i_3", "i_4", "w_1", "w_2", "w_3", "o_1", "o_2", "o_3", "o_4", "o_5", "o_6", "o_7", "o_8", "o_9", "p_1n", "p_2n", "p_3n", "p_4n", "p_5a", "p_6a", "p_7a"]
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce', axis=1)

# Extract Features for Prediction & Clustering
features = df.iloc[:, 1:24]

""" End of Module 1 - Import, Clean Data & Data Manipulation """

""" Start of Module 2 - Model Training (Works)"""

""" Start of Pre-work - Determining the right number of clusters"""
### Run this code each time the model needs to be changed 
model = KMeans()

### 1. Elbow Method
# k is range of number of clusters.
visualizer = KElbowVisualizer(model, k=(2,30), timings= True)
visualizer.fit(features) # Fit the data to the visualizer
visualizer.show()        # Plot

### 2. Silhouette Coefficient
# k is range of number of clusters.
visualizer = KElbowVisualizer(model, k=(2,30),metric='silhouette', timings= True)
visualizer.fit(features) # Fit the data to the visualizer
visualizer.show()        # Plot

### 3. Calinski Harabasz Index
# k is range of number of clusters.
visualizer = KElbowVisualizer(model, k=(2,30),metric='calinski_harabasz', timings= True)
visualizer.fit(features) # Fit the data to the visualizer
visualizer.show()        # Plot

""" End of Pre-work - Determining the right number of clusters"""

""" Module 2a - Clustering (Works) """ 
# K Means Clustering
# 0 -> High Flight Risk, 1-> Low Flight Risk
model = KMeans(n_clusters=2, random_state=0) # To determine the number of clusters & random state is like a set.seed which ensures reproducibility in the results
kmeans = model.fit(features)
df["Flight Risk"] = kmeans.labels_

""" Module 2b - Random Forest (Works) """
labels = np.array(df['Flight Risk'])
features = np.array(df.iloc[:,1:24])
feature_list = list(df.iloc[:,1:24].columns)

# Split Data into train-test set
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.3, random_state=0)

# Run Random Forest
rf = RandomForestClassifier(n_estimators = 1000, random_state = 0)

# Train the model on training data
rf.fit(train_features, train_labels)

# Prediction & Model Performance Metrics for Model Validation
predictions = rf.predict(test_features)
conf_mat = confusion_matrix(test_labels, predictions)
print(conf_mat)
print(conf_mat[1][0])
acc = metrics.accuracy_score(test_labels, predictions)
fpr = conf_mat[1][0]/(conf_mat[1][0] + conf_mat[0][0]) # False Positive Rate
tnr = conf_mat[0][0]/(conf_mat[1][0] + conf_mat[0][0]) # True Negative Rate
tpr = conf_mat[1][1]/(conf_mat[1][1] + conf_mat[0][1]) # True Positive Rate
fnr = conf_mat[0][1]/(conf_mat[1][1] + conf_mat[0][1]) # False Negative Rate
print("Accuracy:", acc)
print("False Positive Rate:", fpr)
print("True Negative Rate:", tnr)
print("True Positive Rate:", tpr)
print("False Negative Rate:", fnr)

# Summary Analysis of Feature Importance
# Get numerical feature importances
importances = list(rf.feature_importances_)
# List of tuples with variable and importance
feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]
# Sort the feature importances by most important first
feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)
# Print out the feature and importances 
[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances];

# Individual Analysis Score by Survey Question Buckets Normalised to a Max Score of 100
# extract out the value of the importances and assign them 
df["w_total"] = (df["w_1"]*importances[4] + df["w_2"]*importances[5] + df["w_3"]*importances[6])*100/(5*sum(importances[4:7]))
df["o_total"] = (df["o_1"]*importances[7] + df["o_2"]*importances[8] + df["o_3"]*importances[9] + df["o_4"]*importances[10] + df["o_5"]*importances[11] + df["o_6"]*importances[12] + df["o_7"]*importances[13] + df["o_8"]*importances[14] + df["o_9"]*importances[15])*100/(5*sum(importances[7:16]))
df["p_total"] = (df["p_1n"]*importances[16] + df["p_2n"]*importances[17] + df["p_3n"]*importances[18] + df["p_4n"]*importances[19] + df["p_5a"]*importances[20] + df["p_6a"]*importances[21] + df["p_7a"]*importances[22])*100/(5*sum(importances[16:]))
df["EES"] = (df["w_1"]*importances[4] + df["w_2"]*importances[5] + df["w_3"]*importances[6] + df["o_1"]*importances[7] + df["o_2"]*importances[8] + df["o_3"]*importances[9] + df["o_4"]*importances[10] + df["o_5"]*importances[11] + df["o_6"]*importances[12] + df["o_7"]*importances[13] + df["o_8"]*importances[14] + df["o_9"]*importances[15] + df["p_1n"]*importances[16] + df["p_2n"]*importances[17] + df["p_3n"]*importances[18] + df["p_4n"]*importances[19] + df["p_5a"]*importances[20] + df["p_6a"]*importances[21] + df["p_7a"]*importances[22])*100/(5*sum(importances[4:]))

""" End of Module 2 - Model Training """