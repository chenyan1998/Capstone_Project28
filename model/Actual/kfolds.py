""" Script for K-Fold Cross Validation """

# Standard Libraries Imported
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
import numpy as np

def cv(features, labels):
    
    # Run Repeated KFolds
    kfolds = RepeatedKFold(n_splits = 10, n_repeats = 50, random_state = 0)
    
    rf = RandomForestClassifier(n_estimators = 128)
    dt = DecisionTreeClassifier(max_depth = None)
    knn = KNeighborsClassifier(n_neighbors = 5)
    sv = svm.SVC(kernel='linear')
    nbc = GaussianNB()
    
    supervised_learning = [rf, dt, knn, sv, nbc]
    
    output = []
    
    for i in supervised_learning:
    
        score = cross_val_score(i, features, labels, cv = kfolds)
    
    # Return Range of Accuracy at 95% Confidence
        alpha = 0.95                         
        p = ((1.0-alpha)/2.0) * 100             
        lower = max(0.0, np.percentile(score, p))  
        p = (alpha+((1.0-alpha)/2.0)) * 100
        upper = min(1.0, np.percentile(score, p))
        confint = (lower*100, upper*100)
        output.append(confint)
        
    return output