
import random

filename = open ("cities.csv")

city_list = filename.readlines()

for city in city_list:
	city_data = city.split(',')

	current_city = city_data[2] 
	current_temp = random.randint(-40, 140)

	print current_temp, current_city