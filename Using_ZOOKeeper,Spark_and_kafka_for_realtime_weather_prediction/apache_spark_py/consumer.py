from kafka import *
import os

consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                                 auto_offset_reset='earliest')
consumer.subscribe(['test'])


class TempData:
	def parse(self, line):
		fields = line.split(',')
		self.humidity = fields[0]
		self.windspeed = fields[1]
		self.timestamp = fields[2]
		self.temperature= fields[3]

		return self
	def __repr__(self):
		return 'humidity = %s, windspeed = %s, timestamp = %s, temperature = %s' % (self.humidity, self.windspeed, self.timestamp, self.temperature)

	def to_json(self):
		return '{ "humidity":"%s", "windspeed":"%s", "timestamp":\"%s\", "temperature":"%s" }'%(self.humidity, self.windspeed, self.timestamp, self.temperature)



datafile = open ("output.txt", "a", 0)
jsonfile = open ("tempJson.json", "a", 0)

jsonfile.write("[{ \"humidity\":\"3.08680013442\", \"windspeed\":\"1\", \"timestamp\":\"2016-05-12 20:24:57.945850\", \"temperature\":\"44\" } ]")

for message in consumer:
	line = str(message).split("value=")
	first_part = line[1].split(")")
	data = first_part[0].split("\'")
	datafile.write(data[1] + "\n")
	print data[1]

	json_string = TempData().parse(data[1])
	json_data = json_string.to_json()

	jsonfile.seek(-1, os.SEEK_END) #remove the last ]
	jsonfile.truncate()
	jsonfile.write(",\n")
	jsonfile.write(json_data)
	jsonfile.write("]")


