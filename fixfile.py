from pathlib import Path
import pandas as pd 
import xlrd
import csv
from pprint import pprint

filename = "C:/Users/Big Stupid/Downloads/BarTrackingList.csv"

r = csv.reader(open(filename)) # Here your csv file
lines = list(r)

#df = pd.read_csv("C:/Users/Big Stupid/Downloads/BarTrackingList.csv")

firstline = lines[0][0:3]

print(firstline)

for p in range(12):
	for w in range(4):
		cell = "P" + str(p + 1) + "W" + str(w + 1)

		firstline.append("Start Amount " + cell)
		firstline.append("End Amount " + cell)
		firstline.append("Purchase Amount " + cell)
		firstline.append("Sold Amount " + cell)

		# x = 3 + 4 * w + 16 * p

lines[0] = firstline

# print(firstline)


# pprint(lines)

with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(lines)

#print(df)