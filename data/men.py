import csv 
import matplotlib.pyplot as plt
import numpy as np
 
ausGold=[]
autGold=[]
belGold=[]
blrGold=[] 
bulGold=[]
canGold=[]
chnGold=[]
croGold=[] 
czeGold=[]
espGold=[]
estGold=[]
eunGold=[]
finGold=[] 
fraGold=[]
frgGold=[]
gbrGold=[] 
gdrGold=[] 
gerGold=[]
hunGold=[]
itaGold=[] 
jpnGold=[]
kazGold=[]
korGold=[]
latGold=[]
lieGold=[]
luxGold=[]
nedGold=[]
polGold=[]
rouGold=[] 
rusGold=[] 
sloGold=[]
suiGold=[]
sweGold=[] 
tchGold=[] 
ukrGold=[]
ursGold=[] 
usaGold=[]
yugGold=[]
nzlGold=[]
prkGold=[] 
svkGold=[] 
uzbGold=[] 
norGold=[]
euaGold=[]

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

			elif (row[7] == "Gold" and row[4] == "AUT"):
				autGold += 1 

			elif (row[7] == "Gold" and row[4] == "BEL"):
				belGold += 1 
	
			elif (row[7] == "Gold" and row[4] == "BLR"):
				blrGold += 1 

			elif (row[7] == "Gold" and row[4] == "BUL"):
				bulGold += 1
		
			elif (row[7] == "Gold" and row[4] == "CAN"):
				canGold += 1 

			elif (row[7] == "Gold" and row[4] == "CHN"):
				chnGold += 1 

			elif (row[7] == "Gold" and row[4] == "CRO"):
				croGold += 1 

			elif (row[7] == "Gold" and row[4] == "CZN"):
				cznGold += 1


			elif (row[7] == "Gold" and row[4] == "ESP"):
				espGold += 1 


			elif (row[7] == "Gold" and row[4] == "EST"):
				estGold += 1 


			elif (row[7] == "Gold" and row[4] == "EUA"):
				euaGold += 1 


			elif (row[7] == "Gold" and row[4] == "EUN"):
				eunGold += 1 


			elif (row[7] == "Gold" and row[4] == "FIN"):
				finGold += 1 


			elif (row[7] == "Gold" and row[4] == "FRA"):
				fraGold += 1 
	
			elif (row[7] == "Gold" and row[4] == "FRG"):
				frgGold += 1 


			elif (row[7] == "Gold" and row[4] == "GBR"):
				gbrGold += 1 


			elif (row[7] == "Gold" and row[4] == "GER"):
				gerGold += 1 


			elif (row[7] == "Gold" and row[4] == "HUN"):
				hunGold += 1 

			elif (row[7] == "Gold" and row[4] == "ITA"):
				itaGold += 1 


			elif (row[7] == "Gold" and row[4] == "JPN"):
				jpnGold += 1


			elif (row[7] == "Gold" and row[4] == "KAZ"):
				kazGold += 1


			elif (row[7] == "Gold" and row[4] == "KOR"):
				korGold += 1  


			elif (row[7] == "Gold" and row[4] == "LAT"):
				latGold += 1


			elif (row[7] == "Gold" and row[4] == "LIE"):
				lieGold += 1 


			elif (row[7] == "Gold" and row[4] == "LUX"):
				luxGold += 1 


			elif (row[7] == "Gold" and row[4] == "NED"):
				nedGold += 1


			elif (row[7] == "Gold" and row[4] == "NOR"):
				norGold += 1 

			elif (row[7] == "Gold" and row[4] == "POL"):
				polGold += 1 
		
			elif (row[7] == "Gold" and row[4] == "ROU"):
				rouGold += 1 

			elif (row[7] == "Gold" and row[4] == "RUS"):
				rusGold += 1 


			elif (row[7] == "Gold" and row[4] == "SLO"):
				sloGold += 1


			elif (row[7] == "Gold" and row[4] == "SUI"):
				suiGold += 1 


			elif (row[7] == "Gold" and row[4] == "SWE"):
				sweGold += 1 


			elif (row[7] == "Gold" and row[4] == "TCH"):
				tchGold += 1 
	

			elif (row[7] == "Gold" and row[4] == "UKR"):
				ukrGold += 1 


			elif (row[7] == "Gold" and row[4] == "URS"):
				ursGold += 1
 

			elif (row[7] == "Gold" and row[4] == "USA"):
				usaGold += 1 


			elif (row[7] == "Gold" and row[4] == "YUG"):
				yugGold += 1 


			elif (row[7] == "Gold" and row[4] == "NZL"):
				nzlGold += 1 


			elif (row[7] == "Gold" and row[4] == "SVK"):
				svkGold += 1 


			elif (row[7] == "Gold" and row[4] == "UZB"):
				uzbGold += 1

			

# Chart

golds = (ausGold, autGold, belGold, canGold, chnGold, croGold, czeGold, espGold, estGold,euaGold,eunGold,
finGold ,fraGold ,frgGold,gbrGold ,gdrGold,gerGold,hunGold,itaGold,jpnGold,kazGold ,korGold,latGold,
lieGold,luxGold ,nedGold,norGold,polGold,rouGold,rusGold,suiGold,sweGold,tchGold,ukrGold,ursGold, 
usaGold ,yugGold,nzlGold,prkGold,svkGold,uzbGold)

bars = ('AUS', 'AUT', 'bel','blr', 'bul','can','chn',
'cro', 'cze','esp','est','eua','eun','fin', 'fra','frg','gbr','gdr','ger','hun','ita', 'jpn','kaz', 
'kor','lat', 'lie','lux','ned','nor','pol','rou','rus','slo','sui','swe','tch', 'ukr','urs', 'usa', 
'yug','nzl', 'prk','svk','uzb')
height = [len(ausGold), len(autGold), len(belGold), len(canGold), len(chnGold), len(croGold), 
len(czeGold), len(espGold), len(estGold),len(euaGold),len(eunGold),len(finGold) ,len(fraGold) ,
len(frgGold), len(gbrGold) ,len(gdrGold), len(gerGold),len(hunGold),len(itaGold),len(jpnGold),
len(kazGold) ,len(korGold),len(latGold),len(lieGold),len(luxGold) ,len(nedGold),len(norGold),
len(polGold),len(rouGold),len(rusGold),len(suiGold),len(sweGold),len(tchGold),len(ukrGold),
len(ursGold), len(usaGold) ,len(yugGold),len(nzlGold),len(prkGold),len(svkGold),len(uzbGold)]

y_pos = np.arange(len(bars))
plt.bar(y_pos, height, color=("gold"))
plt.xticks(y_pos, bars)

plt.title("Medals for Canadian Men's Hockey")
plt.xlabel("Medals from 1924 - 2014")
plt.show()


#plt.bar (r1, bar1, color='gold', width=barWidth, label='gold')
#plt.bar (r2, bar2, color='silver', width=barWidth, label='silver')
#plt.bar (r3, bar3, color='darkgoldenrod', width=barWidth, label='bronze')

#plt.xlabel('countries')
#plt.xticks([r + barWidth for r in range(len(bar1))], ['AUS', 'AUT', 'bel','blr', 'bul','can','chn',
#'cro', 'cze','esp','est','eua','eun','fin', 'fra','frg','gbr','gdr','ger','hun','ita', 'jpn','kaz', 
#'kor','lat', 'lie','lux','ned','nor','pol','rou','rus','slo','sui','swe','tch', 'ukr','urs', 'usa', 
#'yug','nzl', 'prk','svk','uzb',])

#plt.legend()
#plt.show()




























