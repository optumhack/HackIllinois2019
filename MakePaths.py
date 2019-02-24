import numpy as np
import scipy.linalg as la
import json
import urllib.request as ur
from mat import mat as table
from queue import queue

API_INTERFACE = 'https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins='
KEY = 'Aoo6MSOdOhu7_gENweR-26VzV-fP83hR3kCT3EouCWeQdF_uyhsT2kx5ZWqyffI2'
POOL_SIZE = 20
class Nurse:
    def __init__(self, name, hours):
        self.employee_name = str(name)
        self.workable_hours = float(hours)
        self.tasks = []

    def get_hours(self):
        return self.workable_hours

    def get_name(self):
        return self.employee_name

    def can_work(self, hours):
        if hours <= self.workable_hours:
            return True
        return False

    def work(self, hours):
        new_hours = self.workable_hours - hours
        if new_hours < 0:
            raise ValueError("Nurse can't work that long")
        self.workable_hours = new_hours

    def set_tasks(self, task_list):
        self.tasks = task_list

    def __str__(self):
        return self.employee_name + ': [TASKS] ' + ', '.join(self.tasks)

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

#Put task type information into usable dictionary
f = open('Data Files/CSV/TASK_TYPE_DURATION.csv','r')
lines = f.read().split('\n')
f.close()
task_type = table([line.split(',') for line in lines])
type_time = {}
for line in lines[1:]:
    try:
        tokens = line.split(',')
        type_time[tokens[0]] = int(tokens[1])
    except:
        pass

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
"""
START OF PROCESSING
"""
#Generate task list
to_do = []

#GENERATING RANDOM NURSES FOR TESTING
nurses = [Nurse(str(i),8) for i in range(5)]

for nurse in nurses:
    new_entries = 0
    while len(to_do) < POOL_SIZE:
        to_do.append(task_queue.pop())
        new_entries += 1
    #Declare origins
    origins = ""
    #Add locations to origins
    for task in to_do:
        origins = origins + ';' + patient_table['street_address'][int(task[2])].replace(' ',',')
    #Clip initial semicolon
    origins = origins[1:]
    #Make graph matrices
    (adjacency, probability) = get_matrices(origins)
    pseudo_adjacency = adjacency.copy()
    pseudo_probability = probability.copy()
    #Apply factor to prioritize older units in task list 1.15 to ~double chances every 5 nurses
    for i in range(POOL_SIZE - new_entries):
        pseudo_adjacency[i,:] /= 1.15
        pseudo_adjacency[:,i] /= 1.15
        pseudo_probability[i,:] *= 1.15
        pseudo_probability[:,i] *= 1.15

    #Numerically get largest eigenvector for page-rank esque cluster finding
    eig = largest_eigenvector(pseudo_probability)
    #Start with points and keep track of visited locations
    points_left = list(range(POOL_SIZE))
    #Get most visited point
    current = np.argmax(eig)
    #Initializing "last" point
    last = current
    #Declare tasks array to keep track of what gets done
    tasks = []
    #Loop until nurse has no time
    while True:
        time = type_time[to_do[current][1]]
        #if nurse has time to do the job, do it
        if nurse.can_work(time):
            nurse.work(time)
        else:
            break
        #remove node
        points_left.remove(current)
        #add to completed tasks
        tasks.append(to_do[current][0])
        #get minimium remaining value in adjacency matrix
        minval = min(pseudo_adjacency[current][points_left])
        current = np.where(pseudo_adjacency[current] == minval)[0][0]
        #Give extra time driving so divide minutes by 45 instead of 60
        time = adjacency[current][last]/45
        if nurse.can_work(time):
            nurse.work(time)
        else:
            break
        last = current
    nurse.set_tasks(tasks)
    for task_number in tasks:
        for i in range(len(to_do)-1,-1,-1):
            if task_number == to_do[i][0]:
                del to_do[i]

for nurse in nurses:
    print(nurse)