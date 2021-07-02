import pandas as pd
import results
import execute 
new_results_individual, new_results_department, new_results_job_level, new_results_age, new_results_organisation = results.get_results(execute.sv, execute.new_df, execute.new_features)


# Total Flight Risk Chart Data
Flight_risk_dataframe = new_results_individual.loc[:,['Flight Risk']]
high_risk_number = (Flight_risk_dataframe['Flight Risk'] == 1).sum()
low_risk_number = (Flight_risk_dataframe['Flight Risk'] == 0).sum()
print("high_risk_number :", high_risk_number)
print("low_risk_number :", low_risk_number)
# print("Flight_risk_dataframe", Flight_risk_dataframe)
 