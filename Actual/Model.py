""" Script for Model Training """

# Standard Libraries Imported
import pandas as pd
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
import pickle
import pymongo

# Actual Importing of Data for Production
# # 链接mongo数据库
mongo_client = pymongo.MongoClient('mongodb+srv://Chenyan:Sutd30121998@cluster0.uxbcx.mongodb.net/test?authSource=admin&replicaSet=atlas-vtcq3b-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
db = mongo_client.Survey
my_collection = db['Survey1'] 
 
list_tmp = []
for r in my_collection.find():
    list_tmp.append(r)
model_data =pd.DataFrame(list_tmp)
model_data = model_data.T.reset_index(drop=True).T

# Cleans last question survey data for model training
import clean_last
drivers = clean_last.clean_last_qns(model_data)

# Clean remaining questions survey data for model training
import clean_others
df, features = clean_others.clean(model_data)

""" Start of Determine the right number of clusters """

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
acc_range = kfolds.cv(features, labels)

# Train Random Forest Model
import train_rf
rf, report_rf = train_rf.train(features, feature_list, labels, df)

# Train Decision Tree Model
import train_dt
dt, report_dt = train_dt.train(features, feature_list, labels, df)

# Train KNN Classifier Model
import train_knn
knn, report_knn = train_knn.train(features, feature_list, labels, df)

# Train SVM Model
import train_svm
sv, report_svm = train_svm.train(features, feature_list, labels, df)

# Train NBC Model
import train_nbc
nbc, report_nbc = train_nbc.train(features, feature_list, labels, df)

# Save Trained Model for Future Execution
pickle.dump(rf, open("rf.sav", "wb"))
pickle.dump(dt, open("dt.sav", "wb"))
pickle.dump(knn, open("knn.sav", "wb"))
pickle.dump(sv, open("sv.sav", "wb"))
pickle.dump(nbc, open("nbc.sav", "wb"))
