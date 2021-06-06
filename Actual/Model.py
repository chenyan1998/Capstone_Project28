""" Script for Model Training """

# Standard Libraries Imported
import pandas as pd
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
import pickle
import os

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'Employee Engagement Survey(1-151).xlsx')

# Import Model Data
model_data = pd.read_excel(filename, header = None)

# Cleans last question survey data for model training
import clean_last
drivers = clean_last.clean_last_qns(model_data)

# Clean remaining questions survey data for model training
import clean_others
df, features = clean_others.clean(model_data)

""" Start of Determine the right number of clusters """

### Run this code each time the model needs to be changed 
model = KMeans(random_state=0)

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

""" End of Determine the right number of clusters """

# Cluster data points and assign labels for supervised learning
import clustering
labels, features, feature_list, df = clustering.cluster(df, features)

# Execute KFolds Cross Validation for Model Tuning and Improvements
import kfolds
acc_range = kfolds.cv(features, feature_list, labels, df)

# Train Random Forest Model
import train_rf
rf, df = train_rf.train(features, feature_list, labels, df)

# Train Decision Tree Model
import train_dt
dt = train_dt.train(features, feature_list, labels, df)

# Train KNN Classifier Model
import train_knn
knn = train_knn.train(features, feature_list, labels, df)

# Train SVM Model
import train_svm
sv = train_svm.train(features, feature_list, labels, df)

# Train NBC Model
import train_nbc
nbc = train_nbc.train(features, feature_list, labels, df)

""" Start of Internal Checking of Output Dataframe & Predictions """
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

""" End of Internal Checking of Output Dataframe & Predictions """

# Save Trained Model for Future Execution
pickle.dump(rf, open("rf.sav", "wb"))
pickle.dump(dt, open("dt.sav", "wb"))
pickle.dump(sv, open("sv.sav", "wb"))
pickle.dump(knn, open("knn.sav", "wb"))
pickle.dump(nbc, open("nbc.sav", "wb"))

# Note for Final Script:
# To remove all but one supervised learning modules once finalised
# To remove Module 3 once code is finalised

# To do
# Cross Validation and Model Tuning