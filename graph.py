import matplotlib.pyplot as plt
import numpy as np
import csv

files = [                        #list files in array, to be graphed
    'I-NB-107-C3-WT Cont.csv',	 #names are extracted from the end of the file name
    'I-NB-107-A1-D96A.csv',
    'I-NB-107-B1-K78E.csv',
    'I-NB-107-C1-R105A.csv',
    'I-NB-107-D1-Y473A.csv',
    'I-NB-107-E1-S265A.csv',
    'I-NB-107-F1-S266A.csv',
    'I-NB-107-G1-T267A.csv',
    'I-NB-107-H1-S324A.csv',
    'I-NB-107-A2-T379A.csv',
    'I-NB-107-B2-K377A.csv',
    'I-NB-107-C2-D502A.csv',
    'I-NB-107-D2-E504A.csv',
    'I-NB-107-E2-L558A.csv',
    'I-NB-107-G2-D562A.csv',
    'I-NB-107-H2-T616A.csv',
    'I-NB-107-A3-T618A.csv',
    'I-NB-107-B3-Negative Control.csv'
]

x_offset = 1.5
y_offset = 10000

x_offset_text = 33
y_offset_text = 8500

x_values = []
y_values = []

for idx in range(len(files)):
    file = files[idx]
    file_number = idx + 1
    
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader) #skip first line (metadata)
        next(csv_reader) #skip second line (headers)

        initial_x_offset = x_offset * file_number
        initial_y_offset = y_offset * file_number
        file_x_values = [initial_x_offset]
        file_y_values = [initial_y_offset]
        
        for row in csv_reader:
            file_x_values.append(float(row[1]) + initial_x_offset)
            file_y_values.append(float(row[2]) + initial_y_offset)
        
        x_values.append(file_x_values)
        y_values.append(file_y_values)

plt.figure(figsize=(9, 9))
plt.xlim(0,70)

plt.xlabel('Minutes')
plt.ylabel('EIC = XXX.XXXX (Counts)')
plt.title(‘LC/MS Screen')

for idx in reversed(range(len(files))):
    color = 'k' if idx == 0 or idx == len(files)-1 else 'm'
    plt.plot(x_values[idx],y_values[idx],color=color)
    plt.text( x_offset_text+x_offset*idx, y_offset_text+y_offset*idx, files[idx][12:len(files[idx])-4] )


#plt.show()
plt.savefig(‘graph.png', dpi=300)