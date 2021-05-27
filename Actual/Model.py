# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:50:30 2021

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

filename = os.path.join(here, 'Employee Engagement Survey(1-33).xlsx')

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
# For i_2 and i_3, both "Below 2 years" and "Below 3 years" are considered the same category and this change was made as the survey option was corrected after the survey was launched
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

""" Start of Module 2a - Clustering (Works) """ 
# K Means Clustering
# 0 -> High Flight Risk, 1-> Low Flight Risk
model = KMeans(n_clusters=2, random_state=0) # To determine the number of clusters & random state is like a set.seed which ensures reproducibility in the results
kmeans = model.fit(features)
df["Flight Risk"] = kmeans.labels_

""" End of Module 2a - Clustering (Works) """

""" Start of Module 2b - Random Forest (Works) """
labels = np.array(df['Flight Risk'])
features = np.array(df.drop(['i_0', 'i_4', 'i_5', 'Flight Risk'], axis=1))
feature_list = list(df.drop(['i_0', 'i_4', 'i_5', 'Flight Risk'], axis=1))

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
df["w_total"] = (df["w_1"]*importances[3] + df["w_2"]*importances[4] + df["w_3"]*importances[5] + df["w_4"]*importances[6] + df["w_5"]*importances[7])*100/(5*sum(importances[3:8]))
df["o_total"] = (df["o_1"]*importances[8] + df["o_2"]*importances[9] + df["o_3"]*importances[10] + df["o_4"]*importances[11] + df["o_5"]*importances[12])*100/(5*sum(importances[8:13]))
df["p_total"] = (df["p_1n"]*importances[13] + df["p_2n"]*importances[14] + df["p_3n"]*importances[15] + df["p_4n"]*importances[16] + df["p_5a"]*importances[17] + df["p_6a"]*importances[18] + df["p_7a"]*importances[19])*100/(5*sum(importances[13:20]))
df["c_total"] = (df["c_1"]*importances[20] + df["c_2"]*importances[21] + df["c_3"]*importances[22] + df["c_4"]*importances[23] + df["c_5"]*importances[24] + df["c_6"]*importances[25])*100/(5*sum(importances[20:]))
df["EES"] = (df["w_1"]*importances[3] + df["w_2"]*importances[4] + df["w_3"]*importances[5] + df["w_4"]*importances[6] + df["w_5"]*importances[7] + df["o_1"]*importances[8] + df["o_2"]*importances[9] + df["o_3"]*importances[10] + df["o_4"]*importances[11] + df["o_5"]*importances[12] + df["p_1n"]*importances[13] + df["p_2n"]*importances[14] + df["p_3n"]*importances[15] + df["p_4n"]*importances[16] + df["p_5a"]*importances[17] + df["p_6a"]*importances[18] + df["p_7a"]*importances[19] + df["c_1"]*importances[20] + df["c_2"]*importances[21] + df["c_3"]*importances[22] + df["c_4"]*importances[23] + df["c_5"]*importances[24] + df["c_6"]*importances[25])*100/(5*sum(importances[3:]))

""" End of Module 2b - Random Forest (Works) """

""" End of Module 2 - Model Training """

""" Start of Module 3 - Results & Query (Works) """
# Aggregate Results
# i_1, i_2, i_3 and Flight Risk are dropped from summary statistics as they are categorical data
results_department = df.drop(['i_1', 'i_2', 'i_3', 'Flight Risk'], axis=1).groupby(['i_4']).agg(['mean', 'std', 'min','median','max'])
results_job_level = df.drop(['i_1', 'i_2', 'i_3', 'Flight Risk'], axis=1).groupby(['i_5']).agg(['mean', 'std', 'min','median','max'])
results_age = df.drop(['i_2', 'i_3', 'Flight Risk'], axis=1).groupby(['i_1']).agg(['mean', 'std', 'min','median','max'])

# Renaming Column Names for Results Dataframe
name_list = ['w_1_mean', 'w_1_std', 'w_1_min', 'w_1_median', 'w_1_max',
             'w_2_mean', 'w_2_std', 'w_2_min', 'w_2_median', 'w_2_max',
             'w_3_mean', 'w_3_std', 'w_3_min', 'w_3_median', 'w_3_max',
             'w_4_mean', 'w_4_std', 'w_4_min', 'w_4_median', 'w_4_max',
             'w_5_mean', 'w_5_std', 'w_5_min', 'w_5_median', 'w_5_max',
             'o_1_mean', 'o_1_std', 'o_1_min', 'o_1_median', 'o_1_max',
             'o_2_mean', 'o_2_std', 'o_2_min', 'o_2_median', 'o_2_max',
             'o_3_mean', 'o_3_std', 'o_3_min', 'o_3_median', 'o_3_max',
             'o_4_mean', 'o_4_std', 'o_4_min', 'o_4_median', 'o_4_max',
             'o_5_mean', 'o_5_std', 'o_5_min', 'o_5_median', 'o_5_max',
             'p_1n_mean', 'p_1n_std', 'p_1n_min', 'p_1n_median', 'p_1n_max',
             'p_2n_mean', 'p_2n_std', 'p_2n_min', 'p_2n_median', 'p_2n_max',
             'p_3n_mean', 'p_3n_std', 'p_3n_min', 'p_3n_median', 'p_3n_max',
             'p_4n_mean', 'p_4n_std', 'p_4n_min', 'p_4n_median', 'p_4n_max',
             'p_5a_mean', 'p_5a_std', 'p_5a_min', 'p_5a_median', 'p_5a_max',
             'p_6a_mean', 'p_6a_std', 'p_6a_min', 'p_6a_median', 'p_6a_max',
             'p_7a_mean', 'p_7a_std', 'p_7a_min', 'p_7a_median', 'p_7a_max',
             'c_1_mean', 'c_1_std', 'c_1_min', 'c_1_median', 'c_1_max',
             'c_2_mean', 'c_2_std', 'c_2_min', 'c_2_median', 'c_2_max',
             'c_3_mean', 'c_3_std', 'c_3_min', 'c_3_median', 'c_3_max',
             'c_4_mean', 'c_4_std', 'c_4_min', 'c_4_median', 'c_4_max',
             'c_5_mean', 'c_5_std', 'c_5_min', 'c_5_median', 'c_5_max',
             'c_6_mean', 'c_6_std', 'c_6_min', 'c_6_median', 'c_6_max',
             'w_total_mean', 'w_total_std', 'w_total_min', 'w_total_median', 'w_total_max',
             'o_total_mean', 'o_total_std', 'o_total_min', 'o_total_median', 'o_total_max',
             'p_total_mean', 'p_total_std', 'p_total_min', 'p_total_median', 'p_total_max',
             'c_total_mean', 'c_total_std', 'c_total_min', 'c_total_median', 'c_total_max',
             'EES_mean', 'EES_std', 'EES_min', 'EES_median', 'EES_max',
             ]

results_department.columns = name_list
results_job_level.columns = name_list
results_age.columns = name_list

# Note for querying that results_organisation have a different row and column structure compared to results_department and results_job_level
results_organisation = df.drop(['i_1', 'i_2', 'i_3', 'Flight Risk'], axis=1).describe()

# Individual Results
results_individual = df

""" End of Module 3 - Results & Query (Works) """

# To do
# 1. Data Cleaning of Others Responses for Department/Job Level Columns & Last Question
# 2. Results for Last Question