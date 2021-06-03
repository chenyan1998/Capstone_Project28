""" Script for Model Training - SVM """

# Libraries Imported
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn import svm

def train(features, feature_list, labels, df):
    
    # Split into Train-Test Set
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.3, random_state=0)
    
    # Run Support Vector Machine
    sv = svm.SVC(kernel='linear', random_state = 0)
    
    # Fit SVM with Training Data
    sv.fit(train_features, train_labels)
    
    # Prediction & Model Performance Metrics for Model Validation
    predictions = sv.predict(test_features)
    conf_mat = confusion_matrix(test_labels, predictions)
    print(conf_mat)
    acc = metrics.accuracy_score(test_labels, predictions)
    fpr = conf_mat[1][0]/(conf_mat[1][0] + conf_mat[0][0]) # False Positive Rate
    tnr = conf_mat[0][0]/(conf_mat[1][0] + conf_mat[0][0]) # True Negative Rate
    tpr = conf_mat[1][1]/(conf_mat[1][1] + conf_mat[0][1]) # True Positive Rate
    fnr = conf_mat[0][1]/(conf_mat[1][1] + conf_mat[0][1]) # False Negative Rate
    print("SVM Performance")
    print("Accuracy:", acc)
    print("False Positive Rate:", fpr)
    print("True Negative Rate:", tnr)
    print("True Positive Rate:", tpr)
    print("False Negative Rate:", fnr)
    
    # Summary Analysis of Feature Importance
    # Get numerical feature importances
    importances_sv_temp = []
    for i in sv.coef_:
        importances_sv_temp.append(i**2)
        
    # Normalise Importance Values to 1
    importances_sv = []
    for i in importances_sv_temp:
        importances_sv.append(i/sum(importances_sv_temp[0]))
    print(sum(importances_sv[0]))
    
    importances = importances_sv[0]
    
    # List of tuples with variable and importance
    feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]
    # Sort the feature importances by most important first
    feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)
    # Print out the feature and importances 
    [print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances];
    
    # Determine Most Important Category
    w = sum(importances[3:8])
    o = sum(importances[8:13])
    p = sum(importances[13:20])
    c = sum(importances[20:])
    print("Wellbeing Weightage:", w)
    print("Opinion Weightage:", o)
    print("Personality Weightage:", p)
    print("Core Values Weightage:", c)
    
    # Individual Analysis Score by Survey Question Buckets Normalised to a Max Score of 100
    # extract out the value of the importances and assign them 
    """ Uncomment the following if SVM is the final Model """
    # df["w_total"] = (df["w_1"]*importances[3] + df["w_2"]*importances[4] + df["w_3"]*importances[5] + df["w_4"]*importances[6] + df["w_5"]*importances[7])*100/(5*sum(importances[3:8]))
    # df["o_total"] = (df["o_1"]*importances[8] + df["o_2"]*importances[9] + df["o_3"]*importances[10] + df["o_4"]*importances[11] + df["o_5"]*importances[12])*100/(5*sum(importances[8:13]))
    # df["p_total"] = (df["p_1n"]*importances[13] + df["p_2n"]*importances[14] + df["p_3n"]*importances[15] + df["p_4n"]*importances[16] + df["p_5a"]*importances[17] + df["p_6a"]*importances[18] + df["p_7a"]*importances[19])*100/(5*sum(importances[13:20]))
    # df["c_total"] = (df["c_1"]*importances[20] + df["c_2"]*importances[21] + df["c_3"]*importances[22] + df["c_4"]*importances[23] + df["c_5"]*importances[24] + df["c_6"]*importances[25])*100/(5*sum(importances[20:]))
    # df["EES"] = (df["w_1"]*importances[3] + df["w_2"]*importances[4] + df["w_3"]*importances[5] + df["w_4"]*importances[6] + df["w_5"]*importances[7] + df["o_1"]*importances[8] + df["o_2"]*importances[9] + df["o_3"]*importances[10] + df["o_4"]*importances[11] + df["o_5"]*importances[12] + df["p_1n"]*importances[13] + df["p_2n"]*importances[14] + df["p_3n"]*importances[15] + df["p_4n"]*importances[16] + df["p_5a"]*importances[17] + df["p_6a"]*importances[18] + df["p_7a"]*importances[19] + df["c_1"]*importances[20] + df["c_2"]*importances[21] + df["c_3"]*importances[22] + df["c_4"]*importances[23] + df["c_5"]*importances[24] + df["c_6"]*importances[25])*100/(5*sum(importances[3:]))

    return sv # ,df