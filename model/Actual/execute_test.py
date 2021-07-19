""" Script for Execution """

# Standard Libraries Imported
import pandas as pd
import pickle
import pymongo

# Actual Importing of Data for Production
# 链接mongo数据库
mongo_client = pymongo.MongoClient('mongodb+srv://Chenyan:Sutd30121998@cluster0.uxbcx.mongodb.net/test?authSource=admin&replicaSet=atlas-vtcq3b-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
db = mongo_client.Survey
my_collection = db['Survey1'] 
 
list_tmp = []
for r in my_collection.find():
    list_tmp.append(r)
data = pd.DataFrame(list_tmp)
data = data.T.reset_index(drop=True).T

# Clean Survey Results
import clean_last
new_drivers = clean_last.clean_last_qns(data)

import clean_others
new_df, new_features = clean_others.clean(data)

# Note: i_3 and o_3 are dropped for model improvements
new_features = new_features.drop(["i_3", "o_3"], axis=1)

# Load Prediction Model
rf = pickle.load(open("rf.sav", 'rb'))

# Execute Prediction Model on New Survey Results
import results
new_results_individual, new_results_department, new_results_job_level, new_results_age, new_results_organisation = results.get_results(rf, new_df, new_features)

# Generate Report for Frontend & Storing to Database
import report
report_type_3_age, report_type_3_job_level, report_type_3_department, report_type_4_wellbeing, report_type_4_opinions, report_type_4_personality, report_type_4_core_values, report_type_5 = report.gen_report(new_results_individual, new_results_age, new_results_job_level, new_results_department)

# Convert Index to Column for Storage in MongoDB as unique identifier
new_results_age['Age Category'] = new_results_age.index
new_results_department['Department'] = new_results_department.index
new_results_job_level['Job Level'] = new_results_job_level.index

import data_upload
data_upload.upload(report_type_4_wellbeing, report_type_4_opinions, report_type_4_personality, report_type_4_core_values, new_results_individual, new_results_department, new_results_job_level, new_results_age)

""" Following Reports are Deprecated """
# =============================================================================
# # Collection 1 - Age
# collection = db["report"]
# for i , j in report_type_3_age.items():
#     year = str(j.iloc[0,5])
#     j = j.drop(["Year"], axis = 1)
#     x = list(j)
#     y = j.iloc[0].tolist()
#     temp = {'name': "Report 3 - Age", 
#             "metric": "wellbeing", 
#             "department": "NA", 
#             "year": year,
#             "report_format": "chart",
#             "question": i,
#             "label_x": "Question",
#             "label_y": "Mean Score",
#             "data_x": x, 
#             "data_y": y}
#     collection.replace_one({"question": i, 'year': year}, temp, upsert = True)
# 
# # Collection 2 - Job Level
# collection = db["RF_Job_Report"]
# for i , j in report_type_3_job_level.items():
#     year = str(j.iloc[0,7])
#     j = j.drop(["Year"], axis = 1)
#     x = list(j)
#     y = j.iloc[0].tolist()
#     temp = {"x": x, "y": y, "Question": i, 'Year': year}
#     collection.replace_one({"Question": i, 'Year': year}, temp, upsert = True)
#     
# # Collection 3 - Department
# collection = db["RF_Department_Report"]
# for i , j in report_type_3_department.items():
#     year = str(j.iloc[0,11])
#     j = j.drop(["Year"], axis = 1)
#     x = list(j)
#     y = j.iloc[0].tolist()
#     temp = {"x": x, "y": y, "Question": i, 'Year': year}
#     collection.replace_one({"Question": i, 'Year': year}, temp, upsert = True)
    
# Update Report Type 5 Results to MongoDB 
# # Collection 1 - Summary
# collection = db["RF_Summary_Report"]
# for i , j in report_type_5.items():
#     year = str(j.iloc[0,5])
#     j = j.drop(["Year"], axis = 1)
#     x = list(j)
#     y = j.iloc[0].tolist()
#     temp = {"x": x, "y": y, "Department": i, 'Year': year}
#     collection.replace_one({"Department": i, 'Year': year}, temp, upsert = True)
# =============================================================================