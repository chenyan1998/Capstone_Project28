""" Script for Model Training - Random Forest """

# Standard Libraries Imported
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from hyperopt import hp, tpe, fmin, Trials
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
import numpy as np

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

def train(features, feature_list, labels, df):

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
    
    # Run Random Forest
    # rf = RandomForestClassifier(n_estimators = 128, random_state = 0) # Based on research, ideal number of estimators is between 64-128, to change n_estimators for model hyper tuning
    
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
    
    # Summary Analysis of Feature Importance
    # Get numerical feature importances
    importances = list(rf.feature_importances_)
    # List of tuples with variable and importance
    feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]
    # Sort the feature importances by most important first
    feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)
    # Print out the feature and importances 
    [print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances];
    
    # Determine Most Important Category
    w = sum(importances[2:7])/sum(importances[2:])
    o = sum(importances[7:11])/sum(importances[2:])
    p = sum(importances[11:18])/sum(importances[2:])
    c = sum(importances[18:])/sum(importances[2:])
    print("Wellbeing Weightage:", w)
    print("Opinion Weightage:", o)
    print("Personality Weightage:", p)
    print("Core Values Weightage:", c)
    
    return rf, report