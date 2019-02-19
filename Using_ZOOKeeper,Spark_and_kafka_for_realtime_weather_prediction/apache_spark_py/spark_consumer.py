#from __future__ import print_function


from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

from pyspark import *
from pyspark.streaming import *
from pyspark.streaming.kafka import *
from datetime import datetime, date


class TempData:
	def parse(self, line):
		fields = line.split(',')
		self.humidity = fields[0]
		self.windspeed = fields[1]
		self.timestamp = fields[2]
		self.temperature= float(fields[3])

		return self
	def __repr__(self):
		return 'humidity = %s, windspeed = %s, timestamp = %d, temperature = %s' % (self.humidity, self.windspeed, self.timestamp, self.temperature)

	def to_json(self):
		return '{ "humidity":"%s", "windspeed":"%s", "timestamp":%d, "temperature":"%s"}'%(self.humidity, self.windspeed, self.timestamp, self.temperature)


def getStreamingData():
	sc = SparkContext(appName="spark_temperature_processor")
	ssc = StreamingContext(sc, 1)
	zkQuorum = 'localhost:2181'
	topic = 'test'

	kvs = KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {topic: 1})

	lines = kvs.map(lambda x: x[1])
	lines.pprint()
	fo.write(str(lines))

	
	#counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
	#counts.pprint()


	#.reduceByKey(lambda a,b : "hot" if int(b) > 90 else "cold")
	#maxt.saveAsTextFile("kk.txt")

	maxt = lines.map(lambda x: x[0])
	maxt.pprint()

	ssc.start()
	ssc.awaitTermination() #terminate in 5 seconds
	

