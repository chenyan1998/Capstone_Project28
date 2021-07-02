from typing import Collection
import pandas as pd
import pymongo
from pymongo import MongoClient
import json
import execute

# Making a Connection with MongoClient
client = MongoClient("mongodb+srv://Chenyan:Sutd30121998@cluster0.uxbcx.mongodb.net/test?authSource=admin&replicaSet=atlas-vtcq3b-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")

# Model database
db = client["ModelResults"]
# collection
collection= db["SvmModelResults"]
report_svm  = execute.report_svm 
report_svm.reset_index(inplace=True)
data_dict = report_svm.to_dict("records")
# Insert collection
collection.insert_many(data_dict)


# Individual Analysis report database
db = client["IndividualAnalysisResults"]
# collection
collection= db["Svm_Individual_Report"]
SVM_Individual_Report  = execute.new_results_individual 
SVM_Individual_Report.reset_index(inplace=True)
data_dict = SVM_Individual_Report.to_dict("records")
# Insert collection
collection.insert_many(data_dict)


# Department Analysis report database
db = client["DepartmentAnalysisResults"]
# collection
collection= db["Svm_Department_Report"]
Svm_Department_Report  = execute.new_results_department 
Svm_Department_Report.reset_index(inplace=True)
data_dict = Svm_Department_Report.to_dict("records")
# Insert collection
collection.insert_many(data_dict)

# Joblevel Analysis report database
db = client["JoblevelAnalysisResults"]
# collection
collection= db["Svm_Joblevel_Report"]
Svm_Joblevel_Report  = execute.new_results_department 
Svm_Joblevel_Report.reset_index(inplace=True)
data_dict = Svm_Joblevel_Report.to_dict("records")
# Insert collection
collection.insert_many(data_dict)

# Joblevel Analysis report database
db = client["JoblevelAnalysisResults"]
# collection
collection= db["Svm_Joblevel_Report"]
Svm_Joblevel_Report  = execute.new_results_job_level 
Svm_Joblevel_Report.reset_index(inplace=True)
data_dict = Svm_Joblevel_Report.to_dict("records")
# Insert collection
collection.insert_many(data_dict)

# Age Analysis report database
db = client["AgelevelAnalysisResults"]
# collection
collection= db["Svm_Age_Report"]
Svm_Age_Report  = execute.new_results_age 
Svm_Age_Report.reset_index(inplace=True)
data_dict = Svm_Age_Report.to_dict("records")
# Insert collection
collection.insert_many(data_dict)

# Organisation Analysis report database
db = client["OrganisationAnalysisResults"]
# collection
collection= db["Svm_Organisation_Report"]
Svm_Organisation_Report  = execute.new_results_age 
Svm_Organisation_Report.reset_index(inplace=True)
data_dict = Svm_Organisation_Report.to_dict("records")
# Insert collection
collection.insert_many(data_dict)

# # Charts report type1  database
# db = client["ChartResults"]
# # collection
# collection= db["Svm_Chart_Report_Type1"]
# Svm_Chart_Report_Type1  = execute.report_type_1 
# Svm_Chart_Report_Type1.reset_index(inplace=True)
# data_dict = Svm_Chart_Report_Type1.to_dict("records")
# # Insert collection
# collection.insert_many(data_dict)

# # Charts report type2 database
# db = client["ChartResults"]
# # collection
# collection= db["Svm_Chart_Report_Type2"]
# Svm_Chart_Report_Type2  = execute.report_type_2 
# Svm_Chart_Report_Type2.reset_index(inplace=True)
# data_dict = Svm_Chart_Report_Type2.to_dict("records")
# # Insert collection
# collection.insert_many(data_dict)

