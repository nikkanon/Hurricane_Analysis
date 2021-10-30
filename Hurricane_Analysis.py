# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
# Hurricanes, also known as cyclones or typhoons, are one of the most powerful forces of nature on Earth. Due to climate change caused by human activity, the number and intensity of hurricanes 
# has risen, calling for better preparation by the many communities that are devastated by them. As a concerned environmentalist, you want to look at data about the most powerful hurricanes that have occurred.
# Begin by looking at the damages list. The list contains strings representing the total cost in USD($) caused by 34 category 5 hurricanes (wind speeds ≥ 157 mph (252 km/h )) in the Atlantic region. 
# For some of the hurricanes, damage data was not recorded ("Damages not recorded"), while the rest are written in the format "Prefix-B/M", where B stands for billions (1000000000) and M stands for millions (1000000).
# Write a function that returns a new list of updated damages where the recorded data is converted to float values and the missing data is retained as "Damages not recorded".
# Test your function with the data stored in damages.



def update_damages(list):
	fixed_damages = []
	for damages in list:
		if damages == "Damages not recorded":
			fixed_damages.append(damages)
		elif damages[-1] == "M":
			fixed_damages.append(float(damages[:-1])*1000000)
		elif damages[-1] == "B":
			fixed_damages.append(float(damages[:-1])*1000000000)
		else:
			continue
	return fixed_damages

print(update_damages(damages))
cleaned_damages = update_damages(damages)


# write your construct hurricane dictionary function here:
# Additional data collected on the 34 strongest Atlantic hurricanes are provided in a series of lists. The data includes:
# names: names of the hurricanes
# months: months in which the hurricanes occurred
# years: years in which the hurricanes occurred
# max_sustained_winds: maximum sustained winds (miles per hour) of the hurricanes
# areas_affected: list of different areas affected by each of the hurricanes
# deaths: total number of deaths caused by each of the hurricanes
# The data is organized such that the data at each index, from 0 to 33, corresponds to the same hurricane.

#For example, names[0] yields the “Cuba I” hurricane, which ouccred in months[0] (October) years[0] (1924).

#Write a function that constructs a dictionary made out of the lists, where the keys of the dictionary are the names of the hurricanes, and the values are dictionaries themselves containing a key for 
#each piece of data (Name, Month, Year,Max Sustained Wind, Areas Affected, Damage, Death) about the hurricane.

#Thus the key "Cuba I" would have the value: {'Name': 'Cuba I', 'Month': 'October', 'Year': 1924, 'Max Sustained Wind': 165, 'Areas Affected': ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 'Damage': 'Damages not recorded', 'Deaths': 90}.

#Test your function on the lists of data provided.

def construct_hurr_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
	hurr_dict = {}
	for i in range(len(names)):
		hurr_dict.update({names[i]: {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Winds": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": damages[i], "Deaths": deaths[i]}})
	return hurr_dict


print(construct_hurr_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths))
hurricane_name_dict = construct_hurr_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)



# write your construct hurricane by year dictionary function here:
# In addition to organizing the hurricanes in a dictionary with names as the key, you want to be able to organize the hurricanes by year.

# Write a function that converts the current dictionary of hurricanes to a new dictionary, where the keys are years and the values are lists containing a dictionary for each hurricane that occurred in that year.
# or example, the key 1932 would yield the value: [{'Name': 'Bahamas', 'Month': 'September', 'Year': 1932, 'Max Sustained Wind': 160, 'Areas Affected': ['The Bahamas', 'Northeastern United States'], 'Damage': 'Damages not recorded', 'Deaths': 16}, {'Name': 'Cuba II', 'Month': 'November', 'Year': 1932, 'Max Sustained Wind': 175, 'Areas Affected': ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 'Damage': 40000000.0, 'Deaths': 3103}].

# Test your function on your hurricane dictionary.

def year_hurr_dict(dict):
	year_dict = {}
	for key, value in dict.items():
		key = value.get("Year")
		year_dict.update({key: value})
	return year_dict

print(year_hurr_dict(hurricane_name_dict))
hurricane_year_dict = year_hurr_dict(hurricane_name_dict)



# write your count affected areas function here:
# You believe that knowing how often each of the areas of the Atlantic are affected by these strong hurricanes is important for making preparations for future hurricanes.
# Write a function that counts how often each area is listed as an affected area of a hurricane. Store and return the results in a dictionary where the keys are the affected areas and the values are counts of how many times the areas were affected.
# Test your function on your hurricane dictionary.

