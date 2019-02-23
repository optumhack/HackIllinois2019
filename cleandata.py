f = open('Data Files/CSV/TASK_DATA.csv')
lines = f.readlines()
f.close()
newlines = []
newlines.append(lines[0])
for line in lines[1:]:
    try:
        if float(line.split(',')[2]) > 100:
            continue
        newlines.append(line)
    except:
        pass

g = open('Data Files/CSV/NEW_TASK_DATA.csv','w+')
g.writelines(newlines)
g.close()