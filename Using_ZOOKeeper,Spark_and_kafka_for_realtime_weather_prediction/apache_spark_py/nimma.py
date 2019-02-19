
import random


cities_file = open("cities.csv", "r+")

city_list = cities_file.readlines()


city_nice_list  = []

for city in city_list:
	city_details = city.split(",")

	city_details.append(random.randint(-40, 100))

	city_nice_list.append(city_details)

	


temperatures = map(lambda x: x[5], city_nice_list)

states = map(lambda x: x[1], city_nice_list)

stat_temp = map(lambda x: [x[1], x[5]], city_nice_list)

odd_temps = filter(lambda x: x%2 == 1, temperatures)

even_temps = filter(lambda x: x%2==0, map(lambda x: x[5], city_nice_list))

sum_of_temps = reduce(lambda x, y: x+ y, temperatures)

number_of_temps = reduce(lambda x, y: x+ y, map(lambda x: 1, temperatures))

wstates = filter(lambda x: x[0] == "W", states)


alist = [(1,2), (2,4), (5,6), (7,7), (6,9)]


#sum of all odd second elements of alist

result = reduce(lambda x,y: x+y , filter(lambda x: x%2 ==1, map(lambda x: x[1], alist)))


print result