def occurance_area(dict):
	occur_dict = {}
	area_gross =[]
	for key, value in dict.items(): #build gross-list from hurrican dictionary, it will become a list of lists
		area_gross.append(value.get("Areas Affected")) 
	area_flat_list = []
	for area_list in area_gross: #convert the area gross list from list of lists to a area flat list
		for area in area_list:
			area_flat_list.append(area)
	for area in area_flat_list: #build occurance dictionary from area flat list
		if area in occur_dict:
			occur_dict[area] += 1
		else:
			occur_dict[area] = 1
	return occur_dict

print(occurance_area(hurricane_name_dict))
occurance_area_dict = occurance_area(hurricane_name_dict)


# write your find most affected area function here:
#Write a function that finds the area affected by the most hurricanes, and how often it was hit.

#Test your function on your affected area dictionary.
def most_affected_area(dict):
	maxi = 0
	most_affect = ""
	for key, value in dict.items():
		if value > maxi:
			maxi = value
			most_affect = key
		else:
			continue
	return most_affect

area_max = most_affected_area(occurance_area_dict)

print("This is the most affected area by hurricanes: " + str(area_max) + " it has been hit " + str(occurance_area_dict[str(area_max)]) + " times by a hurricanes")




# write your greatest number of deaths function here:

#Write a function that finds the hurricane that caused the greatest number of deaths, and how many deaths it caused.

#Test your function on your hurricane dictionary.

def most_deaths (dict):
	deadliest_hurr = ""
	max_deaths = 0
	for key, value in dict.items():
		if value["Deaths"] > max_deaths:
			max_deaths = value["Deaths"]
			deadliest_hurr = key
		else:
			continue
	return deadliest_hurr

deadliest_hurricane = most_deaths(hurricane_name_dict)
max_deaths = (hurricane_name_dict.get(deadliest_hurricane)).get("Deaths")
print("This is the most deadly hurricane: " + str(deadliest_hurricane) + " it has killed " + str(max_deaths) + " humans")



# write your catgeorize by mortality function here:

#Just as hurricanes are rated by their windspeed, you want to try rating hurricanes based on other metrics.

#Write a function that rates hurricanes on a mortality scale according to the following ratings, where the key is the rating and the value is the upper bound of deaths for that rating.

#mortality_scale = {0: 0,
#                   1: 100,
#                   2: 500,
#                   3: 1000,
#                   4: 10000}
#For example, a hurricane with a 1 mortality rating would have resulted in greater than 0 but less than or equal to 100 deaths. A hurricane with a 5 mortality rating would have resulted in greater than 10000 deaths.

#Store the hurricanes in a new dictionary where the keys are mortality ratings and the values are lists containing a dictionary for each hurricane that falls into that mortality rating.

#Test your function on your hurricane dictionary.

def mortality_dict(dict):
	mortal_dict = {}
	mortal_rating = 0
	for key, value in dict.items():
		if value.get("Deaths") > 0 and value.get("Deaths") <= 100:
			mortal_rating = 1
			mortal_dict[mortal_rating] = value
		elif value.get("Deaths") > 100 and value.get("Deaths") <= 500:
			mortal_rating = 2
			mortal_dict[mortal_rating] = value
		elif value.get("Deaths") > 500 and value.get("Deaths") <= 1000:
			mortal_rating = 3
			mortal_dict[mortal_rating] = value
		elif value.get("Deaths") > 1000 and value.get("Deaths") <= 10000:
			mortal_rating = 4
			mortal_dict[mortal_rating] = value
		elif value.get("Deaths") > 10000:
			mortal_rating = 5
			mortal_dict[mortal_rating] = value
		else:
			mortal_rating = 0
			mortal_dict[mortal_rating] = value
	return mortal_dict

print(mortality_dict(hurricane_name_dict))
mortality_rating_dict = mortality_dict(hurricane_name_dict)




# write your greatest damage function here:
#Write a function that finds the hurricane that caused the greatest damage, and how costly it was.

#Test your function on your hurricane dictionary.
def most_damage (dict):
	damage_hurr = ""
	max_dmg = 0
	for key, value in dict.items(): #clean up damages --> float
		if value["Damage"] == "Damages not recorded":
			value["Damage"] = 0
		elif value["Damage"][-1] == "M":
			value["Damage"] = int(float(value["Damage"][:-1])*1000000)
		elif damages[-1] == "B":
			value["Damage"] = int(float(value["Damage"][:-1])*1000000000)
		else:
			continue
	#for key, value in dict.items(): #now lets find the largest damage hurricane
	#	if value["Damage"] > max_dmg:
	#		max_dmg = int(value["Damage"])
	#		damage_hurr = key
	#	else:
	#		continue
	return dict

print(most_damage(hurricane_name_dict))
#max_damage = (hurricane_name_dict.get(dmg_hurricane)).get("Damage")
#print("This is the most deadly hurricane: " + str(dmg_hurricane) + " it has killed " + str(max_deaths) + " humans")



# write your catgeorize by damage function here:
