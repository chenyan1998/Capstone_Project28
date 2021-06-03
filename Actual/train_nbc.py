""" Script for Model Training - Naive Bayes Classifier """

# Libraries Imported
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB

def train(features, feature_list, labels, df):

    # Split into Train-Test Set
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.3, random_state=0)
    
    # Run Naive Bayes Classifier
    nbc = GaussianNB()
    
    # Fit Naive Bayes Classifier with Training Data
    nbc.fit(train_features, train_labels)
    
    # Prediction & Model Performance Metrics for Model Validation
    predictions = nbc.predict(test_features)
    conf_mat = confusion_matrix(test_labels, predictions)
    print(conf_mat)
    acc = metrics.accuracy_score(test_labels, predictions)
    fpr = conf_mat[1][0]/(conf_mat[1][0] + conf_mat[0][0]) # False Positive Rate
    tnr = conf_mat[0][0]/(conf_mat[1][0] + conf_mat[0][0]) # True Negative Rate
    tpr = conf_mat[1][1]/(conf_mat[1][1] + conf_mat[0][1]) # True Positive Rate
    fnr = conf_mat[0][1]/(conf_mat[1][1] + conf_mat[0][1]) # False Negative Rate
    print("Naive Bayes Performance")
    print("Accuracy:", acc)
    print("False Positive Rate:", fpr)
    print("True Negative Rate:", tnr)
    print("True Positive Rate:", tpr)
    print("False Negative Rate:", fnr)
    
    # Note: No Feature Importance Method for KNN Classifier
    return nbc