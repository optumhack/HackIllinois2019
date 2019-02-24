import numpy as np
class mat:
    def __init__(self, data):
        height = len(data)
        width = len(data[0])
        for i in range(height -1, -1, -1):
            if len(data[i]) < width:
                del data[i]
        self.data = data

    #returns a column using the key which names the column name
    def __getitem__(self, key):
        found = False
        index = None
        for i in range(len(self.data[0])):
            if self.data[0][i].upper() == key.upper():
                found = True
                index = i
                break
        if found == False:
            raise KeyError('Key not found')
        return np.array([row[index] for row in self.data])

    #returns the raw data
    def get_raw(self):
        return self.data

