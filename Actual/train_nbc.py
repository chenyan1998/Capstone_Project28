""" Script for Model Training - Naive Bayes Classifier """

# Standard Libraries Imported
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
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
    
    # Accuracy is the number of correct predictions
    # Precision = True_Positive/ (True_Positive+ False_Positive) -> Measures % Correctly Predicted Class
    # Recall = True_Positive/ (True_Positive+ False_Negative) -> Measures the fraction of samples from a class which are correctly predicted by the model
    # F1 Score is the harmonic mean of Precision and recall for each category
    # Support is the number of occurences for each class
    print("NBC Performance")
    print(classification_report(test_labels, predictions))
    
    # Note: No Feature Importance Method for KNN Classifier
    return nbc