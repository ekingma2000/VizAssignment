import csv 
import matplotlib.pyplot as plt
 
ausGold = 0, ausSilver = 0, ausBronze = 0, aut = 0, bel = 0, blr = 0, bul = 0, can = 0, chn = 0, cro = 0, cze= 0, esp= 0
est= 0, eua= 0, eun= 0, fin= 0, fra= 0, frg= 0, gbr= 0, gdr= 0, ger = 0, hun= 0, ita= 0
jpn= 0, kaz= 0, kor= 0, lat = 0, lie= 0, lux= 0, ned= 0, nor= 0, pol= 0, rou= 0, rus= 0
slo= 0, sui = 0, swe= 0, tch= 0, ukr= 0, urs= 0, usa= 0, yug= 0, nzl =0, prk=0, svk =0
uzb = 0

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

			elif (row[4] == "AUT"):
				aut += 1 

			elif (row[4] == "BEL"):
				bel += 1 

			elif (row[4] == "BLR"):
				blr += 1 

			elif (row[4] == "BUL"):
				bul += 1 

			elif (row[4] == "CAN"):
				can += 1 

			elif (row[4] == "CHN"):
				chn += 1 

			elif (row[4] == "CRO"):
				cro += 1 

			elif (row[4] == "CZN"):
				cze += 1 

			elif (row[4] == "ESP"):
				esp += 1 

			elif (row[4] == "EST"):
				est += 1 

			elif (row[4] == "EUA"):
				eua += 1 

			elif (row[4] == "EUN"):
				eun += 1 

			elif (row[4] == "FIN"):
				fin += 1 

			elif (row[4] == "FRA"):
				fra += 1 

			elif (row[4] == "FRG"):
				frg += 1 

			elif (row[4] == "GBR"):
				gbr += 1 

			elif (row[4] == "GER"):
				ger += 1 

			elif (row[4] == "HUN"):
				hun += 1 

			elif (row[4] == "ITA"):
				ita += 1 

			elif (row[4] == "JPN"):
				jpn += 1 

			elif (row[4] == "KAZ"):
				kaz += 1 

			elif (row[4] == "KOR"):
				kor += 1 

			elif (row[4] == "LAT"):
				lat += 1 

			elif (row[4] == "LIE"):
				lie += 1 

			elif (row[4] == "LUX"):
				lux += 1 

			elif (row[4] == "NED"):
				ned += 1 

			elif (row[4] == "NOR"):
				nor += 1 

			elif (row[4] == "POL"):
				pol += 1 

			elif (row[4] == "ROU"):
				rou+= 1 

			elif (row[4] == "RUS"):
				rus += 1 

			elif (row[4] == "SLO"):
				slo += 1 

			elif (row[4] == "SUI"):
				sui += 1 

			elif (row[4] == "SWE"):
				swe += 1 

			elif (row[4] == "TCH"):
				tch += 1 

			elif (row[4] == "UKR"):
				ukr += 1 

			elif (row[4] == "URS"):
				urs += 1 

			elif (row[4] == "USA"):
				usa += 1 

			elif (row[4] == "YUG"):
				yug += 1 

			elif (row[4] == "NZL"):
				nzl += 1 

			elif (row[4] == "SVK"):
				svk += 1 

			elif (row[4] == "UZB"):
				uzb += 1 

# Chart

