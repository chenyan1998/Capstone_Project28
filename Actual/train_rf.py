""" Script for Model Training - Random Forest """

# Standard Libraries Imported
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

def train(features, feature_list, labels, df):

    # Split into Train-Test Set
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.3, random_state=0)
    
    # Run Random Forest
    rf = RandomForestClassifier(n_estimators = 128, random_state = 0) # Based on research, ideal number of estimators is between 64-128, to change n_estimators for model hyper tuning
    
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
    print(classification_report(test_labels, predictions))
    
    # Summary Analysis of Feature Importance
    # Get numerical feature importances
    importances = list(rf.feature_importances_)
    # List of tuples with variable and importance
    feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]
    # Sort the feature importances by most important first
    feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)
    # Print out the feature and importances 
    # [print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances];
    
    # Determine Most Important Category
    w = sum(importances[3:8])
    o = sum(importances[8:13])
    p = sum(importances[13:20])
    c = sum(importances[20:])
    # print("Wellbeing Weightage:", w)
    # print("Opinion Weightage:", o)
    # print("Personality Weightage:", p)
    # print("Core Values Weightage:", c)
    
    # Individual Analysis Score by Survey Question Buckets Normalised to a Max Score of 100
    # extract out the value of the importances and assign them 
    df["w_total"] = (df["w_1"]*importances[3] + df["w_2"]*importances[4] + df["w_3"]*importances[5] + df["w_4"]*importances[6] + df["w_5"]*importances[7])*100/(5*sum(importances[3:8]))
    df["o_total"] = (df["o_1"]*importances[8] + df["o_2"]*importances[9] + df["o_3"]*importances[10] + df["o_4"]*importances[11] + df["o_5"]*importances[12])*100/(5*sum(importances[8:13]))
    df["p_total"] = (df["p_1n"]*importances[13] + df["p_2n"]*importances[14] + df["p_3n"]*importances[15] + df["p_4n"]*importances[16] + df["p_5a"]*importances[17] + df["p_6a"]*importances[18] + df["p_7a"]*importances[19])*100/(5*sum(importances[13:20]))
    df["c_total"] = (df["c_1"]*importances[20] + df["c_2"]*importances[21] + df["c_3"]*importances[22] + df["c_4"]*importances[23] + df["c_5"]*importances[24] + df["c_6"]*importances[25])*100/(5*sum(importances[20:]))
    df["EES"] = (df["w_1"]*importances[3] + df["w_2"]*importances[4] + df["w_3"]*importances[5] + df["w_4"]*importances[6] + df["w_5"]*importances[7] + df["o_1"]*importances[8] + df["o_2"]*importances[9] + df["o_3"]*importances[10] + df["o_4"]*importances[11] + df["o_5"]*importances[12] + df["p_1n"]*importances[13] + df["p_2n"]*importances[14] + df["p_3n"]*importances[15] + df["p_4n"]*importances[16] + df["p_5a"]*importances[17] + df["p_6a"]*importances[18] + df["p_7a"]*importances[19] + df["c_1"]*importances[20] + df["c_2"]*importances[21] + df["c_3"]*importances[22] + df["c_4"]*importances[23] + df["c_5"]*importances[24] + df["c_6"]*importances[25])*100/(5*sum(importances[3:]))
    
    return rf, df