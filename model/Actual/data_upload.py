""" Script for Results Upload to Database """

# Standard Libraries Imported
import pandas as pd
import pymongo

mongo_client = pymongo.MongoClient('mongodb+srv://Chenyan:Sutd30121998@cluster0.uxbcx.mongodb.net/test?authSource=admin&replicaSet=atlas-vtcq3b-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')

def upload(report_type_4_wellbeing, report_type_4_opinions, report_type_4_personality, report_type_4_core_values, new_results_individual, new_results_department, new_results_job_level, new_results_age):
    
    # Establish Connection to Database
    db = mongo_client['report']
    collection = db["report"]
    # Update Survey Categorical Results
    
    # Wellbeing Report
    for i , j in report_type_4_wellbeing.items():
        year = str(j.iloc[0,5])
        j = j.drop(["Year"], axis = 1)
        x = list(j)
        y = j.iloc[0].tolist()
        temp = {'name': "Report 4", 
                "metric": "wellbeing", 
                "department": i, 
                "year": year,
                "report_format": "chart",
                "question": "wellbeing",
                "label_x": "Question",
                "label_y": "Mean Score",
                "data_x": x, 
                "data_y": y}
        collection.replace_one({"department": i, 'year': year, "metric": "wellbeing"}, temp, upsert = True)
    
    # Opinions Report
    for i , j in report_type_4_opinions.items():
        year = str(j.iloc[0,5])
        j = j.drop(["Year"], axis = 1)
        x = list(j)
        y = j.iloc[0].tolist()
        temp = {'name': "Report 4", 
                "metric": "opinion", 
                "department": i, 
                "year": year,
                "report_format": "chart",
                "question": "opinion",
                "label_x": "Question",
                "label_y": "Mean Score",
                "data_x": x, 
                "data_y": y}
        collection.replace_one({"department": i, 'year': year, "metric": "opinion"}, temp, upsert = True)
    
    # Personality Report
    for i , j in report_type_4_personality.items():
        year = str(j.iloc[0,7])
        j = j.drop(["Year"], axis = 1)
        x = list(j)
        y = j.iloc[0].tolist()
        temp = {'name': "Report 4", 
                "metric": "personality", 
                "department": i, 
                "year": year,
                "report_format": "chart",
                "question": "personality",
                "label_x": "Question",
                "label_y": "Mean Score",
                "data_x": x, 
                "data_y": y}
        collection.replace_one({"department": i, 'year': year, "metric": "personality"}, temp, upsert = True)
     
    # Core Values Report
    for i , j in report_type_4_core_values.items():
        year = str(j.iloc[0,6])
        j = j.drop(["Year"], axis = 1)
        x = list(j)
        y = j.iloc[0].tolist()
        temp = {'name': "Report 4", 
                "metric": "coreValues", 
                "department": i, 
                "year": year,
                "report_format": "chart",
                "question": "coreValues",
                "label_x": "Question",
                "label_y": "Mean Score",
                "data_x": x, 
                "data_y": y}
        collection.replace_one({"department": i, 'year': year, "metric": "coreValues"}, temp, upsert = True)
    
    # Update Individual Results - Report Type 2
    collection = db["RF_Summary_Report"]
    for i in range(0, len(new_results_individual)):
        temp = {'Employee_id':new_results_individual.iloc[i,1], 
                "EES_score": new_results_individual.iloc[i,34], 
                "Opinion": new_results_individual.iloc[i,31],  
                "Wellbeing": new_results_individual.iloc[i,30], 
                "Core_values": new_results_individual.iloc[i,33], 
                "Personality": new_results_individual.iloc[i,32], 
                "Flight_risk_label": new_results_individual.iloc[i,35],
                "year": str(new_results_individual.iloc[i,0])}
        collection.replace_one({"Employee_id": new_results_individual.iloc[i,1], 'year': str(new_results_individual.iloc[i,0])}, temp, upsert = True)
    
    # Update Wellbeing Best/Worst Performer - Report Type 5
    collection = db["RF_Best_Worse_Report"]
    compare_lst = ["w_total_mean", "o_total_mean", "p_total_mean", "c_total_mean"]
    for i in compare_lst:
        year = str(new_results_department.iloc[0,140])
        min_score = min(new_results_department[i])
        worse_department = new_results_department[new_results_department[i] == min_score].index[0] 
        max_score = max(new_results_department[i])
        best_department = new_results_department[new_results_department[i] == max_score].index[0]    
        temp = {'name': "Report 5", 
                "metric": i, 
                "department": "NA", 
                "year": year,
                "report_format": "pie_chart",
                "question": "NA",
                "label_x": best_department,
                "label_y": worse_department,
                "data_x": max_score, 
                "data_y": min_score}
        collection.replace_one({"metric":i, "report_format": "pie_chart", 'year': year}, temp, upsert = True)
    
    # Update Raw Results Table - Report Type 1,3
    # collection
    collection= db["Table_Individual"]
    data_dict = new_results_individual.to_dict("records")
    # Insert collection
    for i in data_dict:
        collection.replace_one({"i_0": i["i_0"], "Year": i["Year"]}, i, upsert = True)
    
    # collection
    collection= db["Table_Department"]
    data_dict = new_results_department.to_dict("records")
    # Insert collection
    for i in data_dict:
        collection.replace_one({"Department": i["Department"], "Year": i["Year"]}, i, upsert = True)

    # collection
    collection= db["Table_Job"]
    data_dict = new_results_job_level.to_dict("records")
    # Insert collection
    for i in data_dict:
        collection.replace_one({"Job Level": i["Job Level"], "Year": i["Year"]}, i, upsert = True)
      
    # collection
    collection= db["Table_Age"]
    data_dict = new_results_age.to_dict("records")
    # Insert collection
    for i in data_dict:
        collection.replace_one({"Age Category": i["Age Category"], "Year": i["Year"]}, i, upsert = True)

    return True