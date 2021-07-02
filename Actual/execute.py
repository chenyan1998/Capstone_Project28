""" Script for Prediction """

# Standard Libraries Imported
import pandas as pd
import pickle
import os
import codecs
import csv
import pymongo
from matplotlib import pyplot as plt
import numpy as np

# Actual Importing of Data for Production
# 链接mongo数据库
mongo_client = pymongo.MongoClient('mongodb+srv://Chenyan:Sutd30121998@cluster0.uxbcx.mongodb.net/test?authSource=admin&replicaSet=atlas-vtcq3b-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
db = mongo_client.Survey
my_collection = db['Survey2'] 
 
list_tmp = []
for r in my_collection.find():
    list_tmp.append(r)
model_data_1 = pd.DataFrame(list_tmp)
model_data_1 = model_data_1.T.reset_index(drop=True).T

# =============================================================================
# # Importing of Data for Local Testing
# here = os.path.dirname(os.path.abspath(__file__))
# 
# filename = os.path.join(here, 'Employee Engagement Survey(1-237).xlsx')
# 
# model_data = pd.read_excel(filename, header = None)
# =============================================================================

# Clean Survey Results
import clean_last
new_drivers = clean_last.clean_last_qns(model_data_1)

import clean_others
new_df, new_features = clean_others.clean(model_data_1)

# Note: i_3 and o_3 are dropped for model improvements
new_features = new_features.drop(["i_3", "o_3"], axis=1)

# Load Prediction Model
rf = pickle.load(open("rf.sav", 'rb'))

# Execute Prediction Model on New Survey Results
import results
new_results_individual, new_results_department, new_results_job_level, new_results_age, new_results_organisation = results.get_results(rf, new_df, new_features)

metric_list = ['w_1_mean', 'w_2_mean', 'w_3_mean', 'w_4_mean', 'w_5_mean', 
             'o_1_mean', 'o_2_mean', 'o_3_mean', 'o_4_mean', 'o_5_mean', 
             'p_1n_mean', 'p_2n_mean', 'p_3n_mean', 'p_4n_mean', 
             'p_5a_mean', 'p_6a_mean', 'p_7a_mean', 
             'c_1_mean', 'c_2_mean', 'c_3_mean', 'c_4_mean', 'c_5_mean', 'c_6_mean', 
             'w_total_mean','o_total_mean', 'p_total_mean', 'c_total_mean', 'EES_mean'
             ]
        
# Report Type 1 - Generate All Survey Responses for Each Employee i.e. One Report for Each Employee
# Report Type 2 - Generate Summary Survey Responses for Each Employee i.e. One Report for Each Employee
report_type_1 = {}
report_type_2 = {}
for i in range(0, len(new_results_individual.index)):
    temp_1 = new_results_individual.iloc[i,7:30]
    temp_2 = new_results_individual.iloc[i,30:]
    employee_id = new_results_individual.iloc[i,1]
    report_type_1.update({employee_id: temp_1})
    report_type_2.update({employee_id: temp_2})

# Report Type 3 - Comparison Report between age, job level, department
report_type_3_age = {}
report_type_3_job_level = {}
report_type_3_department = {}
for i in metric_list:
    temp_1 = new_results_age[i]
    temp_2 = new_results_job_level[i]
    temp_3 = new_results_department[i]
    report_type_3_age.update({i: temp_1})
    report_type_3_job_level.update({i: temp_2})
    report_type_3_department.update({i: temp_3})

# Report Type 4 - Department Level Survey Report by Questions
# Report Type 5 - Department Level Summary Report by Questions
report_type_4_wellbeing = {}
report_type_4_opinions = {}
report_type_4_personality = {}
report_type_4_core_values = {}
report_type_5 = {}
temp = new_results_department[metric_list]

for i in range(0, len(new_results_department.index)):
    w_temp = temp.iloc[i,0:5]
    o_temp = temp.iloc[i,5:10]
    p_temp = temp.iloc[i,10:17]
    c_temp = temp.iloc[i,17:23]
    temp_1 = temp.iloc[i,23:]
    key = temp.index[i]
    report_type_4_wellbeing.update({key: w_temp})
    report_type_4_opinions.update({key: o_temp})
    report_type_4_personality.update({key: p_temp})
    report_type_4_core_values.update({key: c_temp})
    report_type_5.update({key: temp_1})
    
""" List of all Dataframes to output to Tables on frontend """
# =============================================================================
# new_results_individual
# new_results_department
# new_results_age
# new_results_job_level
# new_results_organisation
# new_drivers
# =============================================================================

""" List of all Reports to output to Charts on frontend """
# =============================================================================
# report_type_1
# report_type_2
# report_type_3_age
# report_type_3_job_level
# report_type_3_department
# report_type_4_wellbeing
# report_type_4_opinions
# report_type_4_personality
# report_type_4_core_values
# report_type_5
# =============================================================================

""" Upload Results to MongoDB """
# =============================================================================
# db.update(report_type_1, upsert = True)
# db.update(report_type_2, upsert = True)
# db.update(report_type_3_age, upsert = True)
# db.update(report_type_3_department, upsert = True)
# db.update(report_type_3_job_level, upsert = True)
# db.update(report_type_4_wellbeing, upsert = True)
# db.update(report_type_4_opinions, upsert = True)
# db.update(report_type_4_personality, upsert = True)
# db.update(report_type_4_core_values, upsert = True)
# db.update(report_type_5, upsert = True)
# 
# =============================================================================
""" Data Visualisation & Analysis for Review 3 Purposes """
# =============================================================================
# # df.plot(kind = 'bar', x = '', y = '')
# 
# # Department Comparison for EES
# ees = report_type_3_department.get("EES_mean")
# ees.plot(kind = 'bar')
# plt.savefig("ees.png", bbox_inches = 'tight')
# 
# # Radar Chart for Individual
# individual = report_type_2.get("10051")
# categories = ["Wellbeing", "Opinions", " Personality", "Core Values", "EES Score"]
# data = individual[0:5]
# 
# fig = plt.figure()
# ax = fig.add_subplot(111, projection="polar")
# 
# # theta has 5 different angles, and the first one repeated
# theta = np.arange(len(data) + 1) / float(len(data)) * 2 * np.pi
# # values has the 5 values from 'Col B', with the first element repeated
# values = data
# values = np.append(values, data[0])
# 
# # draw the polygon and the mark the points for each angle/value combination
# l1, = ax.plot(theta, values, color="C2", marker="o", label="Name of Col B")
# plt.xticks(theta[:-1], categories, color='grey', size=12)
# ax.tick_params(pad=10) # to increase the distance of the labels to the plot
# # fill the area of the polygon with green and some transparency
# ax.fill(theta, values, 'green', alpha=0.1)
# ax.set_ylim(0,100)
# # plt.legend() # shows the legend, using the label of the line plot (useful when there is more than 1 polygon)
# plt.title("Employee 10051")
# plt.show()
# 
# plt.savefig("radar.png", bbox_inches = 'tight')
# =============================================================================