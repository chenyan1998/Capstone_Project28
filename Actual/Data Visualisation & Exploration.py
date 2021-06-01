""" Script for Data Visualisation & Exploration """

# Libraries Imported
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import os

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'Employee Engagement Survey(1-76).xlsx')

# Import Survey Results 
# To change to pull request function
survey = pd.read_excel(filename, header = None)

""" Start of Module 0 - Data Cleaning for Last Question (Works) """
# Data Cleaning of Last Question with Multiple Answers
test = survey

# Split Response into Multiple Columns
temp = test.iloc[1:,35].str.split(";", n = None, expand = True)

# Obtain Frequency Count by Response Type
temp_1 = pd.DataFrame(temp.iloc[1:,0].value_counts())
temp_2 = pd.DataFrame(temp.iloc[1:,1].value_counts())
temp_3 = pd.DataFrame(temp.iloc[1:,2].value_counts())
temp_4 = pd.DataFrame(temp.iloc[1:,3].value_counts())
temp_5 = pd.DataFrame(temp.iloc[1:,4].value_counts())
temp_6 = pd.DataFrame(temp.iloc[1:,5].value_counts())
temp_7 = pd.DataFrame(temp.iloc[1:,6].value_counts())
temp_8 = pd.DataFrame(temp.iloc[1:,7].value_counts())
# temp_9 = pd.DataFrame(temp.iloc[1:,8].value_counts())
# temp_10 = pd.DataFrame(temp.iloc[1:,9].value_counts())

# List of all DataFrames to be merged
temp_all = [temp_2, temp_3, temp_4, temp_5, temp_6, temp_7, temp_8]

# Merge all DataFrames
for i in temp_all:
    temp_1 = temp_1.merge(i,left_index = True, right_index = True, how = "outer")
    
# Drop Index of Invalid Response
valid_response = ["Improved supervisory relations 监督关系之间的改善", 
                  "Changes in supplies, tools, equipment 用品、工具、设备的变化", 
                  "More freedom 更自由",
                  "More authority 更大的权力、权限",
                  "More and better information 更多更好的信息",
                  "Changes in work environment 工作环境的变化",
                  "Clearer responsibilities 更清晰的职责",
                  "Additional manpower 额外人力",
                  "More cooperation from other areas or departments 更多跨领域或部门的合作",
                  "Better planning 更好的规划"
]

temp_1 = temp_1.loc[valid_response]
temp_1["Frequency"] = temp_1.sum(axis = 1)

# Output Frequency Count of Productivity Driver
drivers = temp_1["Frequency"]

""" End of Module 0 - Data Cleaning for Last Question (Works) """

""" Start of Module 1 - Import, Clean Data & Data Manipulation (Works) """
# Pull out relevant columns in the excel
df = survey.iloc[1:,6:35]

# Rename Dataframe Columns
# i -> Individual
# w-> Wellbeing
# o -> Opinions & Emotions
# p_xn -> Neuroticism
# p_xa -> Agreeableness
# c -> Core Values
names = ["i_0", "i_1", "i_2", "i_3", "i_4", "i_5", "w_1", "w_2", "w_3", "w_4", "w_5", "o_1", "o_2", "o_3", "o_4", "o_5", "p_1n", "p_2n", "p_3n", "p_4n", "p_5a", "p_6a", "p_7a", "c_1", "c_2", "c_3", "c_4", "c_5", "c_6"]
df.columns = names

# Encoding of Categorical Data to Ranked Numerical Order & Data Cleaning
# For i_2 and i_3, both "Below 2 years" and "Below 3 years" are considered the same category and this change was made as the survey option was corrected after the survey was launched
encode = { "i_1": {"20-29": 1, "30-39": 2, "40-49": 3, "50-59": 4, "60 and above": 5 },
            "i_2": {"Below 2 years": 1, "Below 3 years": 1, "3-5 years": 2, "6-10 years": 3, "11-19 years": 4, "20 years and above": 5},
            "i_3": {"Below 2 years": 1, "Below 3 years": 1, "3-5 years": 2, "6-10 years": 3, "11-19 years": 4, "20 years and above": 5},
            "i_4": {"CISCO SLC LVL 6": "Others", "cariuma": "Others"},
            "i_5": {"storekeeper": "Non-Executives",
                    "storkeeper": "Non-Executives",
                    "store keeper": "Non-Executives",
                    "Storekeeper": "Non-Executives",
                    "Senior storekeeper": "Non-Executives",
                    "Senior store keeper": "Non-Executives",
                    "snr storekeeper": "Non-Executives",
                    "S.STOREKEEPER": "Non-Executives", 
                    "Logistic Assistant": "Non-Executives", 
                    "officer": "Non-Executives",
                    "logistics officer": "Non-Executives",
                    "Senior Logistic officer": "Non-Executives",
                    "senior shipping officer": "Non-Executives",
                    "Management Associate": "Executives", 
                    "Senior Executive": "Executives"
                    }
}
            
df = df.replace(encode)

# Reverse Scoring for Neuroticism as it is found to have a negative relation with Employee Engagement
mapping = {1:5, 2: 4, 3: 3, 4: 2, 5: 1}
df["p_1n"] = df["p_1n"].map(mapping)
df["p_2n"] = df["p_2n"].map(mapping)
df["p_3n"] = df["p_3n"].map(mapping)
df["p_4n"] = df["p_4n"].map(mapping)

# Extract Features for Prediction & Clustering
features = df.drop(['i_0', 'i_4', 'i_5'], axis=1)

# Convert all relevant columns to numeric for clustering
cols = ["i_1", "i_2", "i_3", "w_1", "w_2", "w_3", "w_4", "w_5", "o_1", "o_2", "o_3", "o_4", "o_5", "p_1n", "p_2n", "p_3n", "p_4n", "p_5a", "p_6a", "p_7a", "c_1", "c_2", "c_3", "c_4", "c_5", "c_6"]
features[cols] = features[cols].apply(pd.to_numeric, errors='coerce', axis=1)
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce', axis=1)

""" End of Module 1 - Data Cleaning & Manipulation for Model (Works) """

""" Start of Module 2 - Data Exploration & Visualisation (Works) """
# Univariate Analysis to understand Distribution of Data
features.hist(color='steelblue', edgecolor='black', linewidth=1.0,
           xlabelsize=8, ylabelsize=8, grid=False)    
plt.tight_layout(rect=(0, 0, 1.2, 1.2)) 

# Correlation Analysis
# Plot Heatmap of all correlation values
corr = features.corr()
f1, ax1 = plt.subplots(figsize=(10, 6))
mask = np.triu(np.ones_like(corr, dtype=bool))
hm_1 = sns.heatmap(round(corr,2), mask = mask, annot=True, ax=ax1, cmap="coolwarm",fmt='.2f',
                 linewidths=.5)
f1.subplots_adjust(top=0.93)
t1= f1.suptitle('Correlation Heatmap', fontsize=14)

# Plot Heatmap of high correlation values
high_corr = corr[corr >= 0.7]
f2, ax2 = plt.subplots(figsize=(10, 6))
mask = np.triu(np.ones_like(high_corr, dtype=bool))
hm_2 = sns.heatmap(round(high_corr,2), mask = mask, annot=True, ax=ax2, cmap="autumn_r",fmt='.2f',
                 linewidths=.5)
f2.subplots_adjust(top=0.93)
t2= f2.suptitle('Correlation Heatmap', fontsize=14)
""" End of Module 2 - Data Exploration & Visualisation (Works) """