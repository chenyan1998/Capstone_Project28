""" Script for Report Generation """

# Standard Libraries Imported
import pandas as pd

metric_list = ['w_1_mean', 'w_2_mean', 'w_3_mean', 'w_4_mean', 'w_5_mean', 
             'o_1_mean', 'o_2_mean', 'o_3_mean', 'o_4_mean', 'o_5_mean', 
             'p_1n_mean', 'p_2n_mean', 'p_3n_mean', 'p_4n_mean', 
             'p_5a_mean', 'p_6a_mean', 'p_7a_mean', 
             'c_1_mean', 'c_2_mean', 'c_3_mean', 'c_4_mean', 'c_5_mean', 'c_6_mean', 
             'w_total_mean','o_total_mean', 'p_total_mean', 'c_total_mean', 'EES_mean'
             ]

age_cat = ["20-29", "30-39", "40-49", "50-59", "60 and above"]

dept_lst = ["Fairs, Exhibitions, Events  展会、展览、活动", 
            "Air Freight Division  航空货运部门", 
            "Centre of Performance Excellence  卓越表现中心",
            "Contract Logistics/SCM  合同物流/供应链管理",
            "Finance  金融",
            "Global Projects & Industry Soln  全球项目和行业解决方案",
            "HSSE 健康安全与环境",
            "Human Resource  人力资源部",
            "IT  信息技术",
            "Ocean Freight Division  海运部门",
            "Sales and Sales Planning  销售及销售计划"
            ]

def gen_report(individual, segment_age, segment_job_level, segment_department):
    
    # Report Type 3 - Comparison Report between age, job level, department
    report_type_3_age = {}
    report_type_3_job_level = {}
    report_type_3_department = {}
    
    for i in metric_list:
        temp_1 = segment_age[i]
        temp_1 = pd.DataFrame(temp_1)
        temp_1 = temp_1.T
        temp_1.columns = age_cat
        temp_1["Year"] = segment_age.iloc[0,140]
        temp_2 = segment_job_level[i]
        temp_2 = pd.DataFrame(temp_2)
        temp_2 = temp_2.T
        temp_2["Year"] = segment_job_level.iloc[0,140]
        temp_3 = segment_department[i]
        temp_3 = pd.DataFrame(temp_3)
        temp_3 = temp_3.T
        temp_3["Year"] = segment_department.iloc[0,140]
        
        report_type_3_age.update({i: temp_1})
        report_type_3_job_level.update({i: temp_2})
        report_type_3_department.update({i: temp_3})
    
    # Report Type 4 - Department Level Survey Report by Questions
    # Report Type 5 - Department Level Summary Report by Questions
    report_type_4_wellbeing = {}
    report_type_4_opinions = {}
    report_type_4_personality = {}
    report_type_4_core_values = {}
    report_type_5 = {}
    temp = segment_department[metric_list]
    
    for i in range(0, len(segment_department.index)):
        w_temp = temp.iloc[i,0:5]
        w_temp = pd.DataFrame(w_temp)
        w_temp = w_temp.T
        w_temp["Year"] = segment_department.iloc[0,140]
        o_temp = temp.iloc[i,5:10]
        o_temp = pd.DataFrame(o_temp)
        o_temp = o_temp.T
        o_temp["Year"] = segment_department.iloc[0,140]
        p_temp = temp.iloc[i,10:17]
        p_temp = pd.DataFrame(p_temp)
        p_temp = p_temp.T
        p_temp["Year"] = segment_department.iloc[0,140]
        c_temp = temp.iloc[i,17:23]
        c_temp = pd.DataFrame(c_temp)
        c_temp = c_temp.T
        c_temp["Year"] = segment_department.iloc[0,140]
        temp_1 = temp.iloc[i,23:]
        temp_1 = pd.DataFrame(temp_1)
        temp_1 = temp_1.T
        temp_1["Year"] = segment_department.iloc[0,140]
        key = temp.index[i]
        report_type_4_wellbeing.update({key: w_temp})
        report_type_4_opinions.update({key: o_temp})
        report_type_4_personality.update({key: p_temp})
        report_type_4_core_values.update({key: c_temp})
        report_type_5.update({key: temp_1})
    
    return report_type_3_age, report_type_3_job_level, report_type_3_department, report_type_4_wellbeing, report_type_4_opinions, report_type_4_personality, report_type_4_core_values, report_type_5 