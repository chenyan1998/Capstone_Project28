""" Script for Retrieving Individual Employee Data for Plotting """

def get_individual(employee_id, new_results_individual):
    
    # Report Type 1 - Generate All Survey Responses for Each Employee i.e. One Report for Each Employee
    # Report Type 2 - Generate Summary Survey Responses for Each Employee i.e. One Report for Each Employee    
    report_type_1 = {}
    report_type_2 = {}
    temp_1 = new_results_individual[new_results_individual["i_0"] == employee_id].iloc[0,7:30]
    temp_2 = new_results_individual[new_results_individual["i_0"] == employee_id].iloc[0,30:]
    report_type_1.update({employee_id: temp_1})
    report_type_2.update({employee_id: temp_2})
    
    return report_type_1, report_type_2