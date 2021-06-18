""" Script for Model Training - Decision Tree """

# Standard Libraries Imported
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

def train(features, feature_list, labels, df):

    # Split into Train-Test Set
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.3, random_state=0)

    # Run Decision Tree
    dt = DecisionTreeClassifier(max_depth = None, random_state = 0) # To change max_depth for hyper tuning
    
    # Fit Decision Tree with Training Data
    dt.fit(train_features, train_labels)
    
    # Visualise Decision Tree
    tree.plot_tree(dt)
    
    # Prediction & Model Performance Metrics for Model Validation
    predictions = dt.predict(test_features)
    conf_mat = confusion_matrix(test_labels, predictions)
    print(conf_mat)
    
    # Accuracy is the number of correct predictions
    # Precision = True_Positive/ (True_Positive+ False_Positive) -> Measures % Correctly Predicted Class
    # Recall = True_Positive/ (True_Positive+ False_Negative) -> Measures the fraction of samples from a class which are correctly predicted by the model
    # F1 Score is the harmonic mean of Precision and recall for each category
    # Support is the number of occurences for each class
    print("Decision Tree Performance")
    report = classification_report(test_labels, predictions, output_dict=True)
    print(classification_report(test_labels, predictions))
    report = pd.DataFrame(report).transpose()
    
    # Summary Analysis of Feature Importance
    # Get numerical feature importances
    importances = list(dt.feature_importances_)
    # List of tuples with variable and importance
    feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]
    # Sort the feature importances by most important first
    feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)
    # Print out the feature and importances 
    # [print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances];
    
    # Determine Most Important Category
    w = sum(importances[2:7])/sum(importances[2:])
    o = sum(importances[7:11])/sum(importances[2:])
    p = sum(importances[11:18])/sum(importances[2:])
    c = sum(importances[18:])/sum(importances[2:])
    print("Wellbeing Weightage:", w)
    print("Opinion Weightage:", o)
    print("Personality Weightage:", p)
    print("Core Values Weightage:", c)

    return dt, report