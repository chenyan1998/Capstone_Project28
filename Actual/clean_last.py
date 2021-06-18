""" Script for Cleaning Last Question """

# Standard Libraries Imported
import pandas as pd

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

def clean_last_qns(data):
    
    # Data Cleaning of Last Question with Multiple Answers
    test = data
    
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
    
    temp_1 = temp_1.loc[valid_response]
    temp_1["Frequency"] = temp_1.sum(axis = 1)
    
    # Output Frequency Count of Productivity Driver
    drivers = temp_1["Frequency"]
    
    return drivers