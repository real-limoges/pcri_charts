OPEN_PATH = "K:/Producers/Released Database/Version 2.2/SQL_Exported_Files"
SAVE_PATH = "K:/Producers/Released Database/Version 2.2/Dashboard"

SAVE_PATH = "K:/Producers/Released Database/Version 2.2/Dashboard"

bar_colors = [(31,119,180), (171,171,171), (89,89,89), (255,152,150),
			  (197,176,213), (196,156,148), (247,182,210), (199,199,199),
			  (219,219,141), (158,218,229)]

pie_colors = [(31,119,180), (174,199,232), (255,127,14), (255,187,120),
			  (44,160,44), (152,223,138), (214,39,40), (255,152,150),
			  (148,103,189), (197,176,213), (140,86,75), (196,156,148),
			  (227,119,194), (247,182,210), (127,127,127), (199,199,199),
			  (188,189,34), (219,219,141), (23,190,207), (158,218,229)]

bar_colors = bar_colors * 2

for i in range(len(bar_colors)):
	r,g,b = bar_colors[i]
	bar_colors[i] = (r/255., g/255., b/255.)

for i in range(len(pie_colors)):
	r,g,b = pie_colors[i]
	pie_colors[i] = (r/255., g/255., b/255.)

fund_type_replace = {"BUYOUT" : "Buyout",
					 "GROWTH EQUITY" : "Growth Equity",
					 "OTHER" : "Other",
					 "SECOND" : "Secondary",
					 "VC" : "VC"}

region_replace = {"AFRICA": "Africa",
				  "ASIA" : "Asia",
				  "EURASIA" : "Eurasia",
				  "EUROPE" : "Europe",
				  "MIDDLE EAST" : "Middle East",
				  "MULTIGEOGRAPHY" : "Multi-Geography",
				  "NORTH AMERICA" : "North America",
				  "OCEANIA" : "Oceania",
				  "SOUTH AMERICA" : "South America",
				  "UNITED STATES" : "United States"}