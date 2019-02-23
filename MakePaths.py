import numpy as np
import scipy.linalg as la
import json
import urllib.request as ur
from mat import mat as table

API_INTERFACE = 'https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins='
KEY = 'Aoo6MSOdOhu7_gENweR-26VzV-fP83hR3kCT3EouCWeQdF_uyhsT2kx5ZWqyffI2'
def largest_eigenvector(probability_matrix):
    #Start with random vector and get largest eigenvector out of probability
    vec = np.array([1,1,1,1,1])
    for i in range(10):
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

#Put task type information into usable table object
f = open('Data Files/CSV/EMPLOYEE_DATA.csv','r')
lines = f.read().split('\n')
f.close()
employee_table = table([line.split(',') for line in lines])

#Put task type information into usable table object
f = open('Data Files/CSV/PATIENT_DATA.csv','r')
lines = f.read().split('\n')
f.close()
patient_table = table([line.split(',') for line in lines])

#Put task type information into usable table object
f = open('Data Files/CSV/TASK_DATA.csv','r')
lines = f.read().split('\n')
f.close()
task_table = table([line.split(',') for line in lines])

#Put task type information into usable table object
f = open('Data Files/CSV/TASK_TYPE_DURATION.csv','r')
lines = f.read().split('\n')
f.close()
task_type = table([line.split(',') for line in lines])


(adjacency, probability) = get_matrices(origins)

print(adjacency, probability)