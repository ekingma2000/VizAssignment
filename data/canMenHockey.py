import csv 
import matplotlib.pyplot as plt
import numpy as np

golds = []
silvers = []
bronzes = []

categories = []

with open('winterOlympicsMenCanHockey - Sheet1.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0

	for row in reader:
		if line_count is 0:
			
			categories.append(row)
			line_count += 1

		else:
			if row[7] == "Gold":
				golds.append(row[7])

			elif row[7] == "Silver":
				silvers.append(row[7])

			elif row[7] == "Bronze":
				bronzes.append(row[7])

			line_count += 1

print("gold medals: ", len(golds))
print("silver medals: ", len(silvers))
print("bronze medals: ", len(bronzes))

size=[len(golds), len(silvers), len(bronzes)]
names='Gold: 139', 'Silver: 76', 'Bronze: 35'

plt.pie(size, labels=names, colors=('gold', 'silver', 'darkgoldenrod'))


plt.title("Medals for Canadian Men's Hockey")
plt.xlabel("Medals from 1924 - 2014")
plt.show()

