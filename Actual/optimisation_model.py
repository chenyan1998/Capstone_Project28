""" Script for Bayesian Optimisation of Random Forest Algorithm """

# Standard Libraries Imported
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from hyperopt import hp, tpe, fmin, Trials
import pymongo
import pandas as pd
import numpy as np

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

# Cluster data points and assign labels for supervised learning
import clustering
labels, features, feature_list, df = clustering.cluster(df, features)

# Split into Train-Test Set
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.3, random_state=0)

# Objective Function
def objective_function(params):
    
    # Run KFolds to obtain CV Score
    kfolds = KFold(n_splits = 10, random_state = 0)
    rf = RandomForestClassifier()
    cv = cross_val_score(rf, train_features, train_labels, cv = kfolds)
    best_score = max(cv)
    
    # Minimise Loss
    loss_function = 1 - best_score
    return loss_function

 # Domain Space
 # =============================================================================
 # Hyperparameters to tune
 # 1. n_estimators - Based on research, ideal number of trees often lie between 64 - 128
 # 2. max_depth
 # 3. max_features
 # 4. min_samples_split
 # =============================================================================
space = {
        'n_estimators': hp.quniform("n_estimators", 64, 256, 1), # Based on research, ideal number of trees often lie between 64 - 128
        'max_depth': hp.quniform("max_depth", 3, 10, 1), # Balance between complexity & overfitting
        'max_features': hp.quniform("max_features", 2, 24, 1),
        'min_samples_split': hp.quniform("min_samples_split", 2, 15, 1)
    }
 
bayes_trials = Trials()

# Optimisation Algorithm
rstate = np.random.RandomState(64)
best = fmin(fn = objective_function, space = space, algo = tpe.suggest, max_evals = 500, trials = bayes_trials, rstate = rstate)

# Run Random Forest
rf = RandomForestClassifier(n_estimators = int(best['n_estimators']), 
                            max_depth = int(best['max_depth']),
                            max_features = int(best['max_features']), 
                            min_samples_split = int(best['min_samples_split']),
                            random_state = 6) 

kfolds = RepeatedKFold(n_splits = 10, n_repeats = 50, random_state = 0)
score = cross_val_score(rf, features, labels, cv = kfolds)
# Return Range of Accuracy at 95% Confidence
alpha = 0.95                         
p = ((1.0-alpha)/2.0) * 100             
lower = max(0.0, np.percentile(score, p))  
p = (alpha+((1.0-alpha)/2.0)) * 100
upper = min(1.0, np.percentile(score, p))
confint = (lower*100, upper*100)

# Train the model on training data
rf.fit(train_features, train_labels)
    
# Prediction & Model Performance Metrics for Model Validation
predictions = rf.predict(test_features)
conf_mat = confusion_matrix(test_labels, predictions)
print(conf_mat)
    
# Accuracy is the number of correct predictions
# Precision = True_Positive/ (True_Positive+ False_Positive) -> Measures % Correctly Predicted Class
# Recall = True_Positive/ (True_Positive+ False_Negative) -> Measures the fraction of samples from a class which are correctly predicted by the model
# F1 Score is the harmonic mean of Precision and recall for each category
# Support is the number of occurences for each class
print("Random Forest Performance")
report = classification_report(test_labels, predictions, output_dict=True)
print(classification_report(test_labels, predictions))
report = pd.DataFrame(report).transpose()