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

""" Segmented Results for Frontend """
# Update Age Level Analysis Results to MongoDB
db = mongo_client["Segment_Age_Results"]
# Collection
collection = db["RF_Age_Report"]
temp_lst = []
for i in report_type_3_age:
    value = report_type_3_age.get(i)
    temp = value.to_dict("records")
    temp_lst.append(temp[0])
# Insert collection
collection.insert_many(temp_lst)

# Update Job Level Analysis Results to MongoDB
db = mongo_client["Segment_Job_Results"]
# Collection
collection = db["RF_Job_Report"]
temp_lst = []
for i in report_type_3_job_level:
    value = report_type_3_job_level.get(i)
    temp = value.to_dict("records")
    temp_lst.append(temp[0])
# Insert collection
collection.insert_many(temp_lst)

# Update Department Level Analysis Results to MongoDB
db = mongo_client["Segment_Department_Results"]
# Collection
collection = db["RF_Department_Report"]
temp_lst = []
for i in report_type_3_department:
    value = report_type_3_department.get(i)
    temp = value.to_dict("records")
    temp_lst.append(temp[0])
# Insert collection
collection.insert_many(temp_lst)

# Update Wellbeing Level Analysis Results to MongoDB
db = mongo_client["Segment_Wellbeing_Results"]
# Collection
collection = db["RF_Wellbeing_Report"]
temp_lst = []
for i in report_type_4_wellbeing:
    value = report_type_4_wellbeing.get(i)
    temp = value.to_dict("records")
    temp_lst.append(temp[0])
# Insert collection
collection.insert_many(temp_lst)

# Update Opinion Level Analysis Results to MongoDB
db = mongo_client["Segment_Opinions_Results"]
# Collection
collection = db["RF_Opinions_Report"]
temp_lst = []
for i in report_type_4_opinions:
    value = report_type_4_opinions.get(i)
    temp = value.to_dict("records")
    temp_lst.append(temp[0])
# Insert collection
collection.insert_many(temp_lst)

# Update Personality Level Analysis Results to MongoDB
db = mongo_client["Segment_Personality_Results"]
# Collection
collection = db["RF_Personality_Report"]
temp_lst = []
for i in report_type_4_personality:
    value = report_type_4_personality.get(i)
    temp = value.to_dict("records")
    temp_lst.append(temp[0])
# Insert collection
collection.insert_many(temp_lst)

# Update Core Values Level Analysis Results to MongoDB
db = mongo_client["Segment_Core_Values_Results"]
# Collection
collection = db["RF_Core_Values_Report"]
temp_lst = []
for i in report_type_4_core_values:
    value = report_type_4_core_values.get(i)
    temp = value.to_dict("records")
    temp_lst.append(temp[0])
# Insert collection
collection.insert_many(temp_lst)

# Update Department Summary Results to MongoDB
db = mongo_client["Summary_Results"]
# Collection
collection = db["RF_Summary_Report"]
temp_lst = []
for i in report_type_5:
    value = report_type_5.get(i)
    temp = value.to_dict("records")
    temp_lst.append(temp[0])
# Insert collection
collection.insert_many(temp_lst)

""" Raw Results for Frontend Table View """
# Individual Analysis report database
db = mongo_client["Table_Individual"]
# collection
collection= db["RF_Individual_Report"]
RF_Individual_Report = new_results_individual 
data_dict = new_results_individual.to_dict("records")
# Insert collection
collection.insert_many(data_dict)

# Department Analysis report database
db = mongo_client["Table_Department"]
# collection
collection= db["RF_Department_Report"]
RF_Department_Report = new_results_department 
data_dict = RF_Department_Report.to_dict("records")
# Insert collection
collection.insert_many(data_dict)
 
# Joblevel Analysis report database
db = mongo_client["Table_Job"]
# collection
collection= db["RF_Job_Report"]
RF_Joblevel_Report = new_results_job_level 
data_dict = RF_Joblevel_Report.to_dict("records")
# Insert collection
collection.insert_many(data_dict)
 
# Age Analysis report database
db = mongo_client["Table_Age"]
# collection
collection= db["RF_Age_Cat_Report"]
RF_Age_Report = new_results_age 
data_dict = RF_Age_Report.to_dict("records")
# Insert collection
collection.insert_many(data_dict)
 
# Drivers Report Database
db = mongo_client["drivers"]
# collection
collection= db["Drivers_Report"]
drivers = pd.DataFrame(new_drivers)
drivers = drivers.T
data_dict = drivers.to_dict("records")
# Insert collection
collection.insert_many(data_dict)
