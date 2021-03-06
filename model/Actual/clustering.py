""" Script for Clustering """

# Standard Libraries Imported
import numpy as np
from sklearn.cluster import KMeans

def cluster(dataframe, predictors):

    # K Means Clustering
    # 0 -> High Flight Risk, 1-> Low Flight Risk
    model = KMeans(n_clusters=2, random_state=0) # To determine the number of clusters & random state is like a set.seed which ensures reproducibility in the results
    kmeans = model.fit(predictors)
    dataframe["Flight Risk"] = kmeans.labels_
    dataframe['Flight Risk'] = np.where(dataframe['Flight Risk'] == 1, "High Flight Risk", "Low Flight Risk")
    
    # Drop Employee ID, Job Level & Department, Dependent Variable - Flight Risk from Features
    # (Note: Output Results will be segmented by Individuals, Job Level & Department)
    labels = np.array(dataframe['Flight Risk'])
    # Note: i_3 and o_3 are dropped as it results in an improvement in the prediction model
    #  (o_2 is strongly correlated with o_3 and i_2 is strongly correlated with i_3)
    features = np.array(dataframe.drop(['Year', 'i_0', 'i_3', 'o_3', 'i_4', 'i_5', 'Flight Risk'], axis=1))
    feature_list = list(dataframe.drop(['Year', 'i_0', 'i_3', 'o_3', 'i_4', 'i_5', 'Flight Risk'], axis=1))
    
    return labels, features, feature_list, dataframe