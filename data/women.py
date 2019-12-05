import csv 
import matplotlib.pyplot as plt
import numpy as np

nor=0
can=0
fin=0 
urs=0 
usa=0


categories = []

with open('winterOlympicsWomen - Sheet1.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0

	for row in reader:
		if line_count is 0:
			# parse that first row of text data out of the file
			categories.append(row)
			line_count += 1

		else:
			if (row[7] == "Gold" and row[4] == "CAN"):
				can += 1 


			elif (row[7] == "Gold" and row[4] == "FIN"):
				fin += 1 


			elif (row[7] == "Gold" and row[4] == "NOR"):
				nor += 1 


			elif (row[7] == "Gold" and row[4] == "URS"):
				urs += 1
 

			elif (row[7] == "Gold" and row[4] == "USA"):
				usa += 1 


# Make a fake dataset:
height = [can, fin, nor, urs, usa]

bars = ('CAN','FIN','NOR','URS', 'USA')

y_pos = np.arange(len(bars))
 
# Create bars
plt.bar(y_pos, height, color='gold')
 
# Create names on the x-axis
plt.xticks(y_pos, bars)
plt.title("Women's Gold Medals in the Top 5 Countries")
 
# Show graphic
plt.show()
