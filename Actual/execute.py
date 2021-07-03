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

# =============================================================================
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
# db.update(report_type_3_age, upsert = True)
# db.update(report_type_3_department, upsert = True)
# db.update(report_type_3_job_level, upsert = True)
# db.update(report_type_4_wellbeing, upsert = True)
# db.update(report_type_4_opinions, upsert = True)
# db.update(report_type_4_personality, upsert = True)
# db.update(report_type_4_core_values, upsert = True)
# db.update(report_type_5, upsert = True)