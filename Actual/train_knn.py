""" Script for Model Training - KNN """

# Libraries Imported
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

def train(features, feature_list, labels, df):
    
    # Split into Train-Test Set
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.3, random_state=0)

    # Run K Nearest Neighbours
    knn = KNeighborsClassifier(n_neighbors = 5) # To change number of neighbours for hypertuning of model, default is 5
    
    # Fit K Nearest Neighbours with Training Data
    knn.fit(train_features, train_labels)
    
    # Prediction & Model Performance Metrics for Model Validation
    predictions = knn.predict(test_features)
    conf_mat = confusion_matrix(test_labels, predictions)
    print(conf_mat)
    acc = metrics.accuracy_score(test_labels, predictions)
    fpr = conf_mat[1][0]/(conf_mat[1][0] + conf_mat[0][0]) # False Positive Rate
    tnr = conf_mat[0][0]/(conf_mat[1][0] + conf_mat[0][0]) # True Negative Rate
    tpr = conf_mat[1][1]/(conf_mat[1][1] + conf_mat[0][1]) # True Positive Rate
    fnr = conf_mat[0][1]/(conf_mat[1][1] + conf_mat[0][1]) # False Negative Rate
    print("KNN Performance")
    print("Accuracy:", acc)
    print("False Positive Rate:", fpr)
    print("True Negative Rate:", tnr)
    print("True Positive Rate:", tpr)
    print("False Negative Rate:", fnr)
    
    # Note: No Feature Importance Method for KNN Classifier
    
    return knn