import csv 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ausGold=0 
ausSilver=0 
ausBronze=0



categories = []

with open('winterOlympicsMen - Sheet1.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0

	for row in reader:
		if line_count is 0:
			# parse that first row of text data out of the file
			categories.append(row)
			line_count += 1

		else:
			if (row[7] == "Gold" and row[4] == "AUS"):
				ausGold += 1 
			elif (row[7] == "Silver" and row[4] == "AUS"):
				ausSilver += 1 
			elif (row[7] == "Bronze" and row[4] == "AUS"):
				ausBronze += 1 

medals = [ausGold, ausSilver, ausBronze]

df = pd.DataFrame({'group':list(map(chr, range(65, 85))), 'values':np.random.uniform(size=3) })
 
# Reorder it following the values:
ordered_df = df.sort_values(by='values')
my_range=range(1,len(df.index)+1)
 
# Make the plot
plt.stem(ordered_df['values'])
plt.xticks( my_range, ordered_df['group'])

plt.show()
