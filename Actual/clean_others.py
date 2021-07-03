""" Script for Cleaning Other Questions """

# Standard Libraries Imported
import pandas as pd

names = ["Year", "i_0", "i_1", "i_2", "i_3", "i_4", "i_5", "w_1", "w_2", "w_3", "w_4", "w_5", "o_1", "o_2", "o_3", "o_4", "o_5", "p_1n", "p_2n", "p_3n", "p_4n", "p_5a", "p_6a", "p_7a", "c_1", "c_2", "c_3", "c_4", "c_5", "c_6"]

# Encoding of Categorical Data to Ranked Numerical Order & Data Cleaning
# For i_2 and i_3, both "Below 2 years" and "Below 3 years" are considered the same category and this change was made as the survey option was corrected after the survey was launched
encode = { "i_1": {"20-29": 1, "30-39": 2, "40-49": 3, "50-59": 4, "60 and above": 5 },
            "i_2": {"Below 2 years": 1, "Below 3 years": 1, "3-5 years": 2, "6-10 years": 3, "11-19 years": 4, "20 years and above": 5},
            "i_3": {"Below 2 years": 1, "Below 3 years": 1, "3-5 years": 2, "6-10 years": 3, "11-19 years": 4, "20 years and above": 5},
            "i_4": {"CISCO SLC LVL 6": "Contract Logistics/SCM  合同物流/供应链管理", "cariuma": "Contract Logistics/SCM  合同物流/供应链管理"},
            "i_5": {"storekeeper": "Non-Executives",
                    "storkeeper": "Non-Executives",
                    "store keeper": "Non-Executives",
                    "Storekeeper": "Non-Executives",
                    "storekepper": "Non-Executives",
                    "STORE KEEPER": "Non-Executives",
                    "STORE KEEPER ": "Non-Executives",
                    "Store Assistance": "Non-Executives",
                    "Senior storekeeper": "Non-Executives",
                    "Senior store keeper ": "Non-Executives",
                    "Senior store keeper": "Non-Executives",
                    "Senior Storekeeper": "Non-Executives",
                    "snr storekeeper": "Non-Executives",
                    "S.STOREKEEPER": "Non-Executives", 
                    "Logistic Assistant": "Non-Executives", 
                    "LOGISTICS ASSISTANT": "Non-Executives",
                    "Logistic officer": "Non-Executives",
                    "officer": "Non-Executives",
                    "Officer": "Non-Executives",
                    "OFFICER": "Non-Executives",
                    "logistics officer": "Non-Executives",
                    "Senior Logistic officer": "Non-Executives",
                    "Senior Logistics Officer": "Non-Executives",
                    "senior shipping officer": "Non-Executives",
                    "customer services ": "Non-Executives",
                    "EXPORT OFFICER": "Non-Executives",
                    "export officer": "Non-Executives",
                    "System Specialist": "Non-Executives",
                    "Assistant Supervisors": "Supervisors",
                    "Assistant Supervisors ": "Supervisors",
                    "Management Associate": "Executives", 
                    "Senior Executive": "Executives",
                    "Deputy G.M": "Manager",
                    "AGM": "Manager"},
}

# Reverse Scoring for Neuroticism as it is found to have a negative relation with Employee Engagement
mapping = {"1":5, "2": 4, "3": 3, "4": 2, "5": 1}

def clean(data):
    
    # Production Version
    # Extract Date
    date = data.iloc[0:, 2]
    date = pd.to_datetime(date).dt.year
    
    # Pull out relevant columns in the excel
    df = data.iloc[0:, 6:35]
    
    # Insert Year of Survey
    df.insert(0, "Year", date)
    
    # Local Version
    # Extract Date
    # date = data.iloc[1:,1]
    # date = pd.to_datetime(date).dt.year

    # Pull out relevant columns in the excel
    # df = data.iloc[1:,6:35]
    
    # Insert Year of Survey
    # df.insert(0, 'Year', date)
  
    # Rename Dataframe Columns
    # i -> Individual
    # w-> Wellbeing
    # o -> Opinions & Emotions
    # p_xn -> Neuroticism
    # p_xa -> Agreeableness
    # c -> Core Values
    df.columns = names
    
    # Encode Responses for Categorical Data and Cleaning         
    df = df.replace(encode)
    
    # Reverse Scoring for Neuroticism as it is found to have a negative relation with Employee Engagement
    df["p_1n"] = df["p_1n"].map(mapping)
    df["p_2n"] = df["p_2n"].map(mapping)
    df["p_3n"] = df["p_3n"].map(mapping)
    df["p_4n"] = df["p_4n"].map(mapping)
    
    # Cleaning for w_1, w_2, w_3 due to data conversion error from MongoDB
    df['w_1'] = df['w_1'].apply(lambda x: x.get("", {}).get("",{}).get("",{}))
    df['w_2'] = df['w_2'].apply(lambda x: x.get("", {}).get("",{}).get("",{}))
    df['w_3'] = df['w_3'].apply(lambda x: x.get("", {}).get("",{}).get("",{}))
    
    # Extract Features for Prediction & Clustering
    features = df.drop(["Year",'i_0', 'i_4', 'i_5'], axis=1)
    
    # Convert all relevant columns to numeric for clustering
    cols = ["i_1", "i_2", "i_3", "w_1", "w_2", "w_3", "w_4", "w_5", "o_1", "o_2", "o_3", "o_4", "o_5", "p_1n", "p_2n", "p_3n", "p_4n", "p_5a", "p_6a", "p_7a", "c_1", "c_2", "c_3", "c_4", "c_5", "c_6"]
    features[cols] = features[cols].apply(pd.to_numeric, errors='coerce', axis=1)
    df[cols] = df[cols].apply(pd.to_numeric, errors='coerce', axis=1)
    
    return df, features