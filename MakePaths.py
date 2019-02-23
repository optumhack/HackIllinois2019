import numpy as np
import json
#Put employee information into usable Dictionary or object


#Put patient information into usable Dictionary or object


#Put task information into usable Dictionary or object

#Run and parse API
key = 'Aoo6MSOdOhu7_gENweR-26VzV-fP83hR3kCT3EouCWeQdF_uyhsT2kx5ZWqyffI2'
origins = '45.5347,-122.6231;47.4747,-122.2057;47.6044,-122.3345;47.6731,-122.1185;47.6149,-122.1936'
destinations = '45.5347,-122.6231;47.4747,-122.2057;47.6044,-122.3345;47.6731,-122.1185;47.6149,-122.1936'
API_url = 'https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins='+origins+'&destinations='+destinations+'&travelMode=driving&key='+key

f = open('examplejson.txt','r')
data_string = f.read()
parsed_json = json.loads(data_string)
#Process data

n = 5
#n = len(addresses)
connections = parsed_json['resourceSets'][0]['resources'][0]['results']
adjacency_matrix = np.zeros((n,n))
for connection in connections:
    dest = connection['destinationIndex']
    origin = connection['originIndex']
    adjacency_matrix[dest][origin] = connection['travelDuration']
    adjacency_matrix[origin][dest] = connection['travelDuration']
for i in range(n):
    adjacency_matrix[i][i] = 9999999

print(adjacency_matrix)