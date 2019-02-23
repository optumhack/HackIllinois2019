import numpy as np
class mat:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        found = False
        for i in range(len(self.data[0])):
            if self.data[0][i] == key:
                found = True
                break
        if found == False:
            raise KeyError('Key not found')
        return np.array([row[i] for row in self.data[1:]])

