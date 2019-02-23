import numpy as np
f = open('Data Files/CSV/PATIENT_DATA.csv')
lines = f.readlines()
f.close()
newlines = []
newlines.append(lines[0])

base_area = (45.5347,-122.6231)
for line in lines[1:]:
    try:
        linelist = line.split(',')
        linelist[3] = str(base_area[0] + np.random.randn()/5) + ',' + str(base_area[1] + np.random.randn()/5)
        newlines.append(','.join(linelist))
    except:
        pass

g = open('Data Files/CSV/NEW_PATIENT_DATA.csv','w+')
g.writelines(newlines)
g.close()
