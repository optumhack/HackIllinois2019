import numpy as np
import scipy.linalg as la
import json
from mat import mat as table
def largest_eigenvector(probability_matrix):
    #Start with random vector and get largest eigenvector out of probability
    vec = np.array([1,1,1,1,1])
    for i in range(10):
        vec = probability_matrix@vec
        vec = vec/(la.norm(vec))
    return vec
#Put employee information into usable Dictionary or object


#Put patient information into usable Dictionary or object


#Put task information into usable Dictionary or object
f = open('Data Files/CSV/TASK_DATA.csv','r')
lines = f.read().split('\n')
f.close()
task_table = table([line.split(',') for line in lines])


#Run and parse API
key = 'Aoo6MSOdOhu7_gENweR-26VzV-fP83hR3kCT3EouCWeQdF_uyhsT2kx5ZWqyffI2'
origins = '45.5347,-122.6231;47.4747,-122.2057;47.6044,-122.3345;47.6731,-122.1185;47.6149,-122.1936'
destinations = '45.5347,-122.6231;47.4747,-122.2057;47.6044,-122.3345;47.6731,-122.1185;47.6149,-122.1936'
API_url = 'https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins='+origins+'&destinations='+destinations+'&travelMode=driving&key='+key

f = open('examplejson.txt','r')
data_string = f.read()
f.close()
parsed_json = json.loads(data_string)
#Process data

n = 5
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

