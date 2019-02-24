import numpy as np
import scipy.linalg as la
import json
import urllib.request as ur
from mat import mat as table
from queue import queue

class Nurse:
    def __init__(self, name, hours):
        employee_name = self.name
        workable_hours = self.hours
    def check_hours(self):
        return self.hours
    def work(self):
        return 

API_INTERFACE = 'https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins='
KEY = 'Aoo6MSOdOhu7_gENweR-26VzV-fP83hR3kCT3EouCWeQdF_uyhsT2kx5ZWqyffI2'
def largest_eigenvector(probability_matrix):
    #Start with random vector and get largest eigenvector out of probability
    vec = np.zeros(len(probability_matrix)) + 1
    for i in range(5):
        vec = probability_matrix@vec
        vec = vec/(la.norm(vec))
    return vec

#Returns tuple of adjacency matrix then probability matrix
def get_matrices(origins):
    #Run and parse API
    API_url = API_INTERFACE+origins+'&destinations='+origins+'&travelMode=driving&key='+KEY
    data_string = ur.urlopen(API_url).read()
    parsed_json = json.loads(data_string)
    #Process data
    n = len(origins.split(';'))
    #n = len(addresses)
    connections = parsed_json['resourceSets'][0]['resources'][0]['results']

    #Adjacency matrix with weights proportional to time
    adjacency_matrix = np.zeros((n,n))
    #Probability matrix with weights linking probability to less time
    probability_matrix = np.zeros((n,n))
    #Add weights as the travel duration symmetrically
    for connection in connections:
        dest = connection['destinationIndex']
        origin = connection['originIndex']
        dur = connection['travelDuration']
        adjacency_matrix[dest][origin] = dur
        adjacency_matrix[origin][dest] = dur
        if np.isclose(0,dur):
            continue
        probability_matrix[origin][dest] = 1./dur
        probability_matrix[dest][origin] = 1./dur
    #Put large numbers over diagonal to make it useless to stay in the same place
    for i in range(n):
        adjacency_matrix[i][i] = 9999999
    return (adjacency_matrix, probability_matrix)

#Maps high medium and low to 1 2 and 3 for sorting
def highmedlow(word):
    if 'HIGH' in word.upper():
        return 1
    if "MED" in word.upper():
        return 2
    if "LOW" in word.upper():
        return 3
    return 0

#Put task type information into usable table object
f = open('Data Files/CSV/EMPLOYEE_DATA.csv','r')
lines = f.read().split('\n')
f.close()
employee_table = table([line.split(',') for line in lines])

#Put task type information into usable table object
f = open('Data Files/CSV/NEW_PATIENT_DATA.csv','r')
lines = f.read().split('\n')
f.close()
patient_table = table([line.split(',') for line in lines])

#Put task type information into usable table object
f = open('Data Files/CSV/NEW_TASK_DATA.csv','r')
lines = f.read().split('\n')
f.close()
task_table = table([line.split(',') for line in lines])

#Put task type information into usable table object
f = open('Data Files/CSV/TASK_TYPE_DURATION.csv','r')
lines = f.read().split('\n')
f.close()
task_type = table([line.split(',') for line in lines])

#Sorting by due date over priority
indicies = np.argsort(list(map(highmedlow,task_table['priority_level'])))
priority_table = table(np.array(task_table.get_raw())[indicies])
indicies = np.argsort(priority_table['due_date'],kind='mergesort')
data = np.vstack((priority_table.get_raw()[indicies][-1],priority_table.get_raw()[indicies][:-1]))
sorted_tasks = table(data)
tasks = data[1:]
task_queue = queue(tasks[0])
for task in tasks[1:]:
    task_queue.push(task)

to_do = []
for i in range(20):
    to_do.append(task_queue.pop())
origins = ""
for task in to_do:
    origins = origins + ';' + patient_table['street_address'][int(task[2])].replace(' ',',')
origins = origins[1:]
(adjacency, probability) = get_matrices(origins)
print(largest_eigenvector(probability))


#print(adjacency, probability)