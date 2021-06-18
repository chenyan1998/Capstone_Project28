""" Script for Prediction """

# Standard Libraries Imported
import pandas as pd
import pickle
import os

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

# Load Prediction Model
rf = pickle.load(open("rf.sav", 'rb'))

# Execute Prediction Model on New Survey Results
import results
new_results_individual, new_results_department, new_results_job_level, new_results_age, new_results_organisation = results.get_results(rf, new_df, new_features)

# List of all Dataframes to output
# new_results_individual
# new_results_department
# new_results_age
# new_results_job_level
# new_results_organisation
# new_drivers