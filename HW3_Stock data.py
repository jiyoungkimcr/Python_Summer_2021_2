'''
Write a program that searches for CSV files with stock rates in a given folder and for every one of them:
Calculates the percentage change between Close and Open price and adds these values as another column to this CSV file.
Code writer: Jiyoung Kim
'''

import os
import csv
from pip._vendor.distlib.compat import raw_input

print('Write a path of a folder containing csv files (please add slash at the end):')
path = raw_input()

counter = 0

for file in os.listdir(path):
    if file.endswith('.csv'):
        counter += 1
        filepath = path + file
        if file.endswith('.csv'):
            file_copy = filepath[:-4] + "_new.csv"
            with open(filepath, 'r') as input:
                with open(file_copy, 'w') as output:
                    reader = csv.reader(input)
                    writer = csv.writer(output)
                    row0 = next(reader)
                    row0.append('change_pct')
                    writer.writerow(row0)

                    for row in reader:
                        change_pct = ((float(row[4]) - float(row[1])) / float(row[1])) * 100
                        row.append(change_pct)
                        writer.writerow(row)
print("Please check your folder")