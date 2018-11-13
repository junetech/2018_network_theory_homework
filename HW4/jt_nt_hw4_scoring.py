import json
import csv
import time
import networkx as nx
from munkres import Munkres, print_matrix

def return_list_of_filename(filename, mid_string):
    file_list = []
    with open(filename) as json_file:
        filename_data = json.load(json_file)
    for key, value in filename_data.items():
        filestring = key + mid_string + value
        file_list.append(filestring)
    return file_list

def my_read_function(filename):
    '''    
    Returns the matrix as list after reading csv file
    written by HW3_20172939_Bang
    '''
    ## Opening file csv at current folder as read mode
    f = open(filename,'r')   
    csvReader = csv.reader(f)
    matrix = []
    for i in csvReader:
        a_list = []
        for j in i:
            a_list.append(float(j))
        matrix.append(a_list)
    f.close()
    return matrix

def solve2(filename):
    '''    
    Returns the solution of Munkres python library
    written by HW3_20172939_Bang
    '''
    matrix = my_read_function(filename)
    m = Munkres()
    indexes = m.compute(matrix)
    return indexes  

def main():
    input_filename = "network_theory_hw3_assignment_costs_48_48.csv"
    result_filename = "result_slow_"+input_filename

    matrix = my_read_function(input_filename)
    true_answer = solve2(input_filename)
    true_cost = 0
    for (i, j) in true_answer:
        true_cost += matrix[i][j]
    print("Minimum cost by munkres:", true_cost)
    # import pprint
    # pprint.pprint(true_answer)
    info_json_filename = "filenames_2018_nf.json"
    file_list = return_list_of_filename(info_json_filename, "_HW3_")

    with open(result_filename, 'w') as csvfile:
        headers = ["module name", "success_fail", "time_spent", "time_score"]
        writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
        writer.writerow(headers)

    for module in map(__import__, file_list):
        module_name = str(module)[18:36]
        print(module_name)
        start_time = time.time()
        result = module.solve(input_filename)
        end_time = time.time()
        time_spent = end_time-start_time
        print("The module took", time_spent, "seconds")
        status = True
        calc_cost = 0
        for (i, j) in result:
            calc_cost += matrix[i][j]
        if true_cost != calc_cost:
            status = False
        result_list = [module_name, status, time_spent]
        with open(result_filename, 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
            writer.writerow(result_list)

if __name__ == '__main__':
    main()
