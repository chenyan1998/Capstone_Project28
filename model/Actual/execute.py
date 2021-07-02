""" Script for Prediction """


import pickle
import os
# Standard Libraries Imported
import pandas as pd
from sklearn import svm
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
import pickle
import os
from pymongo import MongoClient

# Establish Connection with Database
# client = MongoClient(host=, port=)
# model_data = client["name of database"]

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'Employee Engagement Survey(1-237).xlsx')

# Import Model Data
model_data = pd.read_excel(filename, header = None)

# Cleans last question survey data for model training
import clean_last
drivers = clean_last.clean_last_qns(model_data)

# Clean remaining questions survey data for model training
import clean_others
df, features = clean_others.clean(model_data)

# Load New Survey Results
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'Employee Engagement Survey(1-44).xlsx')
new_data = pd.read_excel(filename, header = None)

# Clean Survey Results
import clean_last
new_drivers = clean_last.clean_last_qns(new_data)

import clean_others
new_df, new_features = clean_others.clean(new_data)

# Note: i_3 and o_3 are dropped for model improvements
new_features = new_features.drop(["i_3", "o_3"], axis=1)

# Cluster data points and assign labels for supervised learning
import clustering
labels, features, feature_list, df = clustering.cluster(df, features)

# Train SVM Model
import train_svm
sv, report_svm = train_svm.train(features, feature_list, labels, df)

# print("sv : ", sv)
# print("rep: ", report_svm)
# Load Prediction Model
# rf = pickle.load(open("rf.sav", 'rb'))

# Execute Prediction Model on New Survey Results
import results
new_results_individual, new_results_department, new_results_job_level, new_results_age, new_results_organisation = results.get_results(sv, new_df, new_features)

# print("new_results_individual : ", new_results_individual)
# List of all Dataframes to output
# new_results_individual
# new_results_department
# new_results_age
# new_results_job_level
# new_results_organisation
# new_drivers

metric_list = ['w_1_mean', 'w_2_mean', 'w_3_mean', 'w_4_mean', 'w_5_mean', 
             'o_1_mean', 'o_2_mean', 'o_3_mean', 'o_4_mean', 'o_5_mean', 
             'p_1n_mean', 'p_2n_mean', 'p_3n_mean', 'p_4n_mean', 
             'p_5a_mean', 'p_6a_mean', 'p_7a_mean', 
             'c_1_mean', 'c_2_mean', 'c_3_mean', 'c_4_mean', 'c_5_mean', 'c_6_mean', 
             'w_total_mean','o_total_mean', 'p_total_mean', 'c_total_mean', 'EES_mean'
             ]




# # Report Type 1 - Generate All Survey Responses for Each Employee i.e. One Report for Each Employee
# # Report Type 2 - Generate Summary Survey Responses for Each Employee i.e. One Report for Each Employee
# report_type_1 = {}
# report_type_2 = {}

# for i in range(0, len(new_results_individual.index)):
#     temp_1 = new_results_individual.iloc[i,7:30]
#     temp_2 = new_results_individual.iloc[i,30:]
#     employee_id = new_results_individual.iloc[i,1]
#     report_type_1.update({employee_id: temp_1})
#     report_type_2.update({employee_id: temp_2})

# keys_values1 = report_type_1.items()
# report_type_1 = {str(key): str(value) for key, value in keys_values1}

# keys_values2 = report_type_2.items()
# report_type_2 = {str(key): str(value) for key, value in keys_values2}

# report_type_1 = pd.DataFrame(report_type_1.items())
# report_type_2 = pd.DataFrame(report_type_2.items())

# print("new_results_individual : ", new_results_individual)
# print("report_type1 : ", report_type_1)
# print("report_type2 : ", report_type_2)

# # Report Type 3 - Comparison Report between age, job level, department
# report_type_3_age = {}
# report_type_3_job_level = {}
# report_type_3_department = {}
# for i in metric_list:
#     temp_1 = new_results_age[i]
#     temp_2 = new_results_job_level[i]
#     temp_3 = new_results_department[i]
#     report_type_3_age.update({i: temp_1})
#     report_type_3_job_level.update({i: temp_2})
#     report_type_3_department.update({i: temp_3})

# # Report Type 4 - Department Level Survey Report by Questions
# # Report Type 5 - Department Level Summary Report by Questions
# report_type_4_wellbeing = {}
# report_type_4_opinions = {}
# report_type_4_personality = {}
# report_type_4_core_values = {}
# report_type_5 = {}
# temp = new_results_department[metric_list]

# for i in range(0, len(new_results_department.index)):
#     w_temp = temp.iloc[i,0:5]
#     o_temp = temp.iloc[i,5:10]
#     p_temp = temp.iloc[i,10:17]
#     c_temp = temp.iloc[i,17:23]
#     temp_1 = temp.iloc[i,23:]
#     key = temp.index[i]
#     report_type_4_wellbeing.update({key: w_temp})
#     report_type_4_opinions.update({key: o_temp})
#     report_type_4_personality.update({key: p_temp})
#     report_type_4_core_values.update({key: c_temp})
#     report_type_5.update({key: temp_1})     