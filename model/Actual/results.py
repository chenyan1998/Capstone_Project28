""" Script for Processing Survey Results with Loaded Prediction Model"""

import numpy as np

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

def get_results(model, df, features):
    
    # Introduce Try/Except Statement to capture scenarios where Supervised Learning Methods without Feature Importances are used
    
    try: 
        importances = list(model.feature_importances_)
        # Individual Analysis Score by Survey Question Buckets Normalised to a Max Score of 100
        # extract out the value of the importances and assign them
        df["w_total"] = (df["w_1"]*importances[2] + df["w_2"]*importances[3] + df["w_3"]*importances[4] + df["w_4"]*importances[5] + df["w_5"]*importances[6])*100/(5*sum(importances[2:7]))
        df["o_total"] = (df["o_1"]*importances[7] + df["o_2"]*importances[8] + df["o_4"]*importances[9] + df["o_5"]*importances[10])*100/(5*sum(importances[7:11]))
        df["p_total"] = (df["p_1n"]*importances[11] + df["p_2n"]*importances[12] + df["p_3n"]*importances[13] + df["p_4n"]*importances[14] + df["p_5a"]*importances[15] + df["p_6a"]*importances[16] + df["p_7a"]*importances[17])*100/(5*sum(importances[11:18]))
        df["c_total"] = (df["c_1"]*importances[18] + df["c_2"]*importances[19] + df["c_3"]*importances[20] + df["c_4"]*importances[21] + df["c_5"]*importances[22] + df["c_6"]*importances[23])*100/(5*sum(importances[18:]))
        df["EES"] = (df["w_1"]*importances[2] + df["w_2"]*importances[3] + df["w_3"]*importances[4] + df["w_4"]*importances[5] + df["w_5"]*importances[6] + 
                     df["o_1"]*importances[7] + df["o_2"]*importances[8] + df["o_4"]*importances[9] + df["o_5"]*importances[10] + 
                     df["p_1n"]*importances[11] + df["p_2n"]*importances[12] + df["p_3n"]*importances[13] + df["p_4n"]*importances[14] + df["p_5a"]*importances[15] + df["p_6a"]*importances[15] + df["p_7a"]*importances[17] + 
                     df["c_1"]*importances[18] + df["c_2"]*importances[19] + df["c_3"]*importances[20] + df["c_4"]*importances[21] + df["c_5"]*importances[22] + df["c_6"]*importances[23])*100/(5*sum(importances[2:]))
        
        # Note: o_3 is not included in scoring as it was dropped from prediction
        
        # Predict
        df["Flight Risk"] = model.predict(features)
        df['Flight Risk'] = np.where(df['Flight Risk'] == 1, "High Flight Risk", "Low Flight Risk")
        
        # Aggregate Results
        # i_1, i_2, i_3 and Flight Risk are dropped from summary statistics as they are categorical data
        results_department = df.drop(['Year', 'i_0', 'i_1', 'i_2', 'i_3', 'Flight Risk'], axis=1).groupby(['i_4']).agg(['mean', 'std', 'min','median','max'])
        results_job_level = df.drop(['Year', 'i_0', 'i_1', 'i_2', 'i_3', 'Flight Risk'], axis=1).groupby(['i_5']).agg(['mean', 'std', 'min','median','max'])
        results_age = df.drop(['Year', 'i_0', 'i_2', 'i_3', 'Flight Risk'], axis=1).groupby(['i_1']).agg(['mean', 'std', 'min','median','max'])
        results_organisation = df.drop(['Year', 'i_0', 'i_1', 'i_2', 'i_3', 'Flight Risk'], axis=1).describe()

        # Rename Columns
        results_department.columns = name_list
        results_job_level.columns = name_list
        results_age.columns = name_list

        # Individual Flags by Category -> If Category Score is in bottom 25%, assign flag for category
        df['w_flag'] = df['w_total'].apply(lambda x: 'True' if x <= df['w_total'].quantile(0.25) else 'False')
        df['o_flag'] = df['o_total'].apply(lambda x: 'True' if x <= df['o_total'].quantile(0.25) else 'False')
        df['p_flag'] = df['p_total'].apply(lambda x: 'True' if x <= df['p_total'].quantile(0.25) else 'False')
        df['c_flag'] = df['c_total'].apply(lambda x: 'True' if x <= df['c_total'].quantile(0.25) else 'False')

        # Individual Results
        results_individual = df
        
        # Reassign Year to Aggregate Results
        survey_year = results_individual.iloc[0,0]
        results_department["Year"] = survey_year
        results_job_level["Year"] = survey_year
        results_age["Year"] = survey_year
        results_organisation["Year"] = survey_year
        
    except AttributeError:
        # Predict
        df["Flight Risk"] = model.predict(features)
        df['Flight Risk'] = np.where(df['Flight Risk'] == 1, "High Flight Risk", "Low Flight Risk")
        
        # Individual Results
        results_individual = df
        
        # Aggregate Results
        # i_1, i_2, i_3 and Flight Risk are dropped from summary statistics as they are categorical data
        results_department = df.drop(['Year', 'i_0', 'i_1', 'i_2', 'i_3', 'Flight Risk'], axis=1).groupby(['i_4']).agg(['mean', 'std', 'min','median','max'])
        results_job_level = df.drop(['Year', 'i_0', 'i_1', 'i_2', 'i_3', 'Flight Risk'], axis=1).groupby(['i_5']).agg(['mean', 'std', 'min','median','max'])
        results_age = df.drop(['Year', 'i_0', 'i_2', 'i_3', 'Flight Risk'], axis=1).groupby(['i_1']).agg(['mean', 'std', 'min','median','max'])
        results_organisation = df.drop(['Year', 'i_0', 'i_1', 'i_2', 'i_3', 'Flight Risk'], axis=1).describe()
        
        # Rename Columns
        results_department.columns = name_list[0:115]
        results_job_level.columns = name_list[0:115]
        results_age.columns = name_list[0:115]
        
        # Reassign Year to Aggregate Results
        survey_year = results_individual.iloc[0,0]
        results_department["Year"] = survey_year
        results_job_level["Year"] = survey_year
        results_age["Year"] = survey_year
        results_organisation["Year"] = survey_year

    return results_individual, results_department, results_job_level, results_age, results_organisation