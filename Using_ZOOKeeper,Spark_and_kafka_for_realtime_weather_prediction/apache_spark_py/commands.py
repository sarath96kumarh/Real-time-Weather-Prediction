
#extract and launch zookeeper
tar -xzvf kafka_2.11-0.9.0.1.tgz
./bin/zookeeper-server-start.sh config/zookeeper.properties 

#start kafka server
./bin/kafka-server-start.sh config/server.properties 

#write producer for kafka (simulator) &  consumer for spark (spark_consumer)

#run producer
python producer.py 

#launch kafka consumer for observing logging 
bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic test --from-beginning

#submit spark consumer to spark-submit
./spark-1.6.1-bin-hadoop2.6/bin/spark-submit --packages org.apache.spark:spark-streaming-kafka_2.10:1.6.1 spark_consumer.py 


[{ "humidity":"3.08680013442", "windspeed":"1", "timestamp":"2016-05-12 20:24:57.945850", "temperature":"44" } ,
{ "humidity":"2.61546562825", "windspeed":"1", "timestamp":"2016-05-12 20:31:33.332557", "temperature":"37" },
{ "humidity":"2.21563938631", "windspeed":"4", "timestamp":"2016-05-12 20:31:38.336091", "temperature":"44" },
{ "humidity":"1.34599232331", "windspeed":"0", "timestamp":"2016-05-12 20:31:43.342614", "temperature":"42" },
{ "humidity":"4.18406826296", "windspeed":"1", "timestamp":"2016-05-12 20:31:48.344909", "temperature":"38" },
{ "humidity":"1.28614996947", "windspeed":"4", "timestamp":"2016-05-12 20:31:53.349097", "temperature":"37" },
{ "humidity":"0.153205129032", "windspeed":"4", "timestamp":"2016-05-12 20:31:58.356050", "temperature":"39" },
{ "humidity":"4.99674445201", "windspeed":"5", "timestamp":"2016-05-12 20:32:03.358778", "temperature":"38" },
{ "humidity":"2.97111097014", "windspeed":"4", "timestamp":"2016-05-12 20:32:08.365909", "temperature":"35" },
{ "humidity":"4.22140863393", "windspeed":"4", "timestamp":"2016-05-12 20:32:13.372237", "temperature":"35" },
{ "humidity":"2.07402374905", "windspeed":"3", "timestamp":"2016-05-12 20:32:18.378891", "temperature":"38" },
{ "humidity":"2.77192723243", "windspeed":"2", "timestamp":"2016-05-12 20:32:23.384587", "temperature":"44" },
{ "humidity":"4.59181610466", "windspeed":"2", "timestamp":"2016-05-12 20:32:28.391095", "temperature":"45" },
{ "humidity":"0.199837658928", "windspeed":"0", "timestamp":"2016-05-12 20:32:33.394990", "temperature":"39" },
{ "humidity":"0.438786595219", "windspeed":"1", "timestamp":"2016-05-12 20:32:38.400217", "temperature":"45" },
{ "humidity":"1.29284583318", "windspeed":"3", "timestamp":"2016-05-12 20:32:43.404848", "temperature":"43" },
{ "humidity":"2.99207584831", "windspeed":"4", "timestamp":"2016-05-12 20:32:48.410481", "temperature":"44" },
{ "humidity":"1.08337358927", "windspeed":"4", "timestamp":"2016-05-12 20:32:53.415543", "temperature":"43" },
{ "humidity":"2.36030373531", "windspeed":"1", "timestamp":"2016-05-12 20:32:58.418788", "temperature":"44" },
{ "humidity":"4.09077630483", "windspeed":"0", "timestamp":"2016-05-12 20:33:03.423532", "temperature":"43" },
{ "humidity":"3.87762986539", "windspeed":"0", "timestamp":"2016-05-12 20:33:08.425949", "temperature":"44" },
{ "humidity":"1.2820089158", "windspeed":"3", "timestamp":"2016-05-12 20:33:13.428606", "temperature":"40" },
{ "humidity":"2.72689331876", "windspeed":"2", "timestamp":"2016-05-12 20:33:18.435067", "temperature":"35" },
{ "humidity":"3.40040477956", "windspeed":"5", "timestamp":"2016-05-12 20:33:23.440235", "temperature":"44" },
{ "humidity":"3.49786475317", "windspeed":"2", "timestamp":"2016-05-12 20:33:28.444160", "temperature":"35" },
{ "humidity":"2.66941811399", "windspeed":"3", "timestamp":"2016-05-12 20:33:33.446265", "temperature":"36" },
{ "humidity":"2.87931543762", "windspeed":"5", "timestamp":"2016-05-12 20:33:38.449347", "temperature":"42" },
{ "humidity":"2.10595274881", "windspeed":"2", "timestamp":"2016-05-12 20:33:43.451923", "temperature":"41" },
{ "humidity":"1.96847361688", "windspeed":"2", "timestamp":"2016-05-12 20:33:48.454512", "temperature":"42" },
{ "humidity":"1.31465310558", "windspeed":"5", "timestamp":"2016-05-12 20:33:53.458277", "temperature":"35" },
{ "humidity":"4.27526631758", "windspeed":"3", "timestamp":"2016-05-12 20:33:58.464382", "temperature":"40" },
{ "humidity":"1.10198530725", "windspeed":"1", "timestamp":"2016-05-12 20:34:05.759169", "temperature":"36" },
{ "humidity":"2.59135393545", "windspeed":"1", "timestamp":"2016-05-12 20:34:10.818686", "temperature":"41" },
{ "humidity":"4.2102994506", "windspeed":"3", "timestamp":"2016-05-12 20:34:15.821594", "temperature":"35" },
{ "humidity":"4.86160837154", "windspeed":"1", "timestamp":"2016-05-12 20:34:20.824592", "temperature":"43" },
{ "humidity":"1.70348960509", "windspeed":"4", "timestamp":"2016-05-12 20:34:25.830579", "temperature":"41" },
{ "humidity":"3.13868786503", "windspeed":"2", "timestamp":"2016-05-12 20:34:30.833890", "temperature":"41" },
{ "humidity":"4.89756783728", "windspeed":"0", "timestamp":"2016-05-12 20:34:35.836440", "temperature":"38" },
{ "humidity":"3.8754414036", "windspeed":"3", "timestamp":"2016-05-12 20:34:40.840280", "temperature":"38" },
{ "humidity":"2.55260481109", "windspeed":"5", "timestamp":"2016-05-12 20:34:45.843693", "temperature":"38" },
{ "humidity":"2.7716031613", "windspeed":"3", "timestamp":"2016-05-12 20:34:50.849691", "temperature":"35" },
{ "humidity":"3.15000146099", "windspeed":"5", "timestamp":"2016-05-12 20:34:55.854241", "temperature":"36" },
{ "humidity":"1.84679421999", "windspeed":"5", "timestamp":"2016-05-12 20:35:00.856372", "temperature":"36" },
{ "humidity":"2.76543073287", "windspeed":"5", "timestamp":"2016-05-12 20:35:05.861087", "temperature":"36" },
{ "humidity":"2.27546631661", "windspeed":"4", "timestamp":"2016-05-12 20:35:10.866073", "temperature":"43" },
{ "humidity":"2.02713244002", "windspeed":"4", "timestamp":"2016-05-12 20:35:15.870872", "temperature":"35" },
{ "humidity":"0.895406265871", "windspeed":"2", "timestamp":"2016-05-12 20:35:20.874698", "temperature":"41" },
{ "humidity":"0.227508529848", "windspeed":"2", "timestamp":"2016-05-12 20:35:25.879637", "temperature":"42" },
{ "humidity":"2.17315004664", "windspeed":"0", "timestamp":"2016-05-12 20:35:30.882494", "temperature":"41" },
{ "humidity":"0.131230240156", "windspeed":"1", "timestamp":"2016-05-12 20:35:35.886675", "temperature":"38" },
{ "humidity":"2.0027814254", "windspeed":"0", "timestamp":"2016-05-12 20:35:40.891938", "temperature":"38" },
{ "humidity":"2.51847670304", "windspeed":"2", "timestamp":"2016-05-12 20:35:45.898183", "temperature":"44" },
{ "humidity":"4.62374858721", "windspeed":"0", "timestamp":"2016-05-12 20:35:50.901217", "temperature":"37" },
{ "humidity":"2.84902604298", "windspeed":"0", "timestamp":"2016-05-12 20:35:55.903593", "temperature":"41" },
{ "humidity":"3.69091597622", "windspeed":"3", "timestamp":"2016-05-12 20:36:00.911345", "temperature":"37" },
{ "humidity":"3.23264774387", "windspeed":"4", "timestamp":"2016-05-12 20:36:05.917746", "temperature":"35" },
{ "humidity":"1.81476485949", "windspeed":"0", "timestamp":"2016-05-12 20:36:10.921141", "temperature":"43" },
{ "humidity":"1.87010390198", "windspeed":"3", "timestamp":"2016-05-12 20:36:15.924389", "temperature":"45" },
{ "humidity":"0.254709688424", "windspeed":"0", "timestamp":"2016-05-12 20:36:20.928507", "temperature":"39" },
{ "humidity":"4.01655133773", "windspeed":"5", "timestamp":"2016-05-12 20:36:25.932855", "temperature":"39" },
{ "humidity":"2.36506861742", "windspeed":"0", "timestamp":"2016-05-12 20:36:30.938787", "temperature":"40" },
{ "humidity":"3.03905995457", "windspeed":"1", "timestamp":"2016-05-12 20:36:35.942865", "temperature":"45" },
{ "humidity":"0.0122196067957", "windspeed":"4", "timestamp":"2016-05-12 20:36:40.945269", "temperature":"42" },
{ "humidity":"0.817579939867", "windspeed":"1", "timestamp":"2016-05-12 20:36:45.948391", "temperature":"43" },
{ "humidity":"4.9981258056", "windspeed":"3", "timestamp":"2016-05-12 20:36:50.952094", "temperature":"38" },
{ "humidity":"2.03258585829", "windspeed":"4", "timestamp":"2016-05-12 20:36:55.959534", "temperature":"39" },
{ "humidity":"3.20048853208", "windspeed":"3", "timestamp":"2016-05-12 20:37:00.962855", "temperature":"35" },
{ "humidity":"4.87439112952", "windspeed":"2", "timestamp":"2016-05-12 20:37:05.968381", "temperature":"40" },
{ "humidity":"3.83052470389", "windspeed":"3", "timestamp":"2016-05-12 20:37:10.971338", "temperature":"36" },
{ "humidity":"2.65489803137", "windspeed":"4", "timestamp":"2016-05-12 20:37:15.978678", "temperature":"41" },
{ "humidity":"4.80292923895", "windspeed":"3", "timestamp":"2016-05-12 20:37:20.984652", "temperature":"41" },
{ "humidity":"0.458483345232", "windspeed":"5", "timestamp":"2016-05-12 20:37:25.988710", "temperature":"39" },
{ "humidity":"4.61733112334", "windspeed":"1", "timestamp":"2016-05-12 20:37:30.991189", "temperature":"40" },
{ "humidity":"1.87505459259", "windspeed":"0", "timestamp":"2016-05-12 20:37:35.994096", "temperature":"37" },
{ "humidity":"1.44557396489", "windspeed":"3", "timestamp":"2016-05-12 20:37:41.000491", "temperature":"36" },
{ "humidity":"1.68980194819", "windspeed":"0", "timestamp":"2016-05-12 20:37:46.006249", "temperature":"45" },
{ "humidity":"3.86675472657", "windspeed":"4", "timestamp":"2016-05-12 20:37:51.010745", "temperature":"39" },
{ "humidity":"0.177612732548", "windspeed":"4", "timestamp":"2016-05-12 20:37:56.016923", "temperature":"44" },
{ "humidity":"2.31489272788", "windspeed":"0", "timestamp":"2016-05-12 20:38:01.020237", "temperature":"37" },
{ "humidity":"3.11564452533", "windspeed":"4", "timestamp":"2016-05-12 20:38:06.025105", "temperature":"45" },
{ "humidity":"3.223637376", "windspeed":"1", "timestamp":"2016-05-12 20:38:11.030724", "temperature":"43" },
{ "humidity":"2.12991799962", "windspeed":"4", "timestamp":"2016-05-12 20:38:16.035922", "temperature":"38" },
{ "humidity":"4.28923714164", "windspeed":"1", "timestamp":"2016-05-12 20:38:21.043098", "temperature":"39" },
{ "humidity":"3.9393881039", "windspeed":"2", "timestamp":"2016-05-12 20:38:26.049719", "temperature":"38" },
{ "humidity":"2.49021323967", "windspeed":"3", "timestamp":"2016-05-12 20:38:31.054491", "temperature":"42" },
{ "humidity":"0.936874133569", "windspeed":"4", "timestamp":"2016-05-12 20:38:36.058788", "temperature":"39" },
{ "humidity":"3.73351508827", "windspeed":"1", "timestamp":"2016-05-12 20:38:41.062642", "temperature":"41" },
{ "humidity":"0.387151966771", "windspeed":"5", "timestamp":"2016-05-12 20:38:46.068778", "temperature":"35" },
{ "humidity":"0.67646945511", "windspeed":"4", "timestamp":"2016-05-12 20:38:51.071262", "temperature":"39" },
{ "humidity":"0.964040777452", "windspeed":"2", "timestamp":"2016-05-12 20:38:56.078456", "temperature":"43" },
{ "humidity":"4.28517392385", "windspeed":"0", "timestamp":"2016-05-12 20:39:01.081978", "temperature":"44" },
{ "humidity":"3.44157083888", "windspeed":"4", "timestamp":"2016-05-12 20:39:06.084972", "temperature":"38" },
{ "humidity":"2.23633994166", "windspeed":"4", "timestamp":"2016-05-12 20:39:11.089182", "temperature":"39" },
{ "humidity":"4.29355510071", "windspeed":"4", "timestamp":"2016-05-12 20:39:16.096359", "temperature":"39" },
{ "humidity":"2.82451406948", "windspeed":"0", "timestamp":"2016-05-12 20:39:21.100387", "temperature":"45" },
{ "humidity":"1.35958359845", "windspeed":"4", "timestamp":"2016-05-12 20:39:26.108754", "temperature":"41" },
{ "humidity":"4.52235176235", "windspeed":"5", "timestamp":"2016-05-12 20:39:31.114950", "temperature":"35" },
{ "humidity":"1.94168718364", "windspeed":"0", "timestamp":"2016-05-12 20:39:36.120130", "temperature":"35" },
{ "humidity":"2.85146692618", "windspeed":"0", "timestamp":"2016-05-12 20:39:41.126000", "temperature":"41" },
{ "humidity":"4.56938269295", "windspeed":"5", "timestamp":"2016-05-12 20:39:46.129611", "temperature":"45" },
{ "humidity":"3.54627369303", "windspeed":"4", "timestamp":"2016-05-12 20:39:51.135800", "temperature":"41" },
{ "humidity":"4.17659458059", "windspeed":"0", "timestamp":"2016-05-12 20:39:56.143393", "temperature":"40" },
{ "humidity":"4.32679073664", "windspeed":"4", "timestamp":"2016-05-12 20:40:01.147595", "temperature":"43" },
{ "humidity":"2.60282610101", "windspeed":"5", "timestamp":"2016-05-12 20:40:06.155075", "temperature":"35" },
{ "humidity":"4.38098296338", "windspeed":"3", "timestamp":"2016-05-12 20:40:11.159276", "temperature":"40" },
{ "humidity":"2.25794162986", "windspeed":"5", "timestamp":"2016-05-12 20:40:16.163907", "temperature":"45" },
{ "humidity":"3.35831434159", "windspeed":"2", "timestamp":"2016-05-12 20:40:21.171579", "temperature":"43" },
{ "humidity":"2.55270542937", "windspeed":"5", "timestamp":"2016-05-12 20:40:26.174969", "temperature":"45" },
{ "humidity":"1.44291584122", "windspeed":"0", "timestamp":"2016-05-12 20:40:31.180197", "temperature":"42" },
{ "humidity":"4.0280573357", "windspeed":"3", "timestamp":"2016-05-12 20:40:36.183002", "temperature":"42" },
{ "humidity":"2.75837264795", "windspeed":"5", "timestamp":"2016-05-12 20:40:41.189835", "temperature":"44" },
{ "humidity":"3.09493196786", "windspeed":"4", "timestamp":"2016-05-12 20:40:46.193843", "temperature":"44" },
{ "humidity":"1.59759248503", "windspeed":"2", "timestamp":"2016-05-12 20:40:51.201632", "temperature":"38" },
{ "humidity":"1.01355992516", "windspeed":"0", "timestamp":"2016-05-12 20:40:56.204379", "temperature":"41" },
{ "humidity":"0.82281698686", "windspeed":"1", "timestamp":"2016-05-12 20:41:01.209529", "temperature":"40" },
{ "humidity":"3.60797312982", "windspeed":"3", "timestamp":"2016-05-12 20:41:06.219160", "temperature":"43" },
{ "humidity":"3.74281782734", "windspeed":"4", "timestamp":"2016-05-12 20:41:11.223861", "temperature":"39" },
{ "humidity":"3.32515988509", "windspeed":"2", "timestamp":"2016-05-12 20:41:16.229120", "temperature":"37" },
{ "humidity":"0.916990527009", "windspeed":"0", "timestamp":"2016-05-12 20:41:21.233495", "temperature":"41" },
{ "humidity":"4.96136346279", "windspeed":"3", "timestamp":"2016-05-12 20:41:26.237729", "temperature":"38" },
{ "humidity":"2.46557850412", "windspeed":"2", "timestamp":"2016-05-12 20:41:31.245216", "temperature":"37" },
{ "humidity":"1.66771322694", "windspeed":"1", "timestamp":"2016-05-12 20:41:36.249959", "temperature":"39" },
{ "humidity":"3.9151539523", "windspeed":"1", "timestamp":"2016-05-12 20:41:41.253323", "temperature":"36" },
{ "humidity":"1.65008067702", "windspeed":"0", "timestamp":"2016-05-12 20:41:46.256207", "temperature":"35" },
{ "humidity":"0.398540928379", "windspeed":"2", "timestamp":"2016-05-12 20:41:51.261705", "temperature":"38" },
{ "humidity":"4.42161035296", "windspeed":"0", "timestamp":"2016-05-12 20:41:56.266697", "temperature":"40" },
{ "humidity":"2.70294086922", "windspeed":"5", "timestamp":"2016-05-12 20:42:01.272787", "temperature":"40" },
{ "humidity":"0.580984978868", "windspeed":"0", "timestamp":"2016-05-12 20:42:06.277957", "temperature":"44" },
{ "humidity":"1.50283183795", "windspeed":"2", "timestamp":"2016-05-12 20:42:11.283633", "temperature":"41" },
{ "humidity":"0.827425794856", "windspeed":"0", "timestamp":"2016-05-12 20:42:16.287507", "temperature":"41" },
{ "humidity":"3.21385071731", "windspeed":"2", "timestamp":"2016-05-12 20:42:21.292612", "temperature":"36" },
{ "humidity":"3.44009345405", "windspeed":"5", "timestamp":"2016-05-12 20:42:26.300001", "temperature":"38" },
{ "humidity":"1.95309441344", "windspeed":"0", "timestamp":"2016-05-12 20:42:31.304888", "temperature":"42" },
{ "humidity":"4.43112874798", "windspeed":"3", "timestamp":"2016-05-12 20:42:36.315846", "temperature":"40" },
{ "humidity":"4.96145523592", "windspeed":"4", "timestamp":"2016-05-12 20:42:41.320053", "temperature":"39" },
{ "humidity":"1.38217421857", "windspeed":"3", "timestamp":"2016-05-12 20:42:46.327079", "temperature":"44" },
{ "humidity":"0.0720244990322", "windspeed":"4", "timestamp":"2016-05-12 20:42:51.330991", "temperature":"38" },
{ "humidity":"4.41805048706", "windspeed":"3", "timestamp":"2016-05-12 20:42:56.338847", "temperature":"37" },
{ "humidity":"2.35879094927", "windspeed":"3", "timestamp":"2016-05-12 20:43:01.343260", "temperature":"42" },
{ "humidity":"4.38103103882", "windspeed":"0", "timestamp":"2016-05-12 20:43:06.347424", "temperature":"43" },
{ "humidity":"3.71783598266", "windspeed":"4", "timestamp":"2016-05-12 20:43:11.350875", "temperature":"37" },
{ "humidity":"4.33680545602", "windspeed":"0", "timestamp":"2016-05-12 20:43:16.358300", "temperature":"40" },
{ "humidity":"3.98087085617", "windspeed":"2", "timestamp":"2016-05-12 20:43:21.365746", "temperature":"45" },
{ "humidity":"2.37120090818", "windspeed":"5", "timestamp":"2016-05-12 20:43:26.370623", "temperature":"35" },
{ "humidity":"1.98014087068", "windspeed":"0", "timestamp":"2016-05-12 20:43:31.374948", "temperature":"35" },
{ "humidity":"3.87411031499", "windspeed":"0", "timestamp":"2016-05-12 20:43:36.380877", "temperature":"40" },
{ "humidity":"3.7742857123", "windspeed":"0", "timestamp":"2016-05-12 20:43:41.384056", "temperature":"44" },
{ "humidity":"0.249251878844", "windspeed":"0", "timestamp":"2016-05-12 20:43:46.389813", "temperature":"36" },
{ "humidity":"0.415106250549", "windspeed":"2", "timestamp":"2016-05-12 20:43:51.393368", "temperature":"42" },
{ "humidity":"4.36789733921", "windspeed":"5", "timestamp":"2016-05-12 20:43:56.395657", "temperature":"43" },
{ "humidity":"4.75796075754", "windspeed":"1", "timestamp":"2016-05-12 20:44:01.399976", "temperature":"41" },
{ "humidity":"4.71148094078", "windspeed":"0", "timestamp":"2016-05-12 20:44:06.403247", "temperature":"42" },
{ "humidity":"0.456319847879", "windspeed":"5", "timestamp":"2016-05-12 20:44:11.408441", "temperature":"36" },
{ "humidity":"2.27588226746", "windspeed":"2", "timestamp":"2016-05-12 20:44:16.412513", "temperature":"40" },
{ "humidity":"2.34168748698", "windspeed":"0", "timestamp":"2016-05-12 20:44:21.419540", "temperature":"40" },
{ "humidity":"2.09555605707", "windspeed":"5", "timestamp":"2016-05-12 20:44:26.423635", "temperature":"40" },
{ "humidity":"1.02410326964", "windspeed":"0", "timestamp":"2016-05-12 20:44:31.429191", "temperature":"44" },
{ "humidity":"3.58484865001", "windspeed":"3", "timestamp":"2016-05-12 20:44:36.436949", "temperature":"35" },
{ "humidity":"1.45518879564", "windspeed":"2", "timestamp":"2016-05-12 20:44:41.442898", "temperature":"42" },
{ "humidity":"1.11660147481", "windspeed":"0", "timestamp":"2016-05-12 20:44:46.448723", "temperature":"40" },
{ "humidity":"1.38340570996", "windspeed":"4", "timestamp":"2016-05-12 20:44:51.453378", "temperature":"45" },
{ "humidity":"1.2185970581", "windspeed":"1", "timestamp":"2016-05-12 20:44:56.456417", "temperature":"41" },
{ "humidity":"3.37001264328", "windspeed":"2", "timestamp":"2016-05-12 20:45:01.464119", "temperature":"35" },
{ "humidity":"3.03811333485", "windspeed":"3", "timestamp":"2016-05-12 20:45:06.470886", "temperature":"38" },
{ "humidity":"3.80706530269", "windspeed":"2", "timestamp":"2016-05-12 20:45:11.477367", "temperature":"40" },
{ "humidity":"3.35344006333", "windspeed":"5", "timestamp":"2016-05-12 20:45:16.482429", "temperature":"37" },
{ "humidity":"4.76969528267", "windspeed":"1", "timestamp":"2016-05-12 20:45:21.489822", "temperature":"44" },
{ "humidity":"2.16772328238", "windspeed":"3", "timestamp":"2016-05-12 20:45:26.494391", "temperature":"35" },
{ "humidity":"3.66885907802", "windspeed":"5", "timestamp":"2016-05-12 20:45:31.497204", "temperature":"44" },
{ "humidity":"1.72603517204", "windspeed":"1", "timestamp":"2016-05-12 20:45:36.502200", "temperature":"44" },
{ "humidity":"3.59301587371", "windspeed":"0", "timestamp":"2016-05-12 20:45:41.507135", "temperature":"36" },
{ "humidity":"4.16525755482", "windspeed":"0", "timestamp":"2016-05-12 20:45:46.509928", "temperature":"44" },
{ "humidity":"3.03173325797", "windspeed":"0", "timestamp":"2016-05-12 20:45:51.514028", "temperature":"41" },
{ "humidity":"1.91341660479", "windspeed":"4", "timestamp":"2016-05-12 20:45:56.517239", "temperature":"42" },
{ "humidity":"4.68452768921", "windspeed":"4", "timestamp":"2016-05-12 20:46:01.522506", "temperature":"40" },
{ "humidity":"1.72771718786", "windspeed":"4", "timestamp":"2016-05-12 20:46:06.525431", "temperature":"45" },
{ "humidity":"2.39998595836", "windspeed":"2", "timestamp":"2016-05-12 20:46:11.527912", "temperature":"44" },
{ "humidity":"3.60835014077", "windspeed":"1", "timestamp":"2016-05-12 20:46:16.531888", "temperature":"43" },
{ "humidity":"0.562849340371", "windspeed":"0", "timestamp":"2016-05-12 20:46:21.535817", "temperature":"42" },
{ "humidity":"2.46827123452", "windspeed":"0", "timestamp":"2016-05-12 20:46:26.539643", "temperature":"40" },
{ "humidity":"2.54860527434", "windspeed":"1", "timestamp":"2016-05-12 20:46:31.546459", "temperature":"42" },
{ "humidity":"3.04207980773", "windspeed":"4", "timestamp":"2016-05-12 20:46:36.548618", "temperature":"40" },
{ "humidity":"3.36916164262", "windspeed":"3", "timestamp":"2016-05-12 20:46:41.553464", "temperature":"41" },
{ "humidity":"2.36979313233", "windspeed":"5", "timestamp":"2016-05-12 20:46:46.557808", "temperature":"37" },
{ "humidity":"1.6670123598", "windspeed":"1", "timestamp":"2016-05-12 20:46:51.561428", "temperature":"35" },
{ "humidity":"1.34839759203", "windspeed":"2", "timestamp":"2016-05-12 20:46:56.563920", "temperature":"43" },
{ "humidity":"3.12057510364", "windspeed":"4", "timestamp":"2016-05-12 20:47:01.571128", "temperature":"42" },
{ "humidity":"4.21836283137", "windspeed":"5", "timestamp":"2016-05-12 20:47:06.575230", "temperature":"44" },
{ "humidity":"3.72274520676", "windspeed":"0", "timestamp":"2016-05-12 20:47:11.579429", "temperature":"43" }][{ "humidity":"3.08680013442", "windspeed":"1", "timestamp":"2016-05-12 20:24:57.945850", "temperature":"44" } ,
{ "humidity":"3.72274520676", "windspeed":"0", "timestamp":"2016-05-12 20:47:11.579429", "temperature":"43" },
{ "humidity":"3.02319023327", "windspeed":"3", "timestamp":"2016-05-12 20:47:16.584304", "temperature":"38" },
{ "humidity":"2.77650609407", "windspeed":"3", "timestamp":"2016-05-12 20:47:21.589419", "temperature":"45" },
{ "humidity":"3.26838395612", "windspeed":"5", "timestamp":"2016-05-12 20:47:26.594200", "temperature":"43" },
{ "humidity":"4.76091313601", "windspeed":"1", "timestamp":"2016-05-12 20:47:31.596076", "temperature":"37" },
{ "humidity":"1.73225929964", "windspeed":"1", "timestamp":"2016-05-12 20:47:36.600468", "temperature":"44" },
{ "humidity":"3.94079205343", "windspeed":"5", "timestamp":"2016-05-12 20:47:41.604763", "temperature":"38" },
{ "humidity":"2.52434821417", "windspeed":"5", "timestamp":"2016-05-12 20:47:46.607612", "temperature":"41" },
{ "humidity":"3.82135242777", "windspeed":"3", "timestamp":"2016-05-12 20:47:51.610008", "temperature":"43" },
{ "humidity":"4.32575875888", "windspeed":"2", "timestamp":"2016-05-12 20:47:56.619629", "temperature":"40" },
{ "humidity":"0.533112906343", "windspeed":"4", "timestamp":"2016-05-12 20:48:01.625867", "temperature":"37" },
{ "humidity":"4.96561670916", "windspeed":"1", "timestamp":"2016-05-12 20:48:06.632924", "temperature":"43" },
{ "humidity":"4.63830244507", "windspeed":"5", "timestamp":"2016-05-12 20:48:11.636062", "temperature":"38" },
{ "humidity":"2.46809504376", "windspeed":"4", "timestamp":"2016-05-12 20:48:16.641814", "temperature":"44" },
{ "humidity":"0.591199105592", "windspeed":"0", "timestamp":"2016-05-12 20:48:21.644338", "temperature":"44" },
{ "humidity":"1.7253000723", "windspeed":"3", "timestamp":"2016-05-12 20:48:26.647064", "temperature":"38" },
{ "humidity":"4.70680634754", "windspeed":"5", "timestamp":"2016-05-12 20:48:31.651984", "temperature":"45" },
{ "humidity":"3.54435334892", "windspeed":"3", "timestamp":"2016-05-12 20:48:36.658126", "temperature":"43" },
{ "humidity":"2.16119133523", "windspeed":"1", "timestamp":"2016-05-12 20:48:41.663204", "temperature":"39" },
{ "humidity":"4.51644031029", "windspeed":"4", "timestamp":"2016-05-12 20:48:46.667702", "temperature":"39" },
{ "humidity":"1.46439391432", "windspeed":"0", "timestamp":"2016-05-12 20:48:51.672475", "temperature":"38" },
{ "humidity":"3.26638774363", "windspeed":"2", "timestamp":"2016-05-12 20:48:56.674921", "temperature":"38" },
{ "humidity":"2.46257874099", "windspeed":"4", "timestamp":"2016-05-12 20:49:01.676743", "temperature":"35" },
{ "humidity":"0.225569554846", "windspeed":"0", "timestamp":"2016-05-12 20:49:06.681707", "temperature":"41" },
{ "humidity":"4.80793869528", "windspeed":"3", "timestamp":"2016-05-12 20:49:11.684689", "temperature":"36" },
{ "humidity":"1.57494709607", "windspeed":"3", "timestamp":"2016-05-12 20:49:16.691648", "temperature":"39" },
{ "humidity":"3.93871154127", "windspeed":"2", "timestamp":"2016-05-12 20:49:21.697004", "temperature":"41" },
{ "humidity":"3.2894653428", "windspeed":"5", "timestamp":"2016-05-12 20:49:26.700345", "temperature":"41" },
{ "humidity":"2.86679858917", "windspeed":"5", "timestamp":"2016-05-12 20:49:31.704908", "temperature":"42" },
{ "humidity":"3.64268758735", "windspeed":"0", "timestamp":"2016-05-12 20:49:36.709941", "temperature":"41" },
{ "humidity":"1.72994016429", "windspeed":"5", "timestamp":"2016-05-12 20:49:41.715366", "temperature":"40" },
{ "humidity":"1.28015178591", "windspeed":"0", "timestamp":"2016-05-12 20:49:46.717297", "temperature":"40" },
{ "humidity":"1.15707742126", "windspeed":"2", "timestamp":"2016-05-12 20:49:51.722123", "temperature":"44" },
{ "humidity":"0.0239168842959", "windspeed":"3", "timestamp":"2016-05-12 20:49:56.726136", "temperature":"37" },
{ "humidity":"3.58417577648", "windspeed":"2", "timestamp":"2016-05-12 20:50:01.731838", "temperature":"43" },
{ "humidity":"1.24580053315", "windspeed":"2", "timestamp":"2016-05-12 20:50:06.736400", "temperature":"42" },
{ "humidity":"3.51635165021", "windspeed":"5", "timestamp":"2016-05-12 20:50:11.741476", "temperature":"40" },
{ "humidity":"4.6289513346", "windspeed":"1", "timestamp":"2016-05-12 20:50:16.748557", "temperature":"41" },
{ "humidity":"3.64612926218", "windspeed":"4", "timestamp":"2016-05-12 20:50:21.755368", "temperature":"37" },
{ "humidity":"1.01871328292", "windspeed":"3", "timestamp":"2016-05-12 20:50:26.758542", "temperature":"42" },
{ "humidity":"3.34173838165", "windspeed":"1", "timestamp":"2016-05-12 20:50:31.765414", "temperature":"43" },
{ "humidity":"2.11098005677", "windspeed":"3", "timestamp":"2016-05-12 20:50:36.768268", "temperature":"36" },
{ "humidity":"0.929338001278", "windspeed":"1", "timestamp":"2016-05-12 20:50:41.774703", "temperature":"43" },
{ "humidity":"2.93962446849", "windspeed":"1", "timestamp":"2016-05-12 20:50:46.778746", "temperature":"42" },
{ "humidity":"1.0978611606", "windspeed":"5", "timestamp":"2016-05-12 20:50:51.780754", "temperature":"36" },
{ "humidity":"0.398681960164", "windspeed":"1", "timestamp":"2016-05-12 20:50:56.787628", "temperature":"40" },
{ "humidity":"0.117903888387", "windspeed":"1", "timestamp":"2016-05-12 20:51:01.789752", "temperature":"37" },
{ "humidity":"2.88856087869", "windspeed":"4", "timestamp":"2016-05-12 20:51:06.793855", "temperature":"45" },
{ "humidity":"1.02780376606", "windspeed":"1", "timestamp":"2016-05-12 20:51:11.798589", "temperature":"36" },
{ "humidity":"0.487491977635", "windspeed":"5", "timestamp":"2016-05-12 20:51:16.805880", "temperature":"41" },
{ "humidity":"3.82109871034", "windspeed":"3", "timestamp":"2016-05-12 20:51:21.808928", "temperature":"39" },
{ "humidity":"2.39210358725", "windspeed":"0", "timestamp":"2016-05-12 20:51:26.812959", "temperature":"44" },
{ "humidity":"2.6213002393", "windspeed":"5", "timestamp":"2016-05-12 20:51:31.816142", "temperature":"40" },
{ "humidity":"0.93509027799", "windspeed":"3", "timestamp":"2016-05-12 20:51:36.820912", "temperature":"35" },
{ "humidity":"2.03909669668", "windspeed":"2", "timestamp":"2016-05-12 20:51:41.828111", "temperature":"43" },
{ "humidity":"0.637102344289", "windspeed":"5", "timestamp":"2016-05-12 20:51:46.830876", "temperature":"44" },
{ "humidity":"3.88572352515", "windspeed":"4", "timestamp":"2016-05-12 20:51:51.833580", "temperature":"44" },
{ "humidity":"1.21668922898", "windspeed":"0", "timestamp":"2016-05-12 20:51:56.836776", "temperature":"37" },
{ "humidity":"2.55865518108", "windspeed":"3", "timestamp":"2016-05-12 20:52:01.840610", "temperature":"37" },
{ "humidity":"1.32361087704", "windspeed":"1", "timestamp":"2016-05-12 20:52:06.846734", "temperature":"36" },
{ "humidity":"4.3582278877", "windspeed":"2", "timestamp":"2016-05-12 20:52:11.853301", "temperature":"37" },
{ "humidity":"2.34218792759", "windspeed":"4", "timestamp":"2016-05-12 20:52:16.858420", "temperature":"44" },
{ "humidity":"3.18044649089", "windspeed":"4", "timestamp":"2016-05-12 20:52:21.861074", "temperature":"45" },
{ "humidity":"1.55147582491", "windspeed":"4", "timestamp":"2016-05-12 20:52:26.865589", "temperature":"42" },
{ "humidity":"0.0945272550242", "windspeed":"5", "timestamp":"2016-05-12 20:52:31.872404", "temperature":"41" },
{ "humidity":"2.00847669942", "windspeed":"4", "timestamp":"2016-05-12 20:52:36.875345", "temperature":"41" },
{ "humidity":"2.22816698555", "windspeed":"5", "timestamp":"2016-05-12 20:52:41.879450", "temperature":"35" },
{ "humidity":"4.60779413568", "windspeed":"3", "timestamp":"2016-05-12 20:52:46.883875", "temperature":"42" },
{ "humidity":"3.22257302165", "windspeed":"5", "timestamp":"2016-05-12 20:52:51.887542", "temperature":"42" },
{ "humidity":"4.50568794559", "windspeed":"1", "timestamp":"2016-05-12 20:52:56.894851", "temperature":"41" },
{ "humidity":"1.02485393982", "windspeed":"5", "timestamp":"2016-05-12 20:53:01.897450", "temperature":"39" },
{ "humidity":"3.56489571221", "windspeed":"4", "timestamp":"2016-05-12 20:53:06.903304", "temperature":"45" },
{ "humidity":"1.08089363477", "windspeed":"1", "timestamp":"2016-05-12 20:53:11.909246", "temperature":"39" },
{ "humidity":"1.6764763889", "windspeed":"1", "timestamp":"2016-05-12 20:53:16.911702", "temperature":"35" },
{ "humidity":"0.51353045719", "windspeed":"0", "timestamp":"2016-05-12 20:53:21.917409", "temperature":"45" },
{ "humidity":"3.75903072097", "windspeed":"0", "timestamp":"2016-05-12 20:53:26.919708", "temperature":"44" },
{ "humidity":"2.74325510842", "windspeed":"1", "timestamp":"2016-05-12 20:53:31.925038", "temperature":"42" },
{ "humidity":"1.71804600361", "windspeed":"3", "timestamp":"2016-05-12 20:53:36.926591", "temperature":"38" },
{ "humidity":"0.177818762286", "windspeed":"1", "timestamp":"2016-05-12 20:53:41.933583", "temperature":"45" },
{ "humidity":"1.4396599149", "windspeed":"5", "timestamp":"2016-05-12 20:53:46.940542", "temperature":"45" },
{ "humidity":"3.69463622908", "windspeed":"3", "timestamp":"2016-05-12 20:53:51.944930", "temperature":"36" },
{ "humidity":"2.54270870867", "windspeed":"3", "timestamp":"2016-05-12 20:53:56.952418", "temperature":"40" },
{ "humidity":"0.604562113388", "windspeed":"2", "timestamp":"2016-05-12 20:54:01.955922", "temperature":"42" },
{ "humidity":"3.44206487666", "windspeed":"5", "timestamp":"2016-05-12 20:54:06.961058", "temperature":"45" },
{ "humidity":"4.25358308377", "windspeed":"1", "timestamp":"2016-05-12 20:54:11.967961", "temperature":"41" },
{ "humidity":"1.72793081435", "windspeed":"5", "timestamp":"2016-05-12 20:54:16.970868", "temperature":"42" },
{ "humidity":"2.34222258467", "windspeed":"1", "timestamp":"2016-05-12 20:54:21.973019", "temperature":"41" },
{ "humidity":"3.20544781217", "windspeed":"2", "timestamp":"2016-05-12 20:54:26.979947", "temperature":"41" },
{ "humidity":"3.0222121441", "windspeed":"5", "timestamp":"2016-05-12 20:54:31.988365", "temperature":"35" },
{ "humidity":"3.28588157732", "windspeed":"4", "timestamp":"2016-05-12 20:54:36.993825", "temperature":"35" },
{ "humidity":"4.88831130662", "windspeed":"5", "timestamp":"2016-05-12 20:54:41.998643", "temperature":"39" },
{ "humidity":"4.82935025854", "windspeed":"2", "timestamp":"2016-05-12 20:54:47.003281", "temperature":"35" },
{ "humidity":"1.34814912636", "windspeed":"0", "timestamp":"2016-05-12 20:54:52.007002", "temperature":"35" },
{ "humidity":"3.65791024623", "windspeed":"0", "timestamp":"2016-05-12 20:54:57.012590", "temperature":"44" },
{ "humidity":"3.44428735571", "windspeed":"2", "timestamp":"2016-05-12 20:55:02.017079", "temperature":"40" },
{ "humidity":"1.92583429993", "windspeed":"5", "timestamp":"2016-05-12 20:55:07.019887", "temperature":"38" },
{ "humidity":"1.89331172587", "windspeed":"3", "timestamp":"2016-05-12 20:55:12.023946", "temperature":"44" },
{ "humidity":"1.28804182133", "windspeed":"0", "timestamp":"2016-05-12 20:55:17.029667", "temperature":"37" },
{ "humidity":"2.32102222476", "windspeed":"2", "timestamp":"2016-05-12 20:55:22.031866", "temperature":"40" },
{ "humidity":"4.61916993866", "windspeed":"4", "timestamp":"2016-05-12 20:55:27.035241", "temperature":"45" },
{ "humidity":"0.274147788346", "windspeed":"3", "timestamp":"2016-05-12 20:55:32.041380", "temperature":"35" },
{ "humidity":"0.0315622559093", "windspeed":"0", "timestamp":"2016-05-12 20:55:37.045890", "temperature":"44" },
{ "humidity":"0.247164487958", "windspeed":"4", "timestamp":"2016-05-12 20:55:42.053170", "temperature":"45" },
{ "humidity":"4.17245682543", "windspeed":"0", "timestamp":"2016-05-12 20:55:47.058813", "temperature":"40" },
{ "humidity":"3.19013759792", "windspeed":"2", "timestamp":"2016-05-12 20:55:52.061400", "temperature":"35" },
{ "humidity":"2.44588237096", "windspeed":"3", "timestamp":"2016-05-12 20:55:57.064014", "temperature":"45" },
{ "humidity":"4.51193256399", "windspeed":"0", "timestamp":"2016-05-12 20:56:02.070739", "temperature":"43" },
{ "humidity":"1.58160796397", "windspeed":"0", "timestamp":"2016-05-12 20:56:07.076860", "temperature":"35" },
{ "humidity":"3.4386095399", "windspeed":"1", "timestamp":"2016-05-12 20:56:12.081264", "temperature":"42" },
{ "humidity":"3.73575774401", "windspeed":"0", "timestamp":"2016-05-12 20:56:17.085030", "temperature":"36" },
{ "humidity":"2.21878820603", "windspeed":"0", "timestamp":"2016-05-12 20:56:22.087555", "temperature":"38" },
{ "humidity":"0.382339544559", "windspeed":"2", "timestamp":"2016-05-12 20:56:27.091484", "temperature":"42" },
{ "humidity":"1.87364686095", "windspeed":"3", "timestamp":"2016-05-12 20:56:32.096513", "temperature":"38" },
{ "humidity":"0.140513434439", "windspeed":"2", "timestamp":"2016-05-12 20:56:37.099936", "temperature":"42" },
{ "humidity":"4.95357496141", "windspeed":"1", "timestamp":"2016-05-12 20:56:42.106009", "temperature":"36" },
{ "humidity":"1.1661258902", "windspeed":"0", "timestamp":"2016-05-12 20:56:47.109679", "temperature":"38" },
{ "humidity":"3.56412919334", "windspeed":"1", "timestamp":"2016-05-12 20:56:52.116459", "temperature":"43" },
{ "humidity":"2.12194647681", "windspeed":"0", "timestamp":"2016-05-12 20:56:57.123834", "temperature":"42" },
{ "humidity":"0.994879088223", "windspeed":"3", "timestamp":"2016-05-12 20:57:02.130144", "temperature":"39" },
{ "humidity":"3.27164289595", "windspeed":"1", "timestamp":"2016-05-12 20:57:07.132427", "temperature":"42" },
{ "humidity":"0.325186003611", "windspeed":"3", "timestamp":"2016-05-12 20:57:12.137240", "temperature":"38" },
{ "humidity":"1.28425050381", "windspeed":"4", "timestamp":"2016-05-12 20:57:17.143966", "temperature":"38" },
{ "humidity":"3.43549942644", "windspeed":"4", "timestamp":"2016-05-12 20:57:22.151286", "temperature":"36" },
{ "humidity":"3.17892968015", "windspeed":"1", "timestamp":"2016-05-12 20:57:27.156442", "temperature":"35" },
{ "humidity":"2.3516109723", "windspeed":"1", "timestamp":"2016-05-12 20:57:32.161005", "temperature":"36" },
{ "humidity":"0.439865532961", "windspeed":"1", "timestamp":"2016-05-12 20:57:37.166584", "temperature":"38" },
{ "humidity":"0.403255228163", "windspeed":"1", "timestamp":"2016-05-12 20:57:42.171765", "temperature":"36" },
{ "humidity":"2.85864139816", "windspeed":"1", "timestamp":"2016-05-12 20:57:47.178972", "temperature":"42" },
{ "humidity":"2.59583939415", "windspeed":"4", "timestamp":"2016-05-12 20:57:52.185096", "temperature":"42" },
{ "humidity":"3.12014313439", "windspeed":"1", "timestamp":"2016-05-12 20:57:57.189182", "temperature":"40" },
{ "humidity":"2.13480284114", "windspeed":"4", "timestamp":"2016-05-12 20:58:02.193199", "temperature":"35" },
{ "humidity":"3.02138605816", "windspeed":"3", "timestamp":"2016-05-12 20:58:07.198766", "temperature":"37" },
{ "humidity":"3.50958058413", "windspeed":"2", "timestamp":"2016-05-12 20:58:12.205011", "temperature":"38" },
{ "humidity":"2.57698767596", "windspeed":"4", "timestamp":"2016-05-12 20:58:17.210068", "temperature":"40" },
{ "humidity":"4.24183789873", "windspeed":"1", "timestamp":"2016-05-12 20:58:22.212755", "temperature":"40" },
{ "humidity":"2.5047966667", "windspeed":"3", "timestamp":"2016-05-12 20:58:27.215154", "temperature":"39" },
{ "humidity":"1.40945393561", "windspeed":"5", "timestamp":"2016-05-12 20:58:32.220195", "temperature":"35" },
{ "humidity":"1.03616025599", "windspeed":"4", "timestamp":"2016-05-12 20:58:37.225511", "temperature":"35" },
{ "humidity":"0.765994198425", "windspeed":"2", "timestamp":"2016-05-12 20:58:42.229258", "temperature":"39" },
{ "humidity":"1.08986241761", "windspeed":"0", "timestamp":"2016-05-12 20:58:47.232528", "temperature":"35" },
{ "humidity":"3.47262505465", "windspeed":"2", "timestamp":"2016-05-12 20:58:52.237292", "temperature":"36" },
{ "humidity":"4.26249274959", "windspeed":"2", "timestamp":"2016-05-12 20:58:57.241336", "temperature":"37" },
{ "humidity":"4.60845627334", "windspeed":"4", "timestamp":"2016-05-12 20:59:02.245497", "temperature":"35" },
{ "humidity":"4.89320848046", "windspeed":"4", "timestamp":"2016-05-12 20:59:07.248140", "temperature":"42" },
{ "humidity":"1.83431508232", "windspeed":"2", "timestamp":"2016-05-12 20:59:12.254090", "temperature":"35" },
{ "humidity":"1.33657055784", "windspeed":"1", "timestamp":"2016-05-12 20:59:17.257602", "temperature":"37" },
{ "humidity":"0.281683404689", "windspeed":"5", "timestamp":"2016-05-12 20:59:22.264288", "temperature":"38" },
{ "humidity":"3.7490825523", "windspeed":"5", "timestamp":"2016-05-12 20:59:27.268451", "temperature":"39" },
{ "humidity":"3.78433266965", "windspeed":"3", "timestamp":"2016-05-12 20:59:32.270061", "temperature":"38" },
{ "humidity":"0.245424046045", "windspeed":"0", "timestamp":"2016-05-12 20:59:37.274194", "temperature":"41" },
{ "humidity":"1.78848035529", "windspeed":"5", "timestamp":"2016-05-12 20:59:42.279657", "temperature":"36" },
{ "humidity":"1.24454093714", "windspeed":"5", "timestamp":"2016-05-12 20:59:47.283864", "temperature":"37" },
{ "humidity":"2.59993802126", "windspeed":"2", "timestamp":"2016-05-12 20:59:52.286520", "temperature":"35" },
{ "humidity":"3.70750867404", "windspeed":"5", "timestamp":"2016-05-12 20:59:57.289369", "temperature":"44" },
{ "humidity":"2.7481334462", "windspeed":"0", "timestamp":"2016-05-12 21:00:02.292007", "temperature":"39" },
{ "humidity":"2.61085665851", "windspeed":"1", "timestamp":"2016-05-12 21:00:07.297047", "temperature":"45" },
{ "humidity":"3.05282956315", "windspeed":"1", "timestamp":"2016-05-12 21:00:12.302276", "temperature":"43" },
{ "humidity":"4.68641919506", "windspeed":"2", "timestamp":"2016-05-12 21:00:17.310085", "temperature":"43" },
{ "humidity":"1.78177516737", "windspeed":"5", "timestamp":"2016-05-12 21:00:22.316122", "temperature":"42" },
{ "humidity":"4.7297535027", "windspeed":"0", "timestamp":"2016-05-12 21:00:27.321280", "temperature":"43" },
{ "humidity":"4.92618396796", "windspeed":"0", "timestamp":"2016-05-12 21:00:32.326099", "temperature":"41" },
{ "humidity":"0.601099038947", "windspeed":"3", "timestamp":"2016-05-12 21:00:37.332022", "temperature":"45" },
{ "humidity":"1.61432831457", "windspeed":"4", "timestamp":"2016-05-12 21:00:42.336940", "temperature":"42" },
{ "humidity":"1.50010128216", "windspeed":"2", "timestamp":"2016-05-12 21:00:47.339522", "temperature":"35" },
{ "humidity":"1.6956194855", "windspeed":"5", "timestamp":"2016-05-12 21:00:52.342477", "temperature":"36" },
{ "humidity":"4.84734309333", "windspeed":"3", "timestamp":"2016-05-12 21:00:57.348051", "temperature":"38" },
{ "humidity":"2.76784200971", "windspeed":"2", "timestamp":"2016-05-12 21:01:02.350613", "temperature":"43" },
{ "humidity":"2.00423507361", "windspeed":"3", "timestamp":"2016-05-12 21:01:07.357508", "temperature":"38" },
{ "humidity":"3.34887834268", "windspeed":"3", "timestamp":"2016-05-12 21:01:12.361666", "temperature":"38" },
{ "humidity":"2.50824155828", "windspeed":"3", "timestamp":"2016-05-12 21:01:17.364822", "temperature":"35" },
{ "humidity":"4.08380011368", "windspeed":"0", "timestamp":"2016-05-12 21:01:22.367499", "temperature":"39" },
{ "humidity":"4.74594020758", "windspeed":"4", "timestamp":"2016-05-12 21:01:27.370051", "temperature":"40" },
{ "humidity":"2.50693246059", "windspeed":"1", "timestamp":"2016-05-12 21:01:32.377656", "temperature":"35" },
{ "humidity":"3.49555942379", "windspeed":"0", "timestamp":"2016-05-12 21:01:37.383957", "temperature":"41" },
{ "humidity":"4.41071091005", "windspeed":"3", "timestamp":"2016-05-12 21:01:42.389248", "temperature":"44" },
{ "humidity":"2.2980470415", "windspeed":"0", "timestamp":"2016-05-12 21:01:47.394225", "temperature":"44" },
{ "humidity":"0.629162473847", "windspeed":"1", "timestamp":"2016-05-12 21:01:52.405037", "temperature":"35" },
{ "humidity":"3.38680905095", "windspeed":"1", "timestamp":"2016-05-12 21:01:57.410769", "temperature":"41" },
{ "humidity":"3.22636801753", "windspeed":"4", "timestamp":"2016-05-12 21:02:02.414884", "temperature":"39" },
{ "humidity":"1.36562583245", "windspeed":"1", "timestamp":"2016-05-12 21:02:07.416462", "temperature":"45" },
{ "humidity":"4.23595417871", "windspeed":"1", "timestamp":"2016-05-12 21:02:12.420306", "temperature":"43" },
{ "humidity":"0.10400771066", "windspeed":"3", "timestamp":"2016-05-12 21:02:17.422340", "temperature":"43" },
{ "humidity":"4.26071366057", "windspeed":"2", "timestamp":"2016-05-12 21:02:22.429222", "temperature":"39" },
{ "humidity":"1.62325609702", "windspeed":"3", "timestamp":"2016-05-12 21:02:27.432631", "temperature":"44" },
{ "humidity":"3.81191878761", "windspeed":"1", "timestamp":"2016-05-12 21:02:32.434554", "temperature":"40" },
{ "humidity":"1.24060324773", "windspeed":"1", "timestamp":"2016-05-12 21:02:37.440973", "temperature":"37" },
{ "humidity":"3.48627275717", "windspeed":"5", "timestamp":"2016-05-12 21:02:42.443876", "temperature":"36" },
{ "humidity":"0.852657508872", "windspeed":"3", "timestamp":"2016-05-12 21:02:47.448833", "temperature":"44" },
{ "humidity":"2.7508590865", "windspeed":"1", "timestamp":"2016-05-12 21:02:52.453348", "temperature":"40" },
{ "humidity":"2.46277701598", "windspeed":"4", "timestamp":"2016-05-12 21:02:57.459419", "temperature":"37" },
{ "humidity":"4.65559856932", "windspeed":"4", "timestamp":"2016-05-12 21:03:02.462523", "temperature":"44" },
{ "humidity":"3.43899345087", "windspeed":"4", "timestamp":"2016-05-12 21:03:07.468810", "temperature":"42" },
{ "humidity":"2.16830128747", "windspeed":"5", "timestamp":"2016-05-12 21:03:12.471912", "temperature":"41" },
{ "humidity":"4.83831389943", "windspeed":"3", "timestamp":"2016-05-12 21:03:17.477546", "temperature":"41" },
{ "humidity":"0.970786997557", "windspeed":"4", "timestamp":"2016-05-12 21:03:22.481463", "temperature":"40" },
{ "humidity":"1.97379461178", "windspeed":"3", "timestamp":"2016-05-12 21:03:27.487145", "temperature":"38" },
{ "humidity":"4.75555664676", "windspeed":"5", "timestamp":"2016-05-12 21:03:32.491912", "temperature":"43" },
{ "humidity":"0.933053519866", "windspeed":"3", "timestamp":"2016-05-12 21:03:37.496731", "temperature":"43" },
{ "humidity":"0.663806035982", "windspeed":"2", "timestamp":"2016-05-12 21:03:42.503160", "temperature":"43" },
{ "humidity":"2.28637675144", "windspeed":"5", "timestamp":"2016-05-12 21:03:47.509234", "temperature":"42" },
{ "humidity":"2.65169254486", "windspeed":"0", "timestamp":"2016-05-12 21:03:52.515027", "temperature":"42" },
{ "humidity":"0.572581106027", "windspeed":"1", "timestamp":"2016-05-12 21:03:57.520955", "temperature":"39" },
{ "humidity":"4.83874612639", "windspeed":"2", "timestamp":"2016-05-12 21:04:02.526616", "temperature":"35" },
{ "humidity":"0.551108058515", "windspeed":"5", "timestamp":"2016-05-12 21:04:07.530435", "temperature":"45" },
{ "humidity":"0.457316340565", "windspeed":"4", "timestamp":"2016-05-12 21:04:12.533512", "temperature":"42" },
{ "humidity":"0.0437905405039", "windspeed":"4", "timestamp":"2016-05-12 21:04:17.538353", "temperature":"37" },
{ "humidity":"2.10483312332", "windspeed":"2", "timestamp":"2016-05-12 21:04:22.544517", "temperature":"36" },
{ "humidity":"4.53085557844", "windspeed":"1", "timestamp":"2016-05-12 21:04:27.548170", "temperature":"37" },
{ "humidity":"0.507888286895", "windspeed":"2", "timestamp":"2016-05-12 21:04:32.552670", "temperature":"36" },
{ "humidity":"2.17278244824", "windspeed":"2", "timestamp":"2016-05-12 21:04:37.557216", "temperature":"41" },
{ "humidity":"2.16634116158", "windspeed":"5", "timestamp":"2016-05-12 21:04:42.561647", "temperature":"38" },
{ "humidity":"1.07387323214", "windspeed":"5", "timestamp":"2016-05-12 21:04:47.567037", "temperature":"43" },
{ "humidity":"1.66463725563", "windspeed":"0", "timestamp":"2016-05-12 21:04:52.571692", "temperature":"41" },
{ "humidity":"3.98649140867", "windspeed":"0", "timestamp":"2016-05-12 21:04:57.575557", "temperature":"44" },
{ "humidity":"3.84389053305", "windspeed":"4", "timestamp":"2016-05-12 21:05:02.581272", "temperature":"45" },
{ "humidity":"3.30366396295", "windspeed":"5", "timestamp":"2016-05-12 21:05:07.586213", "temperature":"41" },
{ "humidity":"2.27784813639", "windspeed":"5", "timestamp":"2016-05-12 21:05:12.590898", "temperature":"37" },
{ "humidity":"3.72714631486", "windspeed":"4", "timestamp":"2016-05-12 21:05:17.595221", "temperature":"44" },
{ "humidity":"0.419356258507", "windspeed":"2", "timestamp":"2016-05-12 21:05:22.600074", "temperature":"38" },
{ "humidity":"2.58908508451", "windspeed":"0", "timestamp":"2016-05-12 21:05:27.605945", "temperature":"41" },
{ "humidity":"4.38923860166", "windspeed":"4", "timestamp":"2016-05-12 21:05:32.611752", "temperature":"39" },
{ "humidity":"4.53921446634", "windspeed":"1", "timestamp":"2016-05-12 21:05:37.617174", "temperature":"36" },
{ "humidity":"3.65724341015", "windspeed":"5", "timestamp":"2016-05-12 21:05:42.619622", "temperature":"36" },
{ "humidity":"4.91958325239", "windspeed":"3", "timestamp":"2016-05-12 21:05:47.624852", "temperature":"35" },
{ "humidity":"2.75248933037", "windspeed":"5", "timestamp":"2016-05-12 21:05:52.629233", "temperature":"37" },
{ "humidity":"3.1128862379", "windspeed":"4", "timestamp":"2016-05-12 21:05:57.633913", "temperature":"35" },
{ "humidity":"4.95494651511", "windspeed":"3", "timestamp":"2016-05-12 21:06:02.638385", "temperature":"44" },
{ "humidity":"1.76465858683", "windspeed":"1", "timestamp":"2016-05-12 21:06:07.644941", "temperature":"39" },
{ "humidity":"0.0112975846963", "windspeed":"5", "timestamp":"2016-05-12 21:06:12.647530", "temperature":"43" },
{ "humidity":"0.804842508395", "windspeed":"5", "timestamp":"2016-05-12 21:06:17.652302", "temperature":"36" },
{ "humidity":"0.608314849373", "windspeed":"4", "timestamp":"2016-05-12 21:06:22.656934", "temperature":"43" },
{ "humidity":"1.58603372089", "windspeed":"3", "timestamp":"2016-05-12 21:06:27.663985", "temperature":"37" },
{ "humidity":"4.15218990496", "windspeed":"5", "timestamp":"2016-05-12 21:06:32.670978", "temperature":"37" },
{ "humidity":"1.62875104426", "windspeed":"0", "timestamp":"2016-05-12 21:06:37.672564", "temperature":"35" },
{ "humidity":"2.8631770921", "windspeed":"4", "timestamp":"2016-05-12 21:06:42.676768", "temperature":"35" },
{ "humidity":"3.6693633769", "windspeed":"3", "timestamp":"2016-05-12 21:06:47.681801", "temperature":"39" },
{ "humidity":"4.34529793241", "windspeed":"5", "timestamp":"2016-05-12 21:06:52.686158", "temperature":"37" },
{ "humidity":"4.98148118306", "windspeed":"2", "timestamp":"2016-05-12 21:06:57.691457", "temperature":"38" },
{ "humidity":"4.99588903719", "windspeed":"1", "timestamp":"2016-05-12 21:07:02.696288", "temperature":"42" },
{ "humidity":"3.20165332269", "windspeed":"5", "timestamp":"2016-05-12 21:07:07.700965", "temperature":"41" },
{ "humidity":"0.958723422186", "windspeed":"1", "timestamp":"2016-05-12 21:07:12.705785", "temperature":"41" },
{ "humidity":"2.89676981304", "windspeed":"1", "timestamp":"2016-05-12 21:07:17.709626", "temperature":"45" },
{ "humidity":"1.02671983023", "windspeed":"5", "timestamp":"2016-05-12 21:07:22.715303", "temperature":"36" },
{ "humidity":"3.41249305536", "windspeed":"3", "timestamp":"2016-05-12 21:07:27.721185", "temperature":"38" },
{ "humidity":"2.18837471988", "windspeed":"4", "timestamp":"2016-05-12 21:07:32.725485", "temperature":"35" },
{ "humidity":"1.33637038713", "windspeed":"1", "timestamp":"2016-05-12 21:07:37.728832", "temperature":"35" },
{ "humidity":"0.600361231019", "windspeed":"2", "timestamp":"2016-05-12 21:07:42.734421", "temperature":"43" },
{ "humidity":"2.10644049547", "windspeed":"1", "timestamp":"2016-05-12 21:07:47.739170", "temperature":"38" },
{ "humidity":"2.00778055841", "windspeed":"2", "timestamp":"2016-05-12 21:07:52.743709", "temperature":"38" },
{ "humidity":"3.30270070463", "windspeed":"5", "timestamp":"2016-05-12 21:07:57.748125", "temperature":"38" },
{ "humidity":"3.89704867189", "windspeed":"2", "timestamp":"2016-05-12 21:08:02.753565", "temperature":"38" },
{ "humidity":"2.42712862463", "windspeed":"5", "timestamp":"2016-05-12 21:08:07.758191", "temperature":"43" },
{ "humidity":"3.51978590576", "windspeed":"4", "timestamp":"2016-05-12 21:08:12.762186", "temperature":"45" },
{ "humidity":"3.51001016512", "windspeed":"0", "timestamp":"2016-05-12 21:08:17.767869", "temperature":"39" },
{ "humidity":"1.76990471792", "windspeed":"3", "timestamp":"2016-05-12 21:08:22.772588", "temperature":"38" },
{ "humidity":"2.13286077655", "windspeed":"2", "timestamp":"2016-05-12 21:08:27.778792", "temperature":"36" },
{ "humidity":"3.03872841279", "windspeed":"1", "timestamp":"2016-05-12 21:08:32.785059", "temperature":"36" },
{ "humidity":"1.50616974433", "windspeed":"0", "timestamp":"2016-05-12 21:08:37.790790", "temperature":"36" },
{ "humidity":"2.16559975277", "windspeed":"5", "timestamp":"2016-05-12 21:08:42.797597", "temperature":"37" },
{ "humidity":"3.00495526251", "windspeed":"4", "timestamp":"2016-05-12 21:08:47.803046", "temperature":"37" },
{ "humidity":"2.93897729678", "windspeed":"4", "timestamp":"2016-05-12 21:08:52.804693", "temperature":"42" },
{ "humidity":"1.13434243707", "windspeed":"2", "timestamp":"2016-05-12 21:08:57.808441", "temperature":"42" },
{ "humidity":"3.77441091094", "windspeed":"5", "timestamp":"2016-05-12 21:09:02.813152", "temperature":"40" },
{ "humidity":"3.41090390155", "windspeed":"1", "timestamp":"2016-05-12 21:09:07.819341", "temperature":"44" },
{ "humidity":"2.29564858251", "windspeed":"2", "timestamp":"2016-05-12 21:09:12.823277", "temperature":"43" },
{ "humidity":"4.19926788078", "windspeed":"0", "timestamp":"2016-05-12 21:09:17.824818", "temperature":"36" },
{ "humidity":"2.66495901525", "windspeed":"0", "timestamp":"2016-05-12 21:09:22.829985", "temperature":"39" },
{ "humidity":"1.43237789305", "windspeed":"4", "timestamp":"2016-05-12 21:09:27.834357", "temperature":"38" },
{ "humidity":"3.8402786469", "windspeed":"2", "timestamp":"2016-05-12 21:09:32.839508", "temperature":"45" },
{ "humidity":"3.28295454252", "windspeed":"4", "timestamp":"2016-05-12 21:09:37.844731", "temperature":"43" },
{ "humidity":"1.98567494641", "windspeed":"3", "timestamp":"2016-05-12 21:09:42.849123", "temperature":"42" },
{ "humidity":"3.0815647543", "windspeed":"2", "timestamp":"2016-05-12 21:09:47.853047", "temperature":"44" },
{ "humidity":"1.57115544834", "windspeed":"0", "timestamp":"2016-05-12 21:09:52.858744", "temperature":"36" },
{ "humidity":"1.61811320319", "windspeed":"0", "timestamp":"2016-05-12 21:09:57.863549", "temperature":"35" },
{ "humidity":"1.86989289277", "windspeed":"3", "timestamp":"2016-05-12 21:10:02.868324", "temperature":"42" },
{ "humidity":"2.11317476519", "windspeed":"5", "timestamp":"2016-05-12 21:10:07.872450", "temperature":"38" },
{ "humidity":"1.94729544872", "windspeed":"3", "timestamp":"2016-05-12 21:10:12.879001", "temperature":"45" },
{ "humidity":"1.86596141247", "windspeed":"2", "timestamp":"2016-05-12 21:10:17.881827", "temperature":"35" },
{ "humidity":"1.2485637194", "windspeed":"3", "timestamp":"2016-05-12 21:10:22.887497", "temperature":"36" },
{ "humidity":"0.18049980675", "windspeed":"3", "timestamp":"2016-05-12 21:10:27.892212", "temperature":"44" },
{ "humidity":"0.770752387533", "windspeed":"3", "timestamp":"2016-05-12 21:10:32.896961", "temperature":"44" },
{ "humidity":"2.86575488022", "windspeed":"5", "timestamp":"2016-05-12 21:10:37.900783", "temperature":"39" },
{ "humidity":"2.62888369297", "windspeed":"4", "timestamp":"2016-05-12 21:10:42.902191", "temperature":"38" },
{ "humidity":"1.36942461963", "windspeed":"5", "timestamp":"2016-05-12 21:10:47.908839", "temperature":"40" },
{ "humidity":"0.934127495017", "windspeed":"0", "timestamp":"2016-05-12 21:10:52.913837", "temperature":"40" },
{ "humidity":"0.254676467812", "windspeed":"5", "timestamp":"2016-05-12 21:10:57.917954", "temperature":"39" },
{ "humidity":"0.125436346623", "windspeed":"1", "timestamp":"2016-05-12 21:11:02.919812", "temperature":"41" },
{ "humidity":"2.26938835682", "windspeed":"4", "timestamp":"2016-05-12 21:11:07.925944", "temperature":"35" },
{ "humidity":"4.10757444837", "windspeed":"2", "timestamp":"2016-05-12 21:11:12.931876", "temperature":"40" },
{ "humidity":"4.08994787595", "windspeed":"2", "timestamp":"2016-05-12 21:11:17.936813", "temperature":"43" },
{ "humidity":"3.98675643531", "windspeed":"5", "timestamp":"2016-05-12 21:11:22.942032", "temperature":"45" },
{ "humidity":"1.53187912308", "windspeed":"0", "timestamp":"2016-05-12 21:11:27.944710", "temperature":"40" },
{ "humidity":"1.28459987799", "windspeed":"3", "timestamp":"2016-05-12 21:11:32.950936", "temperature":"43" },
{ "humidity":"1.3647019126", "windspeed":"1", "timestamp":"2016-05-12 21:11:37.956456", "temperature":"43" },
{ "humidity":"3.08832202756", "windspeed":"4", "timestamp":"2016-05-12 21:11:42.963193", "temperature":"39" },
{ "humidity":"4.01141564958", "windspeed":"4", "timestamp":"2016-05-12 21:11:47.969039", "temperature":"38" },
{ "humidity":"1.68285067304", "windspeed":"2", "timestamp":"2016-05-12 21:11:52.973473", "temperature":"40" },
{ "humidity":"1.8638471768", "windspeed":"0", "timestamp":"2016-05-12 21:11:57.978245", "temperature":"43" },
{ "humidity":"2.62331246228", "windspeed":"0", "timestamp":"2016-05-12 21:12:02.983038", "temperature":"43" },
{ "humidity":"2.73701580529", "windspeed":"1", "timestamp":"2016-05-12 21:12:07.987485", "temperature":"38" },
{ "humidity":"0.236843270788", "windspeed":"0", "timestamp":"2016-05-12 21:12:12.992708", "temperature":"45" },
{ "humidity":"0.455768148827", "windspeed":"4", "timestamp":"2016-05-12 21:12:17.999443", "temperature":"45" },
{ "humidity":"0.390402356965", "windspeed":"3", "timestamp":"2016-05-12 21:12:23.002163", "temperature":"45" },
{ "humidity":"3.49607409074", "windspeed":"5", "timestamp":"2016-05-12 21:12:28.006902", "temperature":"45" },
{ "humidity":"3.24908985168", "windspeed":"0", "timestamp":"2016-05-12 21:12:33.010034", "temperature":"37" },
{ "humidity":"0.923527607299", "windspeed":"4", "timestamp":"2016-05-12 21:12:38.016625", "temperature":"37" },
{ "humidity":"1.9860161128", "windspeed":"4", "timestamp":"2016-05-12 21:12:43.022517", "temperature":"41" },
{ "humidity":"4.37471470876", "windspeed":"3", "timestamp":"2016-05-12 21:12:48.027578", "temperature":"38" },
{ "humidity":"2.18987094097", "windspeed":"3", "timestamp":"2016-05-12 21:12:53.030962", "temperature":"44" },
{ "humidity":"0.294514035324", "windspeed":"2", "timestamp":"2016-05-12 21:12:58.035672", "temperature":"35" },
{ "humidity":"0.154002790339", "windspeed":"1", "timestamp":"2016-05-12 21:13:03.040533", "temperature":"39" },
{ "humidity":"3.07668487935", "windspeed":"4", "timestamp":"2016-05-12 21:13:08.045404", "temperature":"40" },
{ "humidity":"0.704889079306", "windspeed":"3", "timestamp":"2016-05-12 21:13:13.050073", "temperature":"35" },
{ "humidity":"2.32255584025", "windspeed":"0", "timestamp":"2016-05-12 21:13:18.053810", "temperature":"40" },
{ "humidity":"3.64635441719", "windspeed":"0", "timestamp":"2016-05-12 21:13:23.060219", "temperature":"44" },
{ "humidity":"4.12453919244", "windspeed":"5", "timestamp":"2016-05-12 21:13:28.064459", "temperature":"37" },
{ "humidity":"2.97192192973", "windspeed":"4", "timestamp":"2016-05-12 21:13:33.069197", "temperature":"36" },
{ "humidity":"0.0127897376584", "windspeed":"0", "timestamp":"2016-05-12 21:13:38.074129", "temperature":"42" },
{ "humidity":"3.62418314785", "windspeed":"1", "timestamp":"2016-05-12 21:13:43.078513", "temperature":"38" },
{ "humidity":"2.21581753725", "windspeed":"4", "timestamp":"2016-05-12 21:13:48.083346", "temperature":"35" },
{ "humidity":"1.86021649227", "windspeed":"2", "timestamp":"2016-05-12 21:13:53.088309", "temperature":"36" },
{ "humidity":"2.90012522917", "windspeed":"3", "timestamp":"2016-05-12 21:13:58.092453", "temperature":"45" },
{ "humidity":"3.76550862596", "windspeed":"5", "timestamp":"2016-05-12 21:14:03.098368", "temperature":"45" },
{ "humidity":"0.868033804283", "windspeed":"5", "timestamp":"2016-05-12 21:14:08.102688", "temperature":"43" },
{ "humidity":"1.51142590745", "windspeed":"2", "timestamp":"2016-05-12 21:14:13.107535", "temperature":"36" },
{ "humidity":"0.506498957601", "windspeed":"0", "timestamp":"2016-05-12 21:14:18.112270", "temperature":"45" },
{ "humidity":"2.28877091927", "windspeed":"3", "timestamp":"2016-05-12 21:14:23.116070", "temperature":"41" },
{ "humidity":"1.55978713449", "windspeed":"1", "timestamp":"2016-05-12 21:14:28.121093", "temperature":"35" },
{ "humidity":"2.31221456237", "windspeed":"4", "timestamp":"2016-05-12 21:14:33.128490", "temperature":"45" },
{ "humidity":"1.01532052169", "windspeed":"4", "timestamp":"2016-05-12 21:14:38.131327", "temperature":"43" },
{ "humidity":"4.92777966529", "windspeed":"5", "timestamp":"2016-05-12 21:14:43.136162", "temperature":"41" },
{ "humidity":"0.23513086562", "windspeed":"5", "timestamp":"2016-05-12 21:14:48.140961", "temperature":"45" },
{ "humidity":"3.78086464476", "windspeed":"5", "timestamp":"2016-05-12 21:14:53.144788", "temperature":"43" },
{ "humidity":"3.37460262599", "windspeed":"2", "timestamp":"2016-05-12 21:14:58.151868", "temperature":"35" },
{ "humidity":"0.0489353102649", "windspeed":"1", "timestamp":"2016-05-12 21:15:03.157036", "temperature":"45" },
{ "humidity":"0.307322659591", "windspeed":"0", "timestamp":"2016-05-12 21:15:08.161543", "temperature":"40" },
{ "humidity":"1.69139243072", "windspeed":"0", "timestamp":"2016-05-12 21:15:13.164422", "temperature":"44" },
{ "humidity":"2.85090726939", "windspeed":"1", "timestamp":"2016-05-12 21:15:18.169843", "temperature":"42" },
{ "humidity":"3.89210094642", "windspeed":"3", "timestamp":"2016-05-12 21:15:23.174492", "temperature":"45" },
{ "humidity":"2.99561662422", "windspeed":"1", "timestamp":"2016-05-12 21:15:28.180962", "temperature":"43" },
{ "humidity":"2.61161790524", "windspeed":"4", "timestamp":"2016-05-12 21:15:33.188439", "temperature":"40" },
{ "humidity":"3.59047573794", "windspeed":"5", "timestamp":"2016-05-12 21:15:38.195130", "temperature":"44" },
{ "humidity":"2.53369017913", "windspeed":"1", "timestamp":"2016-05-12 21:15:43.202736", "temperature":"39" },
{ "humidity":"2.84605978934", "windspeed":"4", "timestamp":"2016-05-12 21:15:48.206560", "temperature":"40" },
{ "humidity":"1.15403703745", "windspeed":"5", "timestamp":"2016-05-12 21:15:53.210913", "temperature":"43" },
{ "humidity":"0.71812402998", "windspeed":"3", "timestamp":"2016-05-12 21:15:58.213665", "temperature":"37" },
{ "humidity":"4.95696029792", "windspeed":"4", "timestamp":"2016-05-12 21:16:03.216611", "temperature":"36" },
{ "humidity":"1.14189807926", "windspeed":"4", "timestamp":"2016-05-12 21:16:08.220687", "temperature":"38" },
{ "humidity":"0.364177452358", "windspeed":"0", "timestamp":"2016-05-12 21:16:13.225248", "temperature":"40" },
{ "humidity":"4.91553134931", "windspeed":"4", "timestamp":"2016-05-12 21:16:18.231970", "temperature":"44" },
{ "humidity":"3.80589697613", "windspeed":"4", "timestamp":"2016-05-12 21:16:23.236666", "temperature":"40" },
{ "humidity":"3.69978917045", "windspeed":"5", "timestamp":"2016-05-12 21:16:28.240316", "temperature":"44" },
{ "humidity":"2.27621637972", "windspeed":"5", "timestamp":"2016-05-12 21:16:33.243544", "temperature":"37" },
{ "humidity":"3.42379271432", "windspeed":"4", "timestamp":"2016-05-12 21:16:38.246136", "temperature":"45" },
{ "humidity":"3.3113673724", "windspeed":"2", "timestamp":"2016-05-12 21:16:43.253029", "temperature":"37" },
{ "humidity":"4.65970015083", "windspeed":"3", "timestamp":"2016-05-12 21:16:48.258822", "temperature":"38" },
{ "humidity":"3.16599043154", "windspeed":"3", "timestamp":"2016-05-12 21:16:53.264418", "temperature":"44" },
{ "humidity":"0.74744017953", "windspeed":"2", "timestamp":"2016-05-12 21:16:58.270414", "temperature":"35" },
{ "humidity":"0.185719206535", "windspeed":"5", "timestamp":"2016-05-12 21:17:03.273528", "temperature":"36" },
{ "humidity":"1.96215190009", "windspeed":"2", "timestamp":"2016-05-12 21:17:08.276664", "temperature":"43" },
{ "humidity":"2.47740824464", "windspeed":"5", "timestamp":"2016-05-12 21:17:13.283561", "temperature":"45" },
{ "humidity":"3.11602426464", "windspeed":"1", "timestamp":"2016-05-12 21:17:18.285707", "temperature":"39" },
{ "humidity":"3.58245885537", "windspeed":"3", "timestamp":"2016-05-12 21:17:23.292236", "temperature":"45" },
{ "humidity":"3.34740128805", "windspeed":"5", "timestamp":"2016-05-12 21:17:28.297291", "temperature":"40" },
{ "humidity":"4.19785530849", "windspeed":"1", "timestamp":"2016-05-12 21:17:33.301179", "temperature":"36" },
{ "humidity":"4.69769942065", "windspeed":"5", "timestamp":"2016-05-12 21:17:38.306249", "temperature":"37" },
{ "humidity":"1.30717421198", "windspeed":"4", "timestamp":"2016-05-12 21:17:43.310590", "temperature":"39" },
{ "humidity":"4.32020278921", "windspeed":"0", "timestamp":"2016-05-12 21:17:48.312638", "temperature":"36" },
{ "humidity":"0.207901915457", "windspeed":"1", "timestamp":"2016-05-12 21:17:53.316785", "temperature":"42" },
{ "humidity":"0.185416929288", "windspeed":"5", "timestamp":"2016-05-12 21:17:58.322245", "temperature":"43" },
{ "humidity":"1.85510131981", "windspeed":"4", "timestamp":"2016-05-12 21:18:03.327382", "temperature":"45" },
{ "humidity":"0.835193826015", "windspeed":"0", "timestamp":"2016-05-12 21:18:08.333112", "temperature":"36" },
{ "humidity":"1.32361878812", "windspeed":"2", "timestamp":"2016-05-12 21:18:13.337263", "temperature":"40" },
{ "humidity":"1.37960806486", "windspeed":"4", "timestamp":"2016-05-12 21:18:18.343797", "temperature":"38" },
{ "humidity":"0.0503375177458", "windspeed":"0", "timestamp":"2016-05-12 21:18:23.346619", "temperature":"45" },
{ "humidity":"0.973853484455", "windspeed":"0", "timestamp":"2016-05-12 21:18:28.350844", "temperature":"36" },
{ "humidity":"2.61239137172", "windspeed":"1", "timestamp":"2016-05-12 21:18:33.355835", "temperature":"40" },
{ "humidity":"4.82423165145", "windspeed":"5", "timestamp":"2016-05-12 21:18:38.360035", "temperature":"41" },
{ "humidity":"2.40599829943", "windspeed":"2", "timestamp":"2016-05-12 21:18:43.365650", "temperature":"41" },
{ "humidity":"2.40906420685", "windspeed":"5", "timestamp":"2016-05-12 21:18:48.370361", "temperature":"37" },
{ "humidity":"2.66712454171", "windspeed":"2", "timestamp":"2016-05-12 21:18:53.375548", "temperature":"43" },
{ "humidity":"0.479553477128", "windspeed":"3", "timestamp":"2016-05-12 21:18:58.381473", "temperature":"37" },
{ "humidity":"0.290568534096", "windspeed":"3", "timestamp":"2016-05-12 21:19:03.384835", "temperature":"43" },
{ "humidity":"1.78370174451", "windspeed":"0", "timestamp":"2016-05-12 21:19:08.390980", "temperature":"45" },
{ "humidity":"0.560900683584", "windspeed":"1", "timestamp":"2016-05-12 21:19:13.393826", "temperature":"43" },
{ "humidity":"2.5691285385", "windspeed":"4", "timestamp":"2016-05-12 21:19:18.399195", "temperature":"43" },
{ "humidity":"1.23464928796", "windspeed":"0", "timestamp":"2016-05-12 21:19:23.403935", "temperature":"45" },
{ "humidity":"1.49665299192", "windspeed":"3", "timestamp":"2016-05-12 21:19:28.408475", "temperature":"39" },
{ "humidity":"3.61496389873", "windspeed":"4", "timestamp":"2016-05-12 21:19:33.415212", "temperature":"40" },
{ "humidity":"3.12526568975", "windspeed":"4", "timestamp":"2016-05-12 21:19:38.418290", "temperature":"37" },
{ "humidity":"1.67375947872", "windspeed":"0", "timestamp":"2016-05-12 21:19:43.422196", "temperature":"37" },
{ "humidity":"3.00599726762", "windspeed":"1", "timestamp":"2016-05-12 21:19:48.427788", "temperature":"41" },
{ "humidity":"3.52037114318", "windspeed":"3", "timestamp":"2016-05-12 21:19:53.432278", "temperature":"35" },
{ "humidity":"1.92379703769", "windspeed":"1", "timestamp":"2016-05-12 21:19:58.437439", "temperature":"37" },
{ "humidity":"3.60238938709", "windspeed":"4", "timestamp":"2016-05-12 21:20:03.441304", "temperature":"44" },
{ "humidity":"3.18293298339", "windspeed":"4", "timestamp":"2016-05-12 21:20:08.444619", "temperature":"36" },
{ "humidity":"0.575769541098", "windspeed":"0", "timestamp":"2016-05-12 21:20:13.446948", "temperature":"35" },
{ "humidity":"1.34350746326", "windspeed":"1", "timestamp":"2016-05-12 21:20:18.453304", "temperature":"38" },
{ "humidity":"1.98822360374", "windspeed":"5", "timestamp":"2016-05-12 21:20:23.457484", "temperature":"37" },
{ "humidity":"0.315141794348", "windspeed":"0", "timestamp":"2016-05-12 21:20:28.464364", "temperature":"45" },
{ "humidity":"2.69359184496", "windspeed":"3", "timestamp":"2016-05-12 21:20:33.466869", "temperature":"45" },
{ "humidity":"2.10331981153", "windspeed":"5", "timestamp":"2016-05-12 21:20:38.471009", "temperature":"44" },
{ "humidity":"2.74287623923", "windspeed":"3", "timestamp":"2016-05-12 21:20:43.476915", "temperature":"39" },
{ "humidity":"1.4153256859", "windspeed":"0", "timestamp":"2016-05-12 21:20:48.479514", "temperature":"36" },
{ "humidity":"1.37802410842", "windspeed":"1", "timestamp":"2016-05-12 21:20:53.484441", "temperature":"40" },
{ "humidity":"1.80877249625", "windspeed":"2", "timestamp":"2016-05-12 21:20:58.490238", "temperature":"44" },
{ "humidity":"4.94605064162", "windspeed":"4", "timestamp":"2016-05-12 21:21:03.497454", "temperature":"37" },
{ "humidity":"4.75905842223", "windspeed":"4", "timestamp":"2016-05-12 21:21:08.500396", "temperature":"38" },
{ "humidity":"3.51954462885", "windspeed":"1", "timestamp":"2016-05-12 21:21:13.504909", "temperature":"40" },
{ "humidity":"3.73475171483", "windspeed":"1", "timestamp":"2016-05-12 21:21:18.508336", "temperature":"35" },
{ "humidity":"0.391446607473", "windspeed":"1", "timestamp":"2016-05-12 21:21:23.510813", "temperature":"38" },
{ "humidity":"0.594130956706", "windspeed":"5", "timestamp":"2016-05-12 21:21:28.517519", "temperature":"35" },
{ "humidity":"1.99002078488", "windspeed":"4", "timestamp":"2016-05-12 21:21:33.523741", "temperature":"45" },
{ "humidity":"3.10191038535", "windspeed":"2", "timestamp":"2016-05-12 21:21:38.527323", "temperature":"37" },
{ "humidity":"2.46212436567", "windspeed":"0", "timestamp":"2016-05-12 21:21:43.528736", "temperature":"44" },
{ "humidity":"1.02870435221", "windspeed":"5", "timestamp":"2016-05-12 21:21:48.533013", "temperature":"43" },
{ "humidity":"1.47640096791", "windspeed":"0", "timestamp":"2016-05-12 21:21:53.539648", "temperature":"42" },
{ "humidity":"2.27707731929", "windspeed":"3", "timestamp":"2016-05-12 21:21:58.545914", "temperature":"35" },
{ "humidity":"0.672084153441", "windspeed":"1", "timestamp":"2016-05-12 21:22:03.551548", "temperature":"35" },
{ "humidity":"4.6748723273", "windspeed":"0", "timestamp":"2016-05-12 21:22:08.558162", "temperature":"45" },
{ "humidity":"1.4125319516", "windspeed":"1", "timestamp":"2016-05-12 21:22:13.564487", "temperature":"40" },
{ "humidity":"2.76777559082", "windspeed":"5", "timestamp":"2016-05-12 21:22:18.568681", "temperature":"37" },
{ "humidity":"0.507850259822", "windspeed":"3", "timestamp":"2016-05-12 21:22:23.575726", "temperature":"39" },
{ "humidity":"1.20171804491", "windspeed":"3", "timestamp":"2016-05-12 21:22:28.579303", "temperature":"41" },
{ "humidity":"4.49092883763", "windspeed":"2", "timestamp":"2016-05-12 21:22:33.583642", "temperature":"40" },
{ "humidity":"1.59508966089", "windspeed":"2", "timestamp":"2016-05-12 21:22:38.587234", "temperature":"42" },
{ "humidity":"2.416767972", "windspeed":"2", "timestamp":"2016-05-12 21:22:43.591804", "temperature":"35" },
{ "humidity":"1.62382561797", "windspeed":"1", "timestamp":"2016-05-12 21:22:48.595385", "temperature":"40" },
{ "humidity":"4.36444918495", "windspeed":"2", "timestamp":"2016-05-12 21:22:53.601317", "temperature":"41" },
{ "humidity":"0.713915864423", "windspeed":"5", "timestamp":"2016-05-12 21:22:58.603844", "temperature":"36" },
{ "humidity":"0.540895029953", "windspeed":"2", "timestamp":"2016-05-12 21:23:03.606545", "temperature":"40" },
{ "humidity":"0.799479959806", "windspeed":"4", "timestamp":"2016-05-12 21:23:08.611079", "temperature":"45" },
{ "humidity":"4.76765545991", "windspeed":"1", "timestamp":"2016-05-12 21:23:13.615029", "temperature":"39" },
{ "humidity":"4.28673222713", "windspeed":"5", "timestamp":"2016-05-12 21:23:18.621572", "temperature":"38" },
{ "humidity":"1.77672174012", "windspeed":"4", "timestamp":"2016-05-12 21:23:23.625179", "temperature":"44" },
{ "humidity":"0.861260931376", "windspeed":"3", "timestamp":"2016-05-12 21:23:28.630169", "temperature":"38" },
{ "humidity":"1.42563479039", "windspeed":"0", "timestamp":"2016-05-12 21:23:33.636329", "temperature":"43" },
{ "humidity":"2.62088869113", "windspeed":"5", "timestamp":"2016-05-12 21:23:38.643824", "temperature":"42" },
{ "humidity":"2.49896862833", "windspeed":"4", "timestamp":"2016-05-12 21:23:43.646629", "temperature":"41" },
{ "humidity":"1.19745918385", "windspeed":"0", "timestamp":"2016-05-12 21:23:48.649741", "temperature":"41" },
{ "humidity":"1.11324187978", "windspeed":"2", "timestamp":"2016-05-12 21:23:53.653627", "temperature":"39" },
{ "humidity":"2.37161600645", "windspeed":"3", "timestamp":"2016-05-12 21:23:58.659705", "temperature":"43" },
{ "humidity":"3.38245230081", "windspeed":"3", "timestamp":"2016-05-12 21:24:03.664956", "temperature":"35" },
{ "humidity":"3.02312567977", "windspeed":"5", "timestamp":"2016-05-12 21:24:08.668815", "temperature":"42" },
{ "humidity":"4.6344949038", "windspeed":"5", "timestamp":"2016-05-12 21:24:13.673933", "temperature":"39" },
{ "humidity":"0.00446816610472", "windspeed":"1", "timestamp":"2016-05-12 21:24:18.676733", "temperature":"43" },
{ "humidity":"3.10069069858", "windspeed":"0", "timestamp":"2016-05-12 21:24:23.682949", "temperature":"35" },
{ "humidity":"2.08536647631", "windspeed":"5", "timestamp":"2016-05-12 21:24:28.689013", "temperature":"42" },
{ "humidity":"2.91547452844", "windspeed":"3", "timestamp":"2016-05-12 21:24:33.694245", "temperature":"39" },
{ "humidity":"1.440146085", "windspeed":"1", "timestamp":"2016-05-12 21:24:38.701026", "temperature":"37" },
{ "humidity":"4.83367527238", "windspeed":"5", "timestamp":"2016-05-12 21:24:43.705993", "temperature":"45" },
{ "humidity":"1.70069599852", "windspeed":"1", "timestamp":"2016-05-12 21:24:48.711967", "temperature":"38" },
{ "humidity":"0.321971643212", "windspeed":"5", "timestamp":"2016-05-12 21:24:53.713735", "temperature":"40" },
{ "humidity":"2.81939262675", "windspeed":"3", "timestamp":"2016-05-12 21:24:58.719374", "temperature":"43" },
{ "humidity":"1.23041817495", "windspeed":"0", "timestamp":"2016-05-12 21:25:03.724427", "temperature":"44" },
{ "humidity":"0.702642319965", "windspeed":"3", "timestamp":"2016-05-12 21:25:08.726486", "temperature":"42" },
{ "humidity":"2.48984699623", "windspeed":"2", "timestamp":"2016-05-12 21:25:13.732318", "temperature":"40" },
{ "humidity":"4.71983270495", "windspeed":"1", "timestamp":"2016-05-12 21:25:18.738896", "temperature":"37" },
{ "humidity":"3.94933282707", "windspeed":"0", "timestamp":"2016-05-12 21:25:23.742623", "temperature":"45" },
{ "humidity":"2.31932078418", "windspeed":"1", "timestamp":"2016-05-12 21:25:28.746387", "temperature":"37" },
{ "humidity":"1.24613952339", "windspeed":"0", "timestamp":"2016-05-12 21:25:33.751723", "temperature":"41" },
{ "humidity":"4.75736505842", "windspeed":"3", "timestamp":"2016-05-12 21:25:38.758547", "temperature":"43" },
{ "humidity":"2.68383834854", "windspeed":"2", "timestamp":"2016-05-12 21:25:43.761535", "temperature":"44" },
{ "humidity":"3.63150918889", "windspeed":"5", "timestamp":"2016-05-12 21:25:48.763955", "temperature":"42" },
{ "humidity":"3.48446911092", "windspeed":"1", "timestamp":"2016-05-12 21:25:53.769437", "temperature":"45" },
{ "humidity":"0.754612513821", "windspeed":"3", "timestamp":"2016-05-12 21:25:58.774761", "temperature":"39" },
{ "humidity":"1.8742333523", "windspeed":"4", "timestamp":"2016-05-12 21:26:03.779613", "temperature":"41" },
{ "humidity":"2.4814634555", "windspeed":"5", "timestamp":"2016-05-12 21:26:08.785932", "temperature":"37" },
{ "humidity":"3.60492857995", "windspeed":"2", "timestamp":"2016-05-12 21:26:13.790822", "temperature":"39" },
{ "humidity":"0.672202098137", "windspeed":"1", "timestamp":"2016-05-12 21:26:18.796858", "temperature":"41" },
{ "humidity":"3.48944440815", "windspeed":"1", "timestamp":"2016-05-12 21:26:23.798807", "temperature":"43" },
{ "humidity":"4.9382952287", "windspeed":"2", "timestamp":"2016-05-12 21:26:28.804169", "temperature":"35" },
{ "humidity":"1.6026685297", "windspeed":"4", "timestamp":"2016-05-12 21:26:33.807907", "temperature":"41" },
{ "humidity":"3.90805971851", "windspeed":"5", "timestamp":"2016-05-12 21:26:38.810532", "temperature":"36" },
{ "humidity":"2.83917242831", "windspeed":"3", "timestamp":"2016-05-12 21:26:43.815161", "temperature":"39" },
{ "humidity":"4.54671677508", "windspeed":"5", "timestamp":"2016-05-12 21:26:48.819168", "temperature":"36" },
{ "humidity":"2.56738625318", "windspeed":"0", "timestamp":"2016-05-12 21:26:53.821454", "temperature":"45" },
{ "humidity":"2.01227446933", "windspeed":"5", "timestamp":"2016-05-12 21:26:58.825549", "temperature":"45" },
{ "humidity":"0.579458709975", "windspeed":"1", "timestamp":"2016-05-12 21:27:03.831199", "temperature":"41" },
{ "humidity":"1.21999098378", "windspeed":"1", "timestamp":"2016-05-12 21:27:08.837073", "temperature":"38" },
{ "humidity":"4.26037444266", "windspeed":"2", "timestamp":"2016-05-12 21:27:13.844268", "temperature":"42" },
{ "humidity":"4.32509515303", "windspeed":"2", "timestamp":"2016-05-12 21:27:18.847623", "temperature":"40" },
{ "humidity":"4.07427296128", "windspeed":"1", "timestamp":"2016-05-12 21:27:23.852677", "temperature":"37" },
{ "humidity":"2.99409616051", "windspeed":"2", "timestamp":"2016-05-12 21:27:28.856557", "temperature":"38" },
{ "humidity":"1.86249872396", "windspeed":"0", "timestamp":"2016-05-12 21:27:33.859717", "temperature":"45" },
{ "humidity":"0.824821747002", "windspeed":"1", "timestamp":"2016-05-12 21:27:38.863780", "temperature":"44" },
{ "humidity":"3.7530897598", "windspeed":"2", "timestamp":"2016-05-12 21:27:43.866967", "temperature":"45" },
{ "humidity":"4.35003610025", "windspeed":"2", "timestamp":"2016-05-12 21:27:48.869547", "temperature":"37" },
{ "humidity":"4.31117167062", "windspeed":"2", "timestamp":"2016-05-12 21:27:53.874746", "temperature":"37" },
{ "humidity":"2.14482597674", "windspeed":"0", "timestamp":"2016-05-12 21:27:58.879990", "temperature":"38" },
{ "humidity":"3.29035183704", "windspeed":"0", "timestamp":"2016-05-12 21:28:03.881939", "temperature":"37" },
{ "humidity":"3.50930368194", "windspeed":"1", "timestamp":"2016-05-12 21:28:08.887201", "temperature":"45" },
{ "humidity":"1.71639733169", "windspeed":"2", "timestamp":"2016-05-12 21:28:13.893196", "temperature":"39" },
{ "humidity":"3.79659857602", "windspeed":"1", "timestamp":"2016-05-12 21:28:18.899861", "temperature":"36" },
{ "humidity":"1.98381468186", "windspeed":"1", "timestamp":"2016-05-12 21:28:23.901682", "temperature":"45" },
{ "humidity":"3.27661277829", "windspeed":"1", "timestamp":"2016-05-12 21:28:28.907349", "temperature":"39" },
{ "humidity":"0.821139272962", "windspeed":"3", "timestamp":"2016-05-12 21:28:33.912876", "temperature":"40" },
{ "humidity":"0.535994822035", "windspeed":"5", "timestamp":"2016-05-12 21:28:38.923706", "temperature":"41" },
{ "humidity":"0.137563839236", "windspeed":"3", "timestamp":"2016-05-12 21:28:43.929031", "temperature":"43" },
{ "humidity":"3.99374488891", "windspeed":"2", "timestamp":"2016-05-12 21:28:48.935279", "temperature":"43" },
{ "humidity":"2.84553535107", "windspeed":"0", "timestamp":"2016-05-12 21:28:53.936946", "temperature":"43" },
{ "humidity":"3.95208432718", "windspeed":"0", "timestamp":"2016-05-12 21:28:58.939718", "temperature":"41" },
{ "humidity":"2.40603873429", "windspeed":"3", "timestamp":"2016-05-12 21:29:03.944955", "temperature":"42" },
{ "humidity":"4.02638897399", "windspeed":"1", "timestamp":"2016-05-12 21:29:08.947210", "temperature":"45" },
{ "humidity":"0.601194085139", "windspeed":"1", "timestamp":"2016-05-12 21:29:13.953423", "temperature":"42" },
{ "humidity":"0.226529683543", "windspeed":"5", "timestamp":"2016-05-12 21:29:18.958547", "temperature":"43" },
{ "humidity":"2.0264093356", "windspeed":"1", "timestamp":"2016-05-12 21:29:23.960692", "temperature":"37" },
{ "humidity":"0.588323404269", "windspeed":"5", "timestamp":"2016-05-12 21:29:28.963292", "temperature":"39" },
{ "humidity":"3.11997439801", "windspeed":"2", "timestamp":"2016-05-12 21:29:33.970180", "temperature":"36" },
{ "humidity":"4.97469164893", "windspeed":"5", "timestamp":"2016-05-12 21:29:38.975927", "temperature":"38" },
{ "humidity":"1.60740257508", "windspeed":"3", "timestamp":"2016-05-12 21:29:43.981801", "temperature":"35" },
{ "humidity":"2.84972768849", "windspeed":"2", "timestamp":"2016-05-12 21:29:48.986410", "temperature":"35" },
{ "humidity":"3.06614341408", "windspeed":"3", "timestamp":"2016-05-12 21:29:53.991211", "temperature":"39" },
{ "humidity":"2.84195549509", "windspeed":"2", "timestamp":"2016-05-12 21:29:58.993840", "temperature":"43" },
{ "humidity":"4.52627299074", "windspeed":"5", "timestamp":"2016-05-12 21:30:03.995750", "temperature":"42" },
{ "humidity":"1.61518473327", "windspeed":"2", "timestamp":"2016-05-12 21:30:09.001163", "temperature":"43" },
{ "humidity":"3.18847893331", "windspeed":"5", "timestamp":"2016-05-12 21:30:14.006484", "temperature":"35" },
{ "humidity":"3.38370166159", "windspeed":"4", "timestamp":"2016-05-12 21:30:19.010941", "temperature":"43" },
{ "humidity":"3.52451799893", "windspeed":"3", "timestamp":"2016-05-12 21:30:24.017811", "temperature":"37" },
{ "humidity":"4.0835377649", "windspeed":"4", "timestamp":"2016-05-12 21:30:29.024872", "temperature":"36" },
{ "humidity":"4.16677599804", "windspeed":"0", "timestamp":"2016-05-12 21:30:34.026312", "temperature":"37" },
{ "humidity":"3.37778070349", "windspeed":"1", "timestamp":"2016-05-12 21:30:39.029464", "temperature":"36" },
{ "humidity":"1.26729726525", "windspeed":"5", "timestamp":"2016-05-12 21:30:44.036762", "temperature":"42" },
{ "humidity":"2.09593513237", "windspeed":"2", "timestamp":"2016-05-12 21:30:49.039571", "temperature":"45" },
{ "humidity":"0.871647289121", "windspeed":"3", "timestamp":"2016-05-12 21:30:54.042398", "temperature":"44" },
{ "humidity":"0.578353710286", "windspeed":"4", "timestamp":"2016-05-12 21:30:59.049828", "temperature":"35" },
{ "humidity":"4.07528475676", "windspeed":"3", "timestamp":"2016-05-12 21:31:04.053793", "temperature":"40" },
{ "humidity":"4.79512525346", "windspeed":"3", "timestamp":"2016-05-12 21:31:09.058565", "temperature":"44" },
{ "humidity":"3.73623192026", "windspeed":"4", "timestamp":"2016-05-12 21:31:14.063273", "temperature":"37" },
{ "humidity":"1.82250781983", "windspeed":"1", "timestamp":"2016-05-12 21:31:19.068893", "temperature":"42" },
{ "humidity":"0.953950662337", "windspeed":"4", "timestamp":"2016-05-12 21:31:24.074512", "temperature":"37" },
{ "humidity":"2.43643761258", "windspeed":"3", "timestamp":"2016-05-12 21:31:29.082505", "temperature":"42" },
{ "humidity":"3.14454491362", "windspeed":"3", "timestamp":"2016-05-12 21:31:34.084959", "temperature":"35" },
{ "humidity":"4.87842517429", "windspeed":"0", "timestamp":"2016-05-12 21:31:39.087360", "temperature":"35" },
{ "humidity":"0.0185939787424", "windspeed":"0", "timestamp":"2016-05-12 21:31:44.092442", "temperature":"40" },
{ "humidity":"3.71426768851", "windspeed":"2", "timestamp":"2016-05-12 21:31:49.099163", "temperature":"44" },
{ "humidity":"1.73967792298", "windspeed":"1", "timestamp":"2016-05-12 21:31:54.103635", "temperature":"40" },
{ "humidity":"2.57820746683", "windspeed":"4", "timestamp":"2016-05-12 21:31:59.112521", "temperature":"35" },
{ "humidity":"3.00777912786", "windspeed":"5", "timestamp":"2016-05-12 21:32:04.119689", "temperature":"35" },
{ "humidity":"2.33502186433", "windspeed":"0", "timestamp":"2016-05-12 21:32:09.125955", "temperature":"45" },
{ "humidity":"3.47448481242", "windspeed":"5", "timestamp":"2016-05-12 21:32:14.131829", "temperature":"36" },
{ "humidity":"0.109773004188", "windspeed":"4", "timestamp":"2016-05-12 21:32:19.135417", "temperature":"42" },
{ "humidity":"1.5317390586", "windspeed":"2", "timestamp":"2016-05-12 21:32:24.139909", "temperature":"35" },
{ "humidity":"0.6083768126", "windspeed":"3", "timestamp":"2016-05-12 21:32:29.146482", "temperature":"43" },
{ "humidity":"3.92524530052", "windspeed":"0", "timestamp":"2016-05-12 21:32:34.150582", "temperature":"35" },
{ "humidity":"0.684152199835", "windspeed":"5", "timestamp":"2016-05-12 21:32:39.156772", "temperature":"40" },
{ "humidity":"1.90398988057", "windspeed":"3", "timestamp":"2016-05-12 21:32:44.163434", "temperature":"38" },
{ "humidity":"1.51513017563", "windspeed":"1", "timestamp":"2016-05-12 21:32:49.172395", "temperature":"36" },
{ "humidity":"4.17831469175", "windspeed":"2", "timestamp":"2016-05-12 21:32:54.174959", "temperature":"45" },
{ "humidity":"1.07911644264", "windspeed":"2", "timestamp":"2016-05-12 21:32:59.180293", "temperature":"45" },
{ "humidity":"1.41383288406", "windspeed":"5", "timestamp":"2016-05-12 21:33:04.187806", "temperature":"40" },
{ "humidity":"2.212864017", "windspeed":"4", "timestamp":"2016-05-12 21:33:09.191723", "temperature":"40" },
{ "humidity":"0.611819526988", "windspeed":"4", "timestamp":"2016-05-12 21:33:14.195150", "temperature":"39" },
{ "humidity":"1.92948138341", "windspeed":"5", "timestamp":"2016-05-12 21:33:19.198475", "temperature":"37" },
{ "humidity":"2.93516358548", "windspeed":"4", "timestamp":"2016-05-12 21:33:24.201578", "temperature":"42" },
{ "humidity":"1.38832860621", "windspeed":"1", "timestamp":"2016-05-12 21:33:29.206729", "temperature":"37" },
{ "humidity":"2.50424668923", "windspeed":"4", "timestamp":"2016-05-12 21:33:34.213520", "temperature":"35" },
{ "humidity":"4.22040633605", "windspeed":"1", "timestamp":"2016-05-12 21:33:39.219809", "temperature":"43" },
{ "humidity":"0.465737029148", "windspeed":"4", "timestamp":"2016-05-12 21:33:44.223770", "temperature":"36" },
{ "humidity":"0.467660396935", "windspeed":"0", "timestamp":"2016-05-12 21:33:49.229052", "temperature":"45" },
{ "humidity":"2.77146840791", "windspeed":"4", "timestamp":"2016-05-12 21:33:54.231825", "temperature":"43" },
{ "humidity":"3.87062445507", "windspeed":"4", "timestamp":"2016-05-12 21:33:59.234651", "temperature":"37" },
{ "humidity":"4.57881099001", "windspeed":"3", "timestamp":"2016-05-12 21:34:04.239086", "temperature":"44" },
{ "humidity":"1.84116273657", "windspeed":"1", "timestamp":"2016-05-12 21:34:09.242103", "temperature":"45" },
{ "humidity":"0.619581557413", "windspeed":"2", "timestamp":"2016-05-12 21:34:14.248077", "temperature":"43" },
{ "humidity":"2.67048684825", "windspeed":"2", "timestamp":"2016-05-12 21:34:19.251846", "temperature":"37" },
{ "humidity":"1.3078278896", "windspeed":"3", "timestamp":"2016-05-12 21:34:24.253891", "temperature":"38" },
{ "humidity":"4.9229477159", "windspeed":"4", "timestamp":"2016-05-12 21:34:29.259642", "temperature":"35" },
{ "humidity":"4.31623583617", "windspeed":"4", "timestamp":"2016-05-12 21:34:34.265762", "temperature":"42" },
{ "humidity":"0.620144929422", "windspeed":"5", "timestamp":"2016-05-12 21:34:39.271375", "temperature":"37" },
{ "humidity":"0.454745487989", "windspeed":"1", "timestamp":"2016-05-12 21:34:44.276745", "temperature":"41" },
{ "humidity":"2.73963479834", "windspeed":"2", "timestamp":"2016-05-12 21:34:49.279076", "temperature":"39" },
{ "humidity":"1.6510256468", "windspeed":"3", "timestamp":"2016-05-12 21:34:54.285193", "temperature":"37" },
{ "humidity":"0.17826252507", "windspeed":"3", "timestamp":"2016-05-12 21:34:59.301116", "temperature":"43" },
{ "humidity":"1.66585649673", "windspeed":"5", "timestamp":"2016-05-12 21:35:04.307124", "temperature":"42" },
{ "humidity":"2.70951629581", "windspeed":"4", "timestamp":"2016-05-12 21:35:09.311572", "temperature":"42" },
{ "humidity":"2.10223679677", "windspeed":"3", "timestamp":"2016-05-12 21:35:14.317248", "temperature":"41" },
{ "humidity":"4.62633003919", "windspeed":"3", "timestamp":"2016-05-12 21:35:19.322273", "temperature":"44" },
{ "humidity":"3.50614645503", "windspeed":"2", "timestamp":"2016-05-12 21:35:24.328299", "temperature":"43" },
{ "humidity":"2.06505774743", "windspeed":"3", "timestamp":"2016-05-12 21:35:29.331274", "temperature":"42" },
{ "humidity":"0.0584954523554", "windspeed":"0", "timestamp":"2016-05-12 21:35:34.335940", "temperature":"42" },
{ "humidity":"3.52063685789", "windspeed":"3", "timestamp":"2016-05-12 21:35:39.342373", "temperature":"40" },
{ "humidity":"4.60905723342", "windspeed":"2", "timestamp":"2016-05-12 21:35:44.345159", "temperature":"40" },
{ "humidity":"2.96188233266", "windspeed":"3", "timestamp":"2016-05-12 21:35:49.347607", "temperature":"43" },
{ "humidity":"2.19386546514", "windspeed":"5", "timestamp":"2016-05-12 21:35:54.350489", "temperature":"45" },
{ "humidity":"4.50782695201", "windspeed":"0", "timestamp":"2016-05-12 21:35:59.354275", "temperature":"43" },
{ "humidity":"0.681739429734", "windspeed":"0", "timestamp":"2016-05-12 21:36:04.359846", "temperature":"35" },
{ "humidity":"2.06370779485", "windspeed":"4", "timestamp":"2016-05-12 21:36:09.367425", "temperature":"36" },
{ "humidity":"0.135130695257", "windspeed":"1", "timestamp":"2016-05-12 21:36:14.375159", "temperature":"40" },
{ "humidity":"0.344778830919", "windspeed":"1", "timestamp":"2016-05-12 21:36:19.379623", "temperature":"39" },
{ "humidity":"4.79430768532", "windspeed":"4", "timestamp":"2016-05-12 21:36:24.384678", "temperature":"44" },
{ "humidity":"2.51003389085", "windspeed":"4", "timestamp":"2016-05-12 21:36:29.391308", "temperature":"42" },
{ "humidity":"4.02290166397", "windspeed":"1", "timestamp":"2016-05-12 21:36:34.397722", "temperature":"43" },
{ "humidity":"1.89053068819", "windspeed":"1", "timestamp":"2016-05-12 21:36:39.402920", "temperature":"37" },
{ "humidity":"1.87175486298", "windspeed":"3", "timestamp":"2016-05-12 21:36:44.405690", "temperature":"41" },
{ "humidity":"4.01060888731", "windspeed":"3", "timestamp":"2016-05-12 21:36:49.408596", "temperature":"42" },
{ "humidity":"0.768557554942", "windspeed":"3", "timestamp":"2016-05-12 21:36:54.415202", "temperature":"36" },
{ "humidity":"2.13588669315", "windspeed":"2", "timestamp":"2016-05-12 21:36:59.418321", "temperature":"41" },
{ "humidity":"1.20639730099", "windspeed":"3", "timestamp":"2016-05-12 21:37:04.420162", "temperature":"40" },
{ "humidity":"4.31104714999", "windspeed":"2", "timestamp":"2016-05-12 21:37:09.426037", "temperature":"43" },
{ "humidity":"4.86844663776", "windspeed":"5", "timestamp":"2016-05-12 21:37:14.432388", "temperature":"43" },
{ "humidity":"0.229532309581", "windspeed":"2", "timestamp":"2016-05-12 21:37:19.440053", "temperature":"42" },
{ "humidity":"4.64996896873", "windspeed":"4", "timestamp":"2016-05-12 21:37:24.446113", "temperature":"38" },
{ "humidity":"0.326680087093", "windspeed":"2", "timestamp":"2016-05-12 21:37:29.452313", "temperature":"39" },
{ "humidity":"2.23023456166", "windspeed":"4", "timestamp":"2016-05-12 21:37:34.457890", "temperature":"44" },
{ "humidity":"0.626012411798", "windspeed":"0", "timestamp":"2016-05-12 21:37:39.462190", "temperature":"40" },
{ "humidity":"1.25453123317", "windspeed":"4", "timestamp":"2016-05-12 21:37:44.465826", "temperature":"43" },
{ "humidity":"2.98659152137", "windspeed":"2", "timestamp":"2016-05-12 21:37:49.471214", "temperature":"40" },
{ "humidity":"0.824681992201", "windspeed":"1", "timestamp":"2016-05-12 21:37:54.477798", "temperature":"43" },
{ "humidity":"4.26198177492", "windspeed":"0", "timestamp":"2016-05-12 21:37:59.482586", "temperature":"37" },
{ "humidity":"2.9512026441", "windspeed":"4", "timestamp":"2016-05-12 21:38:04.485376", "temperature":"35" },
{ "humidity":"4.45946594317", "windspeed":"3", "timestamp":"2016-05-12 21:38:09.488042", "temperature":"40" },
{ "humidity":"3.85704133812", "windspeed":"0", "timestamp":"2016-05-12 21:38:14.493461", "temperature":"41" },
{ "humidity":"4.76450855959", "windspeed":"3", "timestamp":"2016-05-12 21:38:19.498022", "temperature":"40" },
{ "humidity":"1.9681844469", "windspeed":"5", "timestamp":"2016-05-12 21:38:24.500798", "temperature":"35" },
{ "humidity":"3.17562266497", "windspeed":"4", "timestamp":"2016-05-12 21:38:29.504154", "temperature":"40" },
{ "humidity":"1.05131029468", "windspeed":"5", "timestamp":"2016-05-12 21:38:34.509255", "temperature":"36" },
{ "humidity":"1.80996902987", "windspeed":"0", "timestamp":"2016-05-12 21:38:39.514862", "temperature":"42" },
{ "humidity":"4.26868217171", "windspeed":"3", "timestamp":"2016-05-12 21:38:44.522368", "temperature":"38" },
{ "humidity":"0.230461092518", "windspeed":"1", "timestamp":"2016-05-12 21:38:49.524961", "temperature":"40" },
{ "humidity":"0.62589207928", "windspeed":"3", "timestamp":"2016-05-12 21:38:54.530428", "temperature":"45" },
{ "humidity":"2.25406445487", "windspeed":"2", "timestamp":"2016-05-12 21:38:59.532636", "temperature":"44" },
{ "humidity":"1.83656496863", "windspeed":"3", "timestamp":"2016-05-12 21:39:04.536830", "temperature":"43" },
{ "humidity":"2.72210314834", "windspeed":"0", "timestamp":"2016-05-12 21:39:09.542132", "temperature":"36" },
{ "humidity":"1.8136829915", "windspeed":"2", "timestamp":"2016-05-12 21:39:14.546512", "temperature":"37" },
{ "humidity":"1.62064138367", "windspeed":"1", "timestamp":"2016-05-12 21:39:19.553918", "temperature":"37" },
{ "humidity":"1.52326208441", "windspeed":"3", "timestamp":"2016-05-12 21:39:24.561036", "temperature":"42" },
{ "humidity":"4.12026688196", "windspeed":"4", "timestamp":"2016-05-12 21:39:29.563683", "temperature":"38" },
{ "humidity":"3.55943001992", "windspeed":"5", "timestamp":"2016-05-12 21:39:34.570608", "temperature":"41" },
{ "humidity":"1.85230131583", "windspeed":"1", "timestamp":"2016-05-12 21:39:39.573708", "temperature":"38" },
{ "humidity":"1.07536453209", "windspeed":"5", "timestamp":"2016-05-12 21:39:44.579455", "temperature":"41" },
{ "humidity":"4.34481906926", "windspeed":"4", "timestamp":"2016-05-12 21:39:49.583594", "temperature":"35" },
{ "humidity":"3.91195675349", "windspeed":"2", "timestamp":"2016-05-12 21:39:54.588794", "temperature":"39" },
{ "humidity":"0.696260070414", "windspeed":"4", "timestamp":"2016-05-12 21:39:59.590960", "temperature":"39" },
{ "humidity":"1.38013871697", "windspeed":"2", "timestamp":"2016-05-12 21:40:04.596169", "temperature":"44" },
{ "humidity":"2.9313616898", "windspeed":"5", "timestamp":"2016-05-12 21:40:09.600660", "temperature":"37" },
{ "humidity":"3.35369798698", "windspeed":"5", "timestamp":"2016-05-12 21:40:14.606336", "temperature":"37" },
{ "humidity":"1.05496821932", "windspeed":"5", "timestamp":"2016-05-12 21:40:19.610638", "temperature":"36" },
{ "humidity":"2.09592160887", "windspeed":"4", "timestamp":"2016-05-12 21:40:24.618200", "temperature":"37" },
{ "humidity":"2.90740415397", "windspeed":"1", "timestamp":"2016-05-12 21:40:29.623800", "temperature":"38" },
{ "humidity":"1.77662337551", "windspeed":"2", "timestamp":"2016-05-12 21:40:34.628662", "temperature":"39" },
{ "humidity":"2.41631086584", "windspeed":"3", "timestamp":"2016-05-12 21:40:39.630699", "temperature":"36" },
{ "humidity":"4.29169311733", "windspeed":"3", "timestamp":"2016-05-12 21:40:44.637876", "temperature":"37" },
{ "humidity":"0.66483038484", "windspeed":"1", "timestamp":"2016-05-12 21:40:49.641074", "temperature":"36" },
{ "humidity":"0.0828747010812", "windspeed":"3", "timestamp":"2016-05-12 21:40:54.644973", "temperature":"41" },
{ "humidity":"1.79357644207", "windspeed":"4", "timestamp":"2016-05-12 21:40:59.648205", "temperature":"45" },
{ "humidity":"2.47862451342", "windspeed":"5", "timestamp":"2016-05-12 21:41:04.650691", "temperature":"39" },
{ "humidity":"3.13287941271", "windspeed":"3", "timestamp":"2016-05-12 21:41:09.658041", "temperature":"45" },
{ "humidity":"1.82059753225", "windspeed":"4", "timestamp":"2016-05-12 21:41:14.669334", "temperature":"40" },
{ "humidity":"1.41224871695", "windspeed":"3", "timestamp":"2016-05-12 21:41:19.673871", "temperature":"36" },
{ "humidity":"3.74853073857", "windspeed":"2", "timestamp":"2016-05-12 21:41:24.677632", "temperature":"41" },
{ "humidity":"3.44630312465", "windspeed":"2", "timestamp":"2016-05-12 21:41:29.684450", "temperature":"35" },
{ "humidity":"3.77056350818", "windspeed":"1", "timestamp":"2016-05-12 21:41:34.687242", "temperature":"45" },
{ "humidity":"3.77806556691", "windspeed":"3", "timestamp":"2016-05-12 21:41:39.693663", "temperature":"37" },
{ "humidity":"1.06260446922", "windspeed":"0", "timestamp":"2016-05-12 21:41:44.701759", "temperature":"37" },
{ "humidity":"3.51505798022", "windspeed":"0", "timestamp":"2016-05-12 21:41:49.707928", "temperature":"44" },
{ "humidity":"2.91987583811", "windspeed":"5", "timestamp":"2016-05-12 21:41:54.711083", "temperature":"43" },
{ "humidity":"3.50543031358", "windspeed":"4", "timestamp":"2016-05-12 21:41:59.718426", "temperature":"37" },
{ "humidity":"1.88311458863", "windspeed":"2", "timestamp":"2016-05-12 21:42:04.721824", "temperature":"40" },
{ "humidity":"1.33122730849", "windspeed":"4", "timestamp":"2016-05-12 21:42:09.726411", "temperature":"44" },
{ "humidity":"0.657801073334", "windspeed":"3", "timestamp":"2016-05-12 21:42:14.729761", "temperature":"41" },
{ "humidity":"3.33547072924", "windspeed":"1", "timestamp":"2016-05-12 21:42:19.732692", "temperature":"42" },
{ "humidity":"2.56831592649", "windspeed":"0", "timestamp":"2016-05-12 21:42:24.740747", "temperature":"39" },
{ "humidity":"4.2764746994", "windspeed":"1", "timestamp":"2016-05-12 21:42:29.744990", "temperature":"41" },
{ "humidity":"2.60653512587", "windspeed":"4", "timestamp":"2016-05-12 21:42:34.747022", "temperature":"38" },
{ "humidity":"3.49431665278", "windspeed":"2", "timestamp":"2016-05-12 21:42:39.749630", "temperature":"38" },
{ "humidity":"1.12877458124", "windspeed":"2", "timestamp":"2016-05-12 21:42:44.755898", "temperature":"40" },
{ "humidity":"4.95464857186", "windspeed":"4", "timestamp":"2016-05-12 21:42:49.758669", "temperature":"42" },
{ "humidity":"1.70705049714", "windspeed":"3", "timestamp":"2016-05-12 21:42:54.762013", "temperature":"36" },
{ "humidity":"1.30526764276", "windspeed":"1", "timestamp":"2016-05-12 21:42:59.765544", "temperature":"44" },
{ "humidity":"4.85432226456", "windspeed":"3", "timestamp":"2016-05-12 21:43:04.769149", "temperature":"43" },
{ "humidity":"4.26504966036", "windspeed":"2", "timestamp":"2016-05-12 21:43:09.776390", "temperature":"43" },
{ "humidity":"1.8715289615", "windspeed":"1", "timestamp":"2016-05-12 21:43:14.780875", "temperature":"45" },
{ "humidity":"0.0849924351682", "windspeed":"1", "timestamp":"2016-05-12 21:43:19.788139", "temperature":"41" },
{ "humidity":"1.01713131495", "windspeed":"0", "timestamp":"2016-05-12 21:43:24.790834", "temperature":"42" },
{ "humidity":"1.90408742473", "windspeed":"5", "timestamp":"2016-05-12 21:43:29.795183", "temperature":"40" },
{ "humidity":"3.67312026888", "windspeed":"5", "timestamp":"2016-05-12 21:43:34.802119", "temperature":"38" },
{ "humidity":"1.13364456031", "windspeed":"1", "timestamp":"2016-05-12 21:43:39.809034", "temperature":"43" },
{ "humidity":"1.98286854737", "windspeed":"1", "timestamp":"2016-05-12 21:43:44.813786", "temperature":"45" },
{ "humidity":"2.57218630039", "windspeed":"1", "timestamp":"2016-05-12 21:43:49.820706", "temperature":"37" },
{ "humidity":"2.25456023509", "windspeed":"4", "timestamp":"2016-05-12 21:43:54.825676", "temperature":"35" },
{ "humidity":"4.31582749985", "windspeed":"4", "timestamp":"2016-05-12 21:43:59.828004", "temperature":"38" },
{ "humidity":"0.621793295094", "windspeed":"5", "timestamp":"2016-05-12 21:44:04.833307", "temperature":"37" },
{ "humidity":"3.70125765751", "windspeed":"4", "timestamp":"2016-05-12 21:44:09.839248", "temperature":"43" },
{ "humidity":"4.15102110697", "windspeed":"2", "timestamp":"2016-05-12 21:44:14.845498", "temperature":"42" },
{ "humidity":"4.56287652556", "windspeed":"3", "timestamp":"2016-05-12 21:44:19.849554", "temperature":"41" },
{ "humidity":"1.05417514083", "windspeed":"5", "timestamp":"2016-05-12 21:44:24.856121", "temperature":"41" },
{ "humidity":"3.12023668773", "windspeed":"4", "timestamp":"2016-05-12 21:44:29.860923", "temperature":"41" },
{ "humidity":"4.24606976579", "windspeed":"4", "timestamp":"2016-05-12 21:44:34.866616", "temperature":"44" },
{ "humidity":"4.80460456577", "windspeed":"3", "timestamp":"2016-05-12 21:44:39.869287", "temperature":"36" },
{ "humidity":"3.44831839501", "windspeed":"5", "timestamp":"2016-05-12 21:44:44.873562", "temperature":"41" },
{ "humidity":"1.71076756414", "windspeed":"0", "timestamp":"2016-05-12 21:44:49.881414", "temperature":"39" },
{ "humidity":"1.56757390765", "windspeed":"0", "timestamp":"2016-05-12 21:44:54.882961", "temperature":"38" },
{ "humidity":"2.21303216335", "windspeed":"4", "timestamp":"2016-05-12 21:44:59.889007", "temperature":"37" },
{ "humidity":"4.83643900409", "windspeed":"0", "timestamp":"2016-05-12 21:45:04.891673", "temperature":"39" },
{ "humidity":"1.04018527459", "windspeed":"1", "timestamp":"2016-05-12 21:45:09.895947", "temperature":"41" },
{ "humidity":"0.834985053931", "windspeed":"4", "timestamp":"2016-05-12 21:45:14.902611", "temperature":"40" },
{ "humidity":"4.47338646823", "windspeed":"0", "timestamp":"2016-05-12 21:45:19.906027", "temperature":"36" },
{ "humidity":"2.76711253554", "windspeed":"3", "timestamp":"2016-05-12 21:45:24.907830", "temperature":"39" },
{ "humidity":"1.2487499292", "windspeed":"0", "timestamp":"2016-05-12 21:45:29.911703", "temperature":"37" },
{ "humidity":"4.05851260638", "windspeed":"5", "timestamp":"2016-05-12 21:45:34.918000", "temperature":"41" },
{ "humidity":"1.21885813589", "windspeed":"0", "timestamp":"2016-05-12 21:45:39.921567", "temperature":"44" },
{ "humidity":"2.26122693846", "windspeed":"4", "timestamp":"2016-05-12 21:45:44.924899", "temperature":"40" },
{ "humidity":"4.0236684245", "windspeed":"2", "timestamp":"2016-05-12 21:45:49.932146", "temperature":"39" },
{ "humidity":"0.554566461199", "windspeed":"1", "timestamp":"2016-05-12 21:45:54.935156", "temperature":"37" },
{ "humidity":"1.43028651848", "windspeed":"5", "timestamp":"2016-05-12 21:45:59.940971", "temperature":"40" },
{ "humidity":"0.212920078075", "windspeed":"3", "timestamp":"2016-05-12 21:46:04.946721", "temperature":"40" },
{ "humidity":"4.64147733124", "windspeed":"2", "timestamp":"2016-05-12 21:46:09.950134", "temperature":"38" },
{ "humidity":"3.20597810032", "windspeed":"4", "timestamp":"2016-05-12 21:46:14.953357", "temperature":"43" },
{ "humidity":"1.70989095296", "windspeed":"1", "timestamp":"2016-05-12 21:46:19.960836", "temperature":"37" },
{ "humidity":"1.45305940857", "windspeed":"5", "timestamp":"2016-05-12 21:46:24.962696", "temperature":"41" },
{ "humidity":"0.781237717944", "windspeed":"4", "timestamp":"2016-05-12 21:46:29.964911", "temperature":"38" },
{ "humidity":"3.75667422208", "windspeed":"4", "timestamp":"2016-05-12 21:46:34.970291", "temperature":"38" },
{ "humidity":"0.387167264268", "windspeed":"1", "timestamp":"2016-05-12 21:46:39.977906", "temperature":"44" },
{ "humidity":"2.23736085407", "windspeed":"1", "timestamp":"2016-05-12 21:46:44.981390", "temperature":"42" },
{ "humidity":"3.72068602432", "windspeed":"2", "timestamp":"2016-05-12 21:46:49.986551", "temperature":"40" },
{ "humidity":"4.14957276489", "windspeed":"0", "timestamp":"2016-05-12 21:46:54.990698", "temperature":"36" },
{ "humidity":"1.56733651006", "windspeed":"2", "timestamp":"2016-05-12 21:46:59.997843", "temperature":"36" },
{ "humidity":"4.18583576378", "windspeed":"0", "timestamp":"2016-05-12 21:47:05.001177", "temperature":"40" },
{ "humidity":"1.63091114314", "windspeed":"0", "timestamp":"2016-05-12 21:47:10.004384", "temperature":"44" },
{ "humidity":"2.33316978065", "windspeed":"3", "timestamp":"2016-05-12 21:47:15.009306", "temperature":"43" },
{ "humidity":"2.74209939033", "windspeed":"1", "timestamp":"2016-05-12 21:47:20.016073", "temperature":"43" },
{ "humidity":"2.41736814976", "windspeed":"3", "timestamp":"2016-05-12 21:47:25.019224", "temperature":"37" },
{ "humidity":"0.295090323463", "windspeed":"5", "timestamp":"2016-05-12 21:47:30.021742", "temperature":"36" },
{ "humidity":"2.67873015874", "windspeed":"4", "timestamp":"2016-05-12 21:47:35.027915", "temperature":"40" },
{ "humidity":"1.72892887525", "windspeed":"1", "timestamp":"2016-05-12 21:47:40.033353", "temperature":"42" },
{ "humidity":"3.39842472544", "windspeed":"5", "timestamp":"2016-05-12 21:47:45.038213", "temperature":"45" },
{ "humidity":"3.95431247926", "windspeed":"0", "timestamp":"2016-05-12 21:47:50.047765", "temperature":"44" },
{ "humidity":"3.70769470447", "windspeed":"2", "timestamp":"2016-05-12 21:47:55.053107", "temperature":"38" },
{ "humidity":"4.65145696723", "windspeed":"1", "timestamp":"2016-05-12 21:48:00.058554", "temperature":"36" },
{ "humidity":"2.08225645824", "windspeed":"5", "timestamp":"2016-05-12 21:48:05.064200", "temperature":"42" },
{ "humidity":"2.336636891", "windspeed":"5", "timestamp":"2016-05-12 21:48:10.071366", "temperature":"45" },
{ "humidity":"0.531154740266", "windspeed":"0", "timestamp":"2016-05-12 21:48:15.076664", "temperature":"38" },
{ "humidity":"0.513949983044", "windspeed":"3", "timestamp":"2016-05-12 21:48:20.079149", "temperature":"38" },
{ "humidity":"4.13280672955", "windspeed":"5", "timestamp":"2016-05-12 21:48:25.084405", "temperature":"45" },
{ "humidity":"0.126482420796", "windspeed":"0", "timestamp":"2016-05-12 21:48:30.087617", "temperature":"41" },
{ "humidity":"0.225015196894", "windspeed":"0", "timestamp":"2016-05-12 21:48:35.091735", "temperature":"38" },
{ "humidity":"3.44882747563", "windspeed":"3", "timestamp":"2016-05-12 21:48:40.095831", "temperature":"35" },
{ "humidity":"3.11325590133", "windspeed":"4", "timestamp":"2016-05-12 21:48:45.100269", "temperature":"38" },
{ "humidity":"1.41260561574", "windspeed":"0", "timestamp":"2016-05-12 21:48:50.102661", "temperature":"36" },
{ "humidity":"4.33082867402", "windspeed":"3", "timestamp":"2016-05-12 21:48:55.108159", "temperature":"42" },
{ "humidity":"3.58729765473", "windspeed":"5", "timestamp":"2016-05-12 21:49:00.111120", "temperature":"37" },
{ "humidity":"4.80040750334", "windspeed":"0", "timestamp":"2016-05-12 21:49:05.117707", "temperature":"39" },
{ "humidity":"2.42349903325", "windspeed":"0", "timestamp":"2016-05-12 21:49:10.124889", "temperature":"36" },
{ "humidity":"0.0203245785392", "windspeed":"0", "timestamp":"2016-05-12 21:49:15.130573", "temperature":"39" },
{ "humidity":"0.911828935097", "windspeed":"2", "timestamp":"2016-05-12 21:49:20.134954", "temperature":"42" },
{ "humidity":"1.85961713376", "windspeed":"4", "timestamp":"2016-05-12 21:49:25.138253", "temperature":"38" },
{ "humidity":"1.28514997311", "windspeed":"1", "timestamp":"2016-05-12 21:49:30.140992", "temperature":"43" },
{ "humidity":"2.14292322796", "windspeed":"4", "timestamp":"2016-05-12 21:49:35.145737", "temperature":"36" },
{ "humidity":"0.717761502374", "windspeed":"3", "timestamp":"2016-05-12 21:49:40.148969", "temperature":"39" },
{ "humidity":"0.0759513418441", "windspeed":"3", "timestamp":"2016-05-12 21:49:45.154404", "temperature":"44" },
{ "humidity":"0.29632431772", "windspeed":"2", "timestamp":"2016-05-12 21:49:50.157003", "temperature":"43" },
{ "humidity":"1.08336699417", "windspeed":"3", "timestamp":"2016-05-12 21:49:55.163236", "temperature":"40" },
{ "humidity":"4.53023513426", "windspeed":"1", "timestamp":"2016-05-12 21:50:00.166405", "temperature":"37" },
{ "humidity":"1.04001710188", "windspeed":"0", "timestamp":"2016-05-12 21:50:05.172801", "temperature":"45" },
{ "humidity":"4.82610828598", "windspeed":"1", "timestamp":"2016-05-12 21:50:10.174277", "temperature":"43" },
{ "humidity":"3.73539473768", "windspeed":"1", "timestamp":"2016-05-12 21:50:15.179469", "temperature":"45" },
{ "humidity":"0.678360860326", "windspeed":"2", "timestamp":"2016-05-12 21:50:20.185264", "temperature":"39" },
{ "humidity":"4.30032049204", "windspeed":"2", "timestamp":"2016-05-12 21:50:25.191622", "temperature":"38" },
{ "humidity":"4.66530937324", "windspeed":"1", "timestamp":"2016-05-12 21:50:30.193999", "temperature":"36" },
{ "humidity":"0.0600339442324", "windspeed":"4", "timestamp":"2016-05-12 21:50:35.198352", "temperature":"39" },
{ "humidity":"1.64349687934", "windspeed":"4", "timestamp":"2016-05-12 21:50:40.204001", "temperature":"36" },
{ "humidity":"0.36115393312", "windspeed":"0", "timestamp":"2016-05-12 21:50:45.210859", "temperature":"41" },
{ "humidity":"1.45143344876", "windspeed":"3", "timestamp":"2016-05-12 21:50:50.214259", "temperature":"40" },
{ "humidity":"0.168477742741", "windspeed":"1", "timestamp":"2016-05-12 21:50:55.218068", "temperature":"40" },
{ "humidity":"3.60201043425", "windspeed":"4", "timestamp":"2016-05-12 21:51:00.223978", "temperature":"40" },
{ "humidity":"3.76934299235", "windspeed":"5", "timestamp":"2016-05-12 21:51:05.226937", "temperature":"44" },
{ "humidity":"3.09563512425", "windspeed":"5", "timestamp":"2016-05-12 21:51:10.230440", "temperature":"38" },
{ "humidity":"3.74476882723", "windspeed":"5", "timestamp":"2016-05-12 21:51:15.233014", "temperature":"35" },
{ "humidity":"4.33635888089", "windspeed":"5", "timestamp":"2016-05-12 21:51:20.239013", "temperature":"45" },
{ "humidity":"1.60855552012", "windspeed":"1", "timestamp":"2016-05-12 21:51:25.250079", "temperature":"42" },
{ "humidity":"1.29068375584", "windspeed":"0", "timestamp":"2016-05-12 21:51:30.252863", "temperature":"44" },
{ "humidity":"3.18167551885", "windspeed":"2", "timestamp":"2016-05-12 21:51:35.259415", "temperature":"45" },
{ "humidity":"1.57669296218", "windspeed":"1", "timestamp":"2016-05-12 21:51:40.266286", "temperature":"40" },
{ "humidity":"3.96642791515", "windspeed":"5", "timestamp":"2016-05-12 21:51:45.268656", "temperature":"45" },
{ "humidity":"4.60557575489", "windspeed":"3", "timestamp":"2016-05-12 21:51:50.272345", "temperature":"36" },
{ "humidity":"0.473013774612", "windspeed":"5", "timestamp":"2016-05-12 21:51:55.279400", "temperature":"38" },
{ "humidity":"1.43398160517", "windspeed":"5", "timestamp":"2016-05-12 21:52:00.282915", "temperature":"44" },
{ "humidity":"0.790302751045", "windspeed":"1", "timestamp":"2016-05-12 21:52:05.287212", "temperature":"43" },
{ "humidity":"1.56438158544", "windspeed":"0", "timestamp":"2016-05-12 21:52:10.293433", "temperature":"36" },
{ "humidity":"3.24767853444", "windspeed":"3", "timestamp":"2016-05-12 21:52:15.297988", "temperature":"35" },
{ "humidity":"4.60460516286", "windspeed":"0", "timestamp":"2016-05-12 21:52:20.303520", "temperature":"37" },
{ "humidity":"4.03027154982", "windspeed":"1", "timestamp":"2016-05-12 21:52:25.311125", "temperature":"42" },
{ "humidity":"1.59344308153", "windspeed":"1", "timestamp":"2016-05-12 21:52:30.318880", "temperature":"45" },
{ "humidity":"4.35230265623", "windspeed":"3", "timestamp":"2016-05-12 21:52:35.323490", "temperature":"42" },
{ "humidity":"2.41678979876", "windspeed":"3", "timestamp":"2016-05-12 21:52:40.328034", "temperature":"42" },
{ "humidity":"2.40270375126", "windspeed":"3", "timestamp":"2016-05-12 21:52:45.334899", "temperature":"44" },
{ "humidity":"3.26721340169", "windspeed":"2", "timestamp":"2016-05-12 21:52:50.339336", "temperature":"43" },
{ "humidity":"0.265678998644", "windspeed":"5", "timestamp":"2016-05-12 21:52:55.341947", "temperature":"36" },
{ "humidity":"3.47157588796", "windspeed":"3", "timestamp":"2016-05-12 21:53:00.345373", "temperature":"43" },
{ "humidity":"0.987863020647", "windspeed":"1", "timestamp":"2016-05-12 21:53:05.351039", "temperature":"41" },
{ "humidity":"2.58273189764", "windspeed":"2", "timestamp":"2016-05-12 21:53:10.358125", "temperature":"37" },
{ "humidity":"1.84940975443", "windspeed":"2", "timestamp":"2016-05-12 21:53:15.364000", "temperature":"38" },
{ "humidity":"1.75390234746", "windspeed":"2", "timestamp":"2016-05-12 21:53:20.367689", "temperature":"35" },
{ "humidity":"0.78550007972", "windspeed":"2", "timestamp":"2016-05-12 21:53:25.371302", "temperature":"39" },
{ "humidity":"3.08588126425", "windspeed":"0", "timestamp":"2016-05-12 21:53:30.381109", "temperature":"37" },
{ "humidity":"3.30184601834", "windspeed":"2", "timestamp":"2016-05-12 21:53:35.387270", "temperature":"41" },
{ "humidity":"3.16368146384", "windspeed":"0", "timestamp":"2016-05-12 21:53:40.390626", "temperature":"35" },
{ "humidity":"0.540646577103", "windspeed":"2", "timestamp":"2016-05-12 21:53:45.393488", "temperature":"41" },
{ "humidity":"2.91305582211", "windspeed":"0", "timestamp":"2016-05-12 21:53:50.400223", "temperature":"38" },
{ "humidity":"3.65122731625", "windspeed":"2", "timestamp":"2016-05-12 21:53:55.405971", "temperature":"40" },
{ "humidity":"3.38751957493", "windspeed":"1", "timestamp":"2016-05-12 21:54:00.409786", "temperature":"43" },
{ "humidity":"3.94308445337", "windspeed":"2", "timestamp":"2016-05-12 21:54:05.415549", "temperature":"44" },
{ "humidity":"4.83987210487", "windspeed":"2", "timestamp":"2016-05-12 21:54:10.420602", "temperature":"44" },
{ "humidity":"1.74627611115", "windspeed":"5", "timestamp":"2016-05-12 21:54:15.427173", "temperature":"35" },
{ "humidity":"1.04430001136", "windspeed":"1", "timestamp":"2016-05-12 21:54:20.432218", "temperature":"42" },
{ "humidity":"1.74831928001", "windspeed":"4", "timestamp":"2016-05-12 21:54:25.434750", "temperature":"40" },
{ "humidity":"2.85557813152", "windspeed":"5", "timestamp":"2016-05-12 21:54:30.440159", "temperature":"37" },
{ "humidity":"0.071227285688", "windspeed":"2", "timestamp":"2016-05-12 21:54:35.445220", "temperature":"39" },
{ "humidity":"1.26893710065", "windspeed":"1", "timestamp":"2016-05-12 21:54:40.450879", "temperature":"42" },
{ "humidity":"3.93016293317", "windspeed":"2", "timestamp":"2016-05-12 21:54:45.455060", "temperature":"35" },
{ "humidity":"3.30010577615", "windspeed":"0", "timestamp":"2016-05-12 21:54:50.458432", "temperature":"35" },
{ "humidity":"2.87565777078", "windspeed":"5", "timestamp":"2016-05-12 21:54:55.460661", "temperature":"44" },
{ "humidity":"2.45077143037", "windspeed":"1", "timestamp":"2016-05-12 21:55:00.466525", "temperature":"35" },
{ "humidity":"0.481265486606", "windspeed":"2", "timestamp":"2016-05-12 21:55:05.469887", "temperature":"36" },
{ "humidity":"4.9749642635", "windspeed":"2", "timestamp":"2016-05-12 21:55:10.474481", "temperature":"40" },
{ "humidity":"1.24761451219", "windspeed":"3", "timestamp":"2016-05-12 21:55:15.480256", "temperature":"44" },
{ "humidity":"2.14069435534", "windspeed":"2", "timestamp":"2016-05-12 21:55:20.486705", "temperature":"38" },
{ "humidity":"4.25727202115", "windspeed":"2", "timestamp":"2016-05-12 21:55:25.493344", "temperature":"43" },
{ "humidity":"0.533178012319", "windspeed":"1", "timestamp":"2016-05-12 21:55:30.500994", "temperature":"45" },
{ "humidity":"4.76261409644", "windspeed":"0", "timestamp":"2016-05-12 21:55:35.506925", "temperature":"40" },
{ "humidity":"1.02025421275", "windspeed":"0", "timestamp":"2016-05-12 21:55:40.512955", "temperature":"39" },
{ "humidity":"1.89144871349", "windspeed":"4", "timestamp":"2016-05-12 21:55:45.516441", "temperature":"36" },
{ "humidity":"4.9698666001", "windspeed":"0", "timestamp":"2016-05-12 21:55:50.518610", "temperature":"38" },
{ "humidity":"3.43386033683", "windspeed":"2", "timestamp":"2016-05-12 21:55:55.523763", "temperature":"36" },
{ "humidity":"2.18417029968", "windspeed":"2", "timestamp":"2016-05-12 21:56:00.527470", "temperature":"38" },
{ "humidity":"4.72350209393", "windspeed":"0", "timestamp":"2016-05-12 21:56:05.534694", "temperature":"44" },
{ "humidity":"4.01006961232", "windspeed":"0", "timestamp":"2016-05-12 21:56:10.540027", "temperature":"42" },
{ "humidity":"2.0044036499", "windspeed":"3", "timestamp":"2016-05-12 21:56:15.547070", "temperature":"38" },
{ "humidity":"4.47619557227", "windspeed":"3", "timestamp":"2016-05-12 21:56:20.552933", "temperature":"40" },
{ "humidity":"4.51092571393", "windspeed":"2", "timestamp":"2016-05-12 21:56:25.559587", "temperature":"42" },
{ "humidity":"2.99036277653", "windspeed":"4", "timestamp":"2016-05-12 21:56:30.563468", "temperature":"40" },
{ "humidity":"1.06191835608", "windspeed":"0", "timestamp":"2016-05-12 21:56:35.568382", "temperature":"43" },
{ "humidity":"1.04587434313", "windspeed":"1", "timestamp":"2016-05-12 21:56:40.571276", "temperature":"42" },
{ "humidity":"2.06536940727", "windspeed":"0", "timestamp":"2016-05-12 21:56:45.577302", "temperature":"44" },
{ "humidity":"0.015843641423", "windspeed":"2", "timestamp":"2016-05-12 21:56:50.582316", "temperature":"37" },
{ "humidity":"3.68505985022", "windspeed":"5", "timestamp":"2016-05-12 21:56:55.586446", "temperature":"37" },
{ "humidity":"3.0769889099", "windspeed":"3", "timestamp":"2016-05-12 21:57:00.588998", "temperature":"35" },
{ "humidity":"4.7357128803", "windspeed":"4", "timestamp":"2016-05-12 21:57:05.595897", "temperature":"38" },
{ "humidity":"0.467949443457", "windspeed":"2", "timestamp":"2016-05-12 21:57:10.601402", "temperature":"43" },
{ "humidity":"1.8074134748", "windspeed":"4", "timestamp":"2016-05-12 21:57:15.607665", "temperature":"44" },
{ "humidity":"0.394349515689", "windspeed":"1", "timestamp":"2016-05-12 21:57:20.610895", "temperature":"35" },
{ "humidity":"0.887385879871", "windspeed":"1", "timestamp":"2016-05-12 21:57:25.616034", "temperature":"39" },
{ "humidity":"2.18538660951", "windspeed":"5", "timestamp":"2016-05-12 21:57:30.620936", "temperature":"41" },
{ "humidity":"3.74505724589", "windspeed":"2", "timestamp":"2016-05-12 21:57:35.624092", "temperature":"42" },
{ "humidity":"1.4836035162", "windspeed":"2", "timestamp":"2016-05-12 21:57:40.628245", "temperature":"43" },
{ "humidity":"3.66869279119", "windspeed":"2", "timestamp":"2016-05-12 21:57:45.635052", "temperature":"38" },
{ "humidity":"0.416456108947", "windspeed":"0", "timestamp":"2016-05-12 21:57:50.638245", "temperature":"39" },
{ "humidity":"1.71092410811", "windspeed":"2", "timestamp":"2016-05-12 21:57:55.642942", "temperature":"45" },
{ "humidity":"4.70908202755", "windspeed":"3", "timestamp":"2016-05-12 21:58:00.647170", "temperature":"42" },
{ "humidity":"0.445253204552", "windspeed":"1", "timestamp":"2016-05-12 21:58:05.652727", "temperature":"43" },
{ "humidity":"4.98253894763", "windspeed":"2", "timestamp":"2016-05-12 21:58:10.656029", "temperature":"37" },
{ "humidity":"1.42460309448", "windspeed":"1", "timestamp":"2016-05-12 21:58:15.662226", "temperature":"40" },
{ "humidity":"2.5730504884", "windspeed":"4", "timestamp":"2016-05-12 21:58:20.670122", "temperature":"35" },
{ "humidity":"3.38129903874", "windspeed":"3", "timestamp":"2016-05-12 21:58:25.673701", "temperature":"42" },
{ "humidity":"0.741833328528", "windspeed":"1", "timestamp":"2016-05-12 21:58:30.678813", "temperature":"40" },
{ "humidity":"3.23815802934", "windspeed":"1", "timestamp":"2016-05-12 21:58:35.681811", "temperature":"44" },
{ "humidity":"1.98369156914", "windspeed":"0", "timestamp":"2016-05-12 21:58:40.688393", "temperature":"41" },
{ "humidity":"1.75898441867", "windspeed":"0", "timestamp":"2016-05-12 21:58:45.692033", "temperature":"35" },
{ "humidity":"0.260885799677", "windspeed":"2", "timestamp":"2016-05-12 21:58:50.698991", "temperature":"36" },
{ "humidity":"2.58762940846", "windspeed":"4", "timestamp":"2016-05-12 21:58:55.702819", "temperature":"36" },
{ "humidity":"2.4545158052", "windspeed":"4", "timestamp":"2016-05-12 21:59:00.707479", "temperature":"36" },
{ "humidity":"1.08281472967", "windspeed":"1", "timestamp":"2016-05-12 21:59:05.713838", "temperature":"43" },
{ "humidity":"0.884165406725", "windspeed":"4", "timestamp":"2016-05-12 21:59:10.717871", "temperature":"43" },
{ "humidity":"3.76814550255", "windspeed":"4", "timestamp":"2016-05-12 21:59:15.722385", "temperature":"45" },
{ "humidity":"1.71281451092", "windspeed":"0", "timestamp":"2016-05-12 21:59:20.728399", "temperature":"37" },
{ "humidity":"3.85595433839", "windspeed":"0", "timestamp":"2016-05-12 21:59:25.731739", "temperature":"44" },
{ "humidity":"1.50136775064", "windspeed":"3", "timestamp":"2016-05-12 21:59:30.736659", "temperature":"44" },
{ "humidity":"4.35500502823", "windspeed":"4", "timestamp":"2016-05-12 21:59:35.743156", "temperature":"43" },
{ "humidity":"4.46580150291", "windspeed":"1", "timestamp":"2016-05-12 21:59:40.747744", "temperature":"43" },
{ "humidity":"4.04651998641", "windspeed":"1", "timestamp":"2016-05-12 21:59:45.753260", "temperature":"43" },
{ "humidity":"2.58324395343", "windspeed":"2", "timestamp":"2016-05-12 21:59:50.757540", "temperature":"36" },
{ "humidity":"3.63833228974", "windspeed":"2", "timestamp":"2016-05-12 21:59:55.763202", "temperature":"39" },
{ "humidity":"0.7704903725", "windspeed":"2", "timestamp":"2016-05-12 22:00:00.767208", "temperature":"45" },
{ "humidity":"4.88509592002", "windspeed":"2", "timestamp":"2016-05-12 22:00:05.772388", "temperature":"38" },
{ "humidity":"3.75830953731", "windspeed":"0", "timestamp":"2016-05-12 22:00:10.775689", "temperature":"37" },
{ "humidity":"0.361983581021", "windspeed":"0", "timestamp":"2016-05-12 22:00:15.780806", "temperature":"36" },
{ "humidity":"4.86794733517", "windspeed":"4", "timestamp":"2016-05-12 22:00:20.785589", "temperature":"39" },
{ "humidity":"0.880769360405", "windspeed":"5", "timestamp":"2016-05-12 22:00:25.789922", "temperature":"42" },
{ "humidity":"1.65106643961", "windspeed":"4", "timestamp":"2016-05-12 22:00:30.792595", "temperature":"45" },
{ "humidity":"0.914292222038", "windspeed":"2", "timestamp":"2016-05-12 22:00:35.795540", "temperature":"37" },
{ "humidity":"1.62934085031", "windspeed":"4", "timestamp":"2016-05-12 22:00:40.800213", "temperature":"41" },
{ "humidity":"0.0751369761284", "windspeed":"2", "timestamp":"2016-05-12 22:00:45.803970", "temperature":"35" },
{ "humidity":"4.94723626445", "windspeed":"0", "timestamp":"2016-05-12 22:00:50.806528", "temperature":"42" },
{ "humidity":"0.389443412202", "windspeed":"5", "timestamp":"2016-05-12 22:00:55.808959", "temperature":"45" },
{ "humidity":"0.83181793256", "windspeed":"0", "timestamp":"2016-05-12 22:01:00.813813", "temperature":"41" },
{ "humidity":"3.02249759464", "windspeed":"2", "timestamp":"2016-05-12 22:01:05.818366", "temperature":"43" },
{ "humidity":"4.90379822103", "windspeed":"3", "timestamp":"2016-05-12 22:01:10.820879", "temperature":"45" },
{ "humidity":"0.504021474397", "windspeed":"1", "timestamp":"2016-05-12 22:01:15.824362", "temperature":"37" },
{ "humidity":"1.40128710181", "windspeed":"4", "timestamp":"2016-05-12 22:01:20.831098", "temperature":"44" },
{ "humidity":"2.01328266623", "windspeed":"0", "timestamp":"2016-05-12 22:01:25.835269", "temperature":"44" },
{ "humidity":"0.56748988146", "windspeed":"0", "timestamp":"2016-05-12 22:01:30.840644", "temperature":"45" },
{ "humidity":"2.23995315542", "windspeed":"5", "timestamp":"2016-05-12 22:01:35.844949", "temperature":"37" },
{ "humidity":"2.84191184808", "windspeed":"2", "timestamp":"2016-05-12 22:01:40.848055", "temperature":"44" },
{ "humidity":"1.05028462455", "windspeed":"5", "timestamp":"2016-05-12 22:01:45.851447", "temperature":"42" },
{ "humidity":"0.232455704814", "windspeed":"0", "timestamp":"2016-05-12 22:01:50.856859", "temperature":"42" },
{ "humidity":"3.57073401102", "windspeed":"5", "timestamp":"2016-05-12 22:01:55.859776", "temperature":"45" },
{ "humidity":"0.454086969542", "windspeed":"0", "timestamp":"2016-05-12 22:02:00.865092", "temperature":"38" },
{ "humidity":"3.84257660415", "windspeed":"5", "timestamp":"2016-05-12 22:02:05.867602", "temperature":"42" },
{ "humidity":"2.66516601911", "windspeed":"0", "timestamp":"2016-05-12 22:02:10.869556", "temperature":"36" },
{ "humidity":"0.394505079503", "windspeed":"1", "timestamp":"2016-05-12 22:02:15.874489", "temperature":"40" },
{ "humidity":"3.97927155602", "windspeed":"1", "timestamp":"2016-05-12 22:02:20.881155", "temperature":"35" },
{ "humidity":"3.42726792301", "windspeed":"3", "timestamp":"2016-05-12 22:02:25.887627", "temperature":"36" },
{ "humidity":"0.377325853813", "windspeed":"2", "timestamp":"2016-05-12 22:02:30.890483", "temperature":"35" },
{ "humidity":"4.33596180635", "windspeed":"5", "timestamp":"2016-05-12 22:02:35.897616", "temperature":"43" },
{ "humidity":"1.57075772361", "windspeed":"3", "timestamp":"2016-05-12 22:02:40.901896", "temperature":"42" },
{ "humidity":"2.01292594342", "windspeed":"4", "timestamp":"2016-05-12 22:02:45.908298", "temperature":"44" },
{ "humidity":"2.47658872767", "windspeed":"4", "timestamp":"2016-05-12 22:02:50.911023", "temperature":"40" },
{ "humidity":"4.45885023774", "windspeed":"5", "timestamp":"2016-05-12 22:02:55.916449", "temperature":"43" },
{ "humidity":"1.66273928812", "windspeed":"1", "timestamp":"2016-05-12 22:03:00.922963", "temperature":"40" },
{ "humidity":"2.06889987546", "windspeed":"3", "timestamp":"2016-05-12 22:03:05.927536", "temperature":"45" },
{ "humidity":"0.00770326056616", "windspeed":"5", "timestamp":"2016-05-12 22:03:10.929676", "temperature":"40" },
{ "humidity":"4.50507901151", "windspeed":"4", "timestamp":"2016-05-12 22:03:15.935035", "temperature":"44" },
{ "humidity":"3.50701803569", "windspeed":"5", "timestamp":"2016-05-12 22:03:20.937227", "temperature":"45" },
{ "humidity":"1.47089476477", "windspeed":"0", "timestamp":"2016-05-12 22:03:25.942892", "temperature":"45" },
{ "humidity":"4.62241839897", "windspeed":"2", "timestamp":"2016-05-12 22:03:30.946335", "temperature":"45" },
{ "humidity":"1.67623004846", "windspeed":"1", "timestamp":"2016-05-12 22:03:35.949032", "temperature":"37" },
{ "humidity":"4.21426537248", "windspeed":"0", "timestamp":"2016-05-12 22:03:40.954178", "temperature":"41" },
{ "humidity":"3.88461319502", "windspeed":"4", "timestamp":"2016-05-12 22:03:45.956793", "temperature":"42" },
{ "humidity":"2.75509255426", "windspeed":"1", "timestamp":"2016-05-12 22:03:50.961513", "temperature":"40" },
{ "humidity":"1.4757905829", "windspeed":"4", "timestamp":"2016-05-12 22:03:55.966153", "temperature":"44" },
{ "humidity":"0.319545421128", "windspeed":"1", "timestamp":"2016-05-12 22:04:00.968601", "temperature":"40" },
{ "humidity":"1.68370485472", "windspeed":"1", "timestamp":"2016-05-12 22:04:05.970792", "temperature":"39" },
{ "humidity":"4.63790041908", "windspeed":"4", "timestamp":"2016-05-12 22:04:10.978433", "temperature":"37" },
{ "humidity":"4.99808014286", "windspeed":"1", "timestamp":"2016-05-12 22:04:15.979856", "temperature":"44" },
{ "humidity":"1.64568885518", "windspeed":"3", "timestamp":"2016-05-12 22:04:20.985657", "temperature":"43" },
{ "humidity":"2.34906566911", "windspeed":"3", "timestamp":"2016-05-12 22:04:25.987677", "temperature":"37" },
{ "humidity":"1.26980746331", "windspeed":"2", "timestamp":"2016-05-12 22:04:30.990733", "temperature":"43" },
{ "humidity":"2.71004680911", "windspeed":"4", "timestamp":"2016-05-12 22:04:35.994784", "temperature":"43" },
{ "humidity":"2.88365502157", "windspeed":"4", "timestamp":"2016-05-12 22:04:41.001101", "temperature":"35" },
{ "humidity":"2.54730572615", "windspeed":"4", "timestamp":"2016-05-12 22:04:46.007726", "temperature":"44" },
{ "humidity":"1.71173123276", "windspeed":"2", "timestamp":"2016-05-12 22:04:51.011894", "temperature":"41" },
{ "humidity":"4.89070423786", "windspeed":"2", "timestamp":"2016-05-12 22:04:56.016586", "temperature":"45" },
{ "humidity":"0.575290159745", "windspeed":"5", "timestamp":"2016-05-12 22:05:01.020135", "temperature":"37" },
{ "humidity":"0.135677143763", "windspeed":"2", "timestamp":"2016-05-12 22:05:06.024503", "temperature":"39" },
{ "humidity":"2.01558697082", "windspeed":"4", "timestamp":"2016-05-12 22:05:11.027286", "temperature":"41" },
{ "humidity":"4.55404304689", "windspeed":"3", "timestamp":"2016-05-12 22:05:16.034718", "temperature":"44" },
{ "humidity":"2.96934143552", "windspeed":"5", "timestamp":"2016-05-12 22:05:21.038556", "temperature":"43" },
{ "humidity":"4.20313323567", "windspeed":"5", "timestamp":"2016-05-12 22:05:26.043353", "temperature":"38" },
{ "humidity":"3.49146416236", "windspeed":"2", "timestamp":"2016-05-12 22:05:31.045738", "temperature":"41" },
{ "humidity":"2.02511927631", "windspeed":"2", "timestamp":"2016-05-12 22:05:36.048447", "temperature":"45" },
{ "humidity":"3.52258472535", "windspeed":"2", "timestamp":"2016-05-12 22:05:41.053400", "temperature":"40" },
{ "humidity":"4.88151749822", "windspeed":"1", "timestamp":"2016-05-12 22:05:46.059775", "temperature":"36" },
{ "humidity":"2.70806082878", "windspeed":"5", "timestamp":"2016-05-12 22:05:51.064867", "temperature":"40" },
{ "humidity":"0.150772585966", "windspeed":"4", "timestamp":"2016-05-12 22:05:56.069474", "temperature":"37" },
{ "humidity":"4.74747847254", "windspeed":"4", "timestamp":"2016-05-12 22:06:01.073537", "temperature":"39" },
{ "humidity":"3.70282894368", "windspeed":"4", "timestamp":"2016-05-12 22:06:06.079494", "temperature":"42" },
{ "humidity":"1.78997270678", "windspeed":"5", "timestamp":"2016-05-12 22:06:11.083143", "temperature":"44" },
{ "humidity":"4.85915520914", "windspeed":"1", "timestamp":"2016-05-12 22:06:16.085642", "temperature":"35" },
{ "humidity":"3.75433747804", "windspeed":"1", "timestamp":"2016-05-12 22:06:21.088163", "temperature":"41" },
{ "humidity":"0.647879706092", "windspeed":"4", "timestamp":"2016-05-12 22:06:26.092155", "temperature":"45" },
{ "humidity":"1.32155834511", "windspeed":"2", "timestamp":"2016-05-12 22:06:31.095303", "temperature":"39" },
{ "humidity":"1.87964293459", "windspeed":"4", "timestamp":"2016-05-12 22:06:36.102393", "temperature":"42" },
{ "humidity":"4.34439237976", "windspeed":"5", "timestamp":"2016-05-12 22:06:41.108264", "temperature":"39" },
{ "humidity":"3.02314527821", "windspeed":"4", "timestamp":"2016-05-12 22:06:46.114812", "temperature":"44" },
{ "humidity":"0.695433469377", "windspeed":"1", "timestamp":"2016-05-12 22:06:51.116553", "temperature":"43" },
{ "humidity":"0.630526115166", "windspeed":"5", "timestamp":"2016-05-12 22:06:56.122772", "temperature":"38" },
{ "humidity":"3.77581638162", "windspeed":"0", "timestamp":"2016-05-12 22:07:01.126566", "temperature":"36" },
{ "humidity":"0.738653504704", "windspeed":"2", "timestamp":"2016-05-12 22:07:06.130463", "temperature":"43" },
{ "humidity":"2.15726402433", "windspeed":"3", "timestamp":"2016-05-12 22:07:11.135641", "temperature":"36" },
{ "humidity":"4.37581222322", "windspeed":"3", "timestamp":"2016-05-12 22:07:16.141057", "temperature":"36" },
{ "humidity":"3.18139807627", "windspeed":"4", "timestamp":"2016-05-12 22:07:21.143694", "temperature":"44" },
{ "humidity":"0.939795397233", "windspeed":"5", "timestamp":"2016-05-12 22:07:26.147918", "temperature":"42" },
{ "humidity":"1.68608242951", "windspeed":"4", "timestamp":"2016-05-12 22:07:31.150091", "temperature":"40" },
{ "humidity":"4.41294355209", "windspeed":"5", "timestamp":"2016-05-12 22:07:36.153108", "temperature":"37" },
{ "humidity":"3.74730123658", "windspeed":"2", "timestamp":"2016-05-12 22:07:41.160690", "temperature":"35" },
{ "humidity":"1.18971730089", "windspeed":"1", "timestamp":"2016-05-12 22:07:46.166406", "temperature":"40" },
{ "humidity":"2.22386750776", "windspeed":"5", "timestamp":"2016-05-12 22:07:51.169708", "temperature":"41" },
{ "humidity":"4.38092118591", "windspeed":"3", "timestamp":"2016-05-12 22:07:56.172694", "temperature":"39" },
{ "humidity":"4.4327267083", "windspeed":"0", "timestamp":"2016-05-12 22:08:01.179295", "temperature":"40" },
{ "humidity":"1.17012565053", "windspeed":"4", "timestamp":"2016-05-12 22:08:06.184343", "temperature":"39" },
{ "humidity":"4.34627731603", "windspeed":"2", "timestamp":"2016-05-12 22:08:11.189701", "temperature":"39" },
{ "humidity":"2.16260709631", "windspeed":"1", "timestamp":"2016-05-12 22:08:16.197045", "temperature":"44" },
{ "humidity":"4.18893922214", "windspeed":"0", "timestamp":"2016-05-12 22:08:21.202209", "temperature":"42" },
{ "humidity":"3.20004670827", "windspeed":"2", "timestamp":"2016-05-12 22:08:26.205891", "temperature":"41" },
{ "humidity":"3.31164646409", "windspeed":"0", "timestamp":"2016-05-12 22:08:31.208694", "temperature":"39" },
{ "humidity":"2.85214824745", "windspeed":"2", "timestamp":"2016-05-12 22:08:36.212323", "temperature":"40" },
{ "humidity":"1.88705326731", "windspeed":"5", "timestamp":"2016-05-12 22:08:41.215540", "temperature":"41" },
{ "humidity":"4.86890557646", "windspeed":"0", "timestamp":"2016-05-12 22:08:46.219987", "temperature":"41" },
{ "humidity":"1.08516496825", "windspeed":"5", "timestamp":"2016-05-12 22:08:51.222092", "temperature":"43" },
{ "humidity":"1.62356837687", "windspeed":"2", "timestamp":"2016-05-12 22:08:56.224623", "temperature":"37" },
{ "humidity":"1.05499443422", "windspeed":"0", "timestamp":"2016-05-12 22:09:01.228146", "temperature":"35" },
{ "humidity":"4.88195224231", "windspeed":"3", "timestamp":"2016-05-12 22:09:06.233008", "temperature":"38" },
{ "humidity":"0.214234031191", "windspeed":"0", "timestamp":"2016-05-12 22:09:11.244095", "temperature":"42" },
{ "humidity":"1.17128021363", "windspeed":"1", "timestamp":"2016-05-12 22:09:16.249312", "temperature":"42" },
{ "humidity":"1.14336557241", "windspeed":"3", "timestamp":"2016-05-12 22:09:21.256021", "temperature":"37" },
{ "humidity":"4.75185940935", "windspeed":"2", "timestamp":"2016-05-12 22:09:26.259528", "temperature":"41" },
{ "humidity":"4.493967096", "windspeed":"3", "timestamp":"2016-05-12 22:09:31.262619", "temperature":"37" },
{ "humidity":"4.72120493826", "windspeed":"3", "timestamp":"2016-05-12 22:09:36.266439", "temperature":"42" },
{ "humidity":"1.70290796969", "windspeed":"3", "timestamp":"2016-05-12 22:09:41.268747", "temperature":"43" },
{ "humidity":"3.74380684455", "windspeed":"5", "timestamp":"2016-05-12 22:09:46.272354", "temperature":"35" },
{ "humidity":"3.96297501087", "windspeed":"3", "timestamp":"2016-05-12 22:09:51.278934", "temperature":"38" },
{ "humidity":"0.926942784008", "windspeed":"1", "timestamp":"2016-05-12 22:09:56.285624", "temperature":"40" },
{ "humidity":"2.84903243184", "windspeed":"4", "timestamp":"2016-05-12 22:10:01.288517", "temperature":"39" },
{ "humidity":"3.88380307859", "windspeed":"2", "timestamp":"2016-05-12 22:10:06.292757", "temperature":"43" },
{ "humidity":"2.41784625522", "windspeed":"5", "timestamp":"2016-05-12 22:10:11.299339", "temperature":"43" },
{ "humidity":"3.71687260006", "windspeed":"5", "timestamp":"2016-05-12 22:10:16.303317", "temperature":"41" },
{ "humidity":"4.44485256176", "windspeed":"1", "timestamp":"2016-05-12 22:10:21.307869", "temperature":"40" },
{ "humidity":"4.24313887598", "windspeed":"5", "timestamp":"2016-05-12 22:10:26.313245", "temperature":"42" },
{ "humidity":"0.220801815838", "windspeed":"2", "timestamp":"2016-05-12 22:10:31.318353", "temperature":"39" },
{ "humidity":"2.97724260545", "windspeed":"2", "timestamp":"2016-05-12 22:10:36.325601", "temperature":"37" },
{ "humidity":"4.01270717279", "windspeed":"4", "timestamp":"2016-05-12 22:10:41.332587", "temperature":"45" },
{ "humidity":"0.932024015344", "windspeed":"1", "timestamp":"2016-05-12 22:10:46.336537", "temperature":"36" },
{ "humidity":"3.82902737492", "windspeed":"3", "timestamp":"2016-05-12 22:10:51.342717", "temperature":"45" },
{ "humidity":"4.33279976009", "windspeed":"0", "timestamp":"2016-05-12 22:10:56.347330", "temperature":"38" },
{ "humidity":"0.823628101678", "windspeed":"4", "timestamp":"2016-05-12 22:11:01.349307", "temperature":"42" },
{ "humidity":"2.62350739885", "windspeed":"4", "timestamp":"2016-05-12 22:11:06.352126", "temperature":"39" },
{ "humidity":"0.451224694759", "windspeed":"3", "timestamp":"2016-05-12 22:11:11.355517", "temperature":"39" },
{ "humidity":"0.525767975828", "windspeed":"2", "timestamp":"2016-05-12 22:11:16.362871", "temperature":"35" },
{ "humidity":"4.78119053662", "windspeed":"0", "timestamp":"2016-05-12 22:11:21.367310", "temperature":"45" },
{ "humidity":"1.3378940629", "windspeed":"5", "timestamp":"2016-05-12 22:11:26.370397", "temperature":"37" },
{ "humidity":"3.23039831914", "windspeed":"3", "timestamp":"2016-05-12 22:11:31.374110", "temperature":"36" },
{ "humidity":"2.27375629109", "windspeed":"5", "timestamp":"2016-05-12 22:11:36.380314", "temperature":"36" },
{ "humidity":"1.88813092715", "windspeed":"0", "timestamp":"2016-05-12 22:11:41.384302", "temperature":"39" },
{ "humidity":"2.30434914613", "windspeed":"5", "timestamp":"2016-05-12 22:11:46.389018", "temperature":"35" },
{ "humidity":"3.86751538882", "windspeed":"5", "timestamp":"2016-05-12 22:11:51.393971", "temperature":"44" },
{ "humidity":"1.12763760952", "windspeed":"4", "timestamp":"2016-05-12 22:11:56.396333", "temperature":"41" },
{ "humidity":"2.3441322618", "windspeed":"4", "timestamp":"2016-05-12 22:12:01.400775", "temperature":"45" },
{ "humidity":"3.48366494678", "windspeed":"4", "timestamp":"2016-05-12 22:12:06.404727", "temperature":"43" },
{ "humidity":"4.58257012185", "windspeed":"4", "timestamp":"2016-05-12 22:12:11.411291", "temperature":"41" },
{ "humidity":"1.26714972571", "windspeed":"2", "timestamp":"2016-05-12 22:12:16.414502", "temperature":"44" },
{ "humidity":"3.18170575021", "windspeed":"3", "timestamp":"2016-05-12 22:12:21.417156", "temperature":"44" },
{ "humidity":"0.414441926152", "windspeed":"1", "timestamp":"2016-05-12 22:12:26.425314", "temperature":"40" },
{ "humidity":"1.5148446802", "windspeed":"1", "timestamp":"2016-05-12 22:12:31.431525", "temperature":"42" },
{ "humidity":"3.73518972315", "windspeed":"1", "timestamp":"2016-05-12 22:12:36.434893", "temperature":"42" },
{ "humidity":"2.25865389572", "windspeed":"0", "timestamp":"2016-05-12 22:12:41.438500", "temperature":"42" },
{ "humidity":"1.86006858514", "windspeed":"0", "timestamp":"2016-05-12 22:12:46.444262", "temperature":"41" },
{ "humidity":"3.80698771564", "windspeed":"1", "timestamp":"2016-05-12 22:12:51.448508", "temperature":"39" },
{ "humidity":"4.5984850964", "windspeed":"1", "timestamp":"2016-05-12 22:12:56.451578", "temperature":"45" },
{ "humidity":"0.801392308288", "windspeed":"1", "timestamp":"2016-05-12 22:13:01.455570", "temperature":"38" },
{ "humidity":"4.53572949349", "windspeed":"5", "timestamp":"2016-05-12 22:13:06.458498", "temperature":"37" },
{ "humidity":"0.491209789873", "windspeed":"2", "timestamp":"2016-05-12 22:13:11.464032", "temperature":"40" },
{ "humidity":"0.613677116351", "windspeed":"5", "timestamp":"2016-05-12 22:13:16.466251", "temperature":"38" },
{ "humidity":"4.4395056841", "windspeed":"5", "timestamp":"2016-05-12 22:13:21.471989", "temperature":"35" },
{ "humidity":"4.88782602664", "windspeed":"5", "timestamp":"2016-05-12 22:13:26.476429", "temperature":"41" },
{ "humidity":"0.438074848325", "windspeed":"3", "timestamp":"2016-05-12 22:13:31.482001", "temperature":"35" },
{ "humidity":"1.64212941553", "windspeed":"3", "timestamp":"2016-05-12 22:13:36.489329", "temperature":"42" },
{ "humidity":"3.76006627627", "windspeed":"4", "timestamp":"2016-05-12 22:13:41.493231", "temperature":"39" },
{ "humidity":"1.7053293534", "windspeed":"5", "timestamp":"2016-05-12 22:13:46.498990", "temperature":"45" },
{ "humidity":"3.24567206307", "windspeed":"1", "timestamp":"2016-05-12 22:13:51.503163", "temperature":"45" },
{ "humidity":"1.29458681745", "windspeed":"0", "timestamp":"2016-05-12 22:13:56.505825", "temperature":"41" },
{ "humidity":"0.434994993733", "windspeed":"3", "timestamp":"2016-05-12 22:14:01.512706", "temperature":"39" },
{ "humidity":"1.03564305226", "windspeed":"2", "timestamp":"2016-05-12 22:14:06.514590", "temperature":"35" },
{ "humidity":"2.53481887792", "windspeed":"5", "timestamp":"2016-05-12 22:14:11.521951", "temperature":"35" },
{ "humidity":"2.31594660268", "windspeed":"3", "timestamp":"2016-05-12 22:14:16.523558", "temperature":"42" },
{ "humidity":"2.70850602653", "windspeed":"3", "timestamp":"2016-05-12 22:14:21.526486", "temperature":"35" },
{ "humidity":"2.54134371166", "windspeed":"1", "timestamp":"2016-05-12 22:14:26.530750", "temperature":"40" },
{ "humidity":"1.34664086998", "windspeed":"0", "timestamp":"2016-05-12 22:14:31.535828", "temperature":"37" },
{ "humidity":"3.83773596778", "windspeed":"4", "timestamp":"2016-05-12 22:14:36.542222", "temperature":"39" },
{ "humidity":"3.72127827381", "windspeed":"5", "timestamp":"2016-05-12 22:14:41.544305", "temperature":"43" },
{ "humidity":"2.9241367021", "windspeed":"5", "timestamp":"2016-05-12 22:14:46.546946", "temperature":"43" },
{ "humidity":"3.32235382073", "windspeed":"3", "timestamp":"2016-05-12 22:14:51.549683", "temperature":"45" },
{ "humidity":"1.58585112913", "windspeed":"4", "timestamp":"2016-05-12 22:14:56.552160", "temperature":"35" },
{ "humidity":"1.65911901783", "windspeed":"5", "timestamp":"2016-05-12 22:15:01.555950", "temperature":"42" },
{ "humidity":"3.60904219748", "windspeed":"3", "timestamp":"2016-05-12 22:15:06.560192", "temperature":"42" },
{ "humidity":"2.1656888521", "windspeed":"4", "timestamp":"2016-05-12 22:15:11.565702", "temperature":"42" },
{ "humidity":"2.25451530123", "windspeed":"0", "timestamp":"2016-05-12 22:15:16.569007", "temperature":"36" },
{ "humidity":"4.76577281229", "windspeed":"3", "timestamp":"2016-05-12 22:15:21.576566", "temperature":"42" },
{ "humidity":"0.358852693526", "windspeed":"1", "timestamp":"2016-05-12 22:15:26.583661", "temperature":"44" },
{ "humidity":"0.594251162092", "windspeed":"5", "timestamp":"2016-05-12 22:15:31.586231", "temperature":"36" },
{ "humidity":"3.70410673265", "windspeed":"4", "timestamp":"2016-05-12 22:15:36.589239", "temperature":"39" },
{ "humidity":"0.985981725869", "windspeed":"5", "timestamp":"2016-05-12 22:15:41.596224", "temperature":"38" },
{ "humidity":"4.20834753683", "windspeed":"0", "timestamp":"2016-05-12 22:15:46.600213", "temperature":"45" },
{ "humidity":"4.14573685004", "windspeed":"3", "timestamp":"2016-05-12 22:15:51.605628", "temperature":"36" },
{ "humidity":"2.80458121747", "windspeed":"5", "timestamp":"2016-05-12 22:15:56.608085", "temperature":"44" },
{ "humidity":"3.26427572812", "windspeed":"5", "timestamp":"2016-05-12 22:16:01.611923", "temperature":"45" },
{ "humidity":"3.61677578828", "windspeed":"0", "timestamp":"2016-05-12 22:16:06.618493", "temperature":"42" },
{ "humidity":"0.394267652678", "windspeed":"0", "timestamp":"2016-05-12 22:16:11.621162", "temperature":"41" },
{ "humidity":"2.70276479632", "windspeed":"2", "timestamp":"2016-05-12 22:16:16.626047", "temperature":"40" },
{ "humidity":"0.411084850112", "windspeed":"3", "timestamp":"2016-05-12 22:16:21.630472", "temperature":"36" },
{ "humidity":"1.81056024885", "windspeed":"4", "timestamp":"2016-05-12 22:16:26.636357", "temperature":"37" },
{ "humidity":"2.25408546317", "windspeed":"4", "timestamp":"2016-05-12 22:16:31.639191", "temperature":"40" },
{ "humidity":"1.1940926484", "windspeed":"5", "timestamp":"2016-05-12 22:16:36.644240", "temperature":"41" },
{ "humidity":"4.77517493933", "windspeed":"2", "timestamp":"2016-05-12 22:16:41.647749", "temperature":"43" },
{ "humidity":"3.05854303994", "windspeed":"2", "timestamp":"2016-05-12 22:16:46.649393", "temperature":"35" },
{ "humidity":"2.227230403", "windspeed":"5", "timestamp":"2016-05-12 22:16:51.652950", "temperature":"36" },
{ "humidity":"2.0920875399", "windspeed":"2", "timestamp":"2016-05-12 22:16:56.655896", "temperature":"42" },
{ "humidity":"0.317684812549", "windspeed":"3", "timestamp":"2016-05-12 22:17:01.660114", "temperature":"36" },
{ "humidity":"3.61838285076", "windspeed":"0", "timestamp":"2016-05-12 22:17:06.664108", "temperature":"38" },
{ "humidity":"3.30188537921", "windspeed":"2", "timestamp":"2016-05-12 22:17:11.666618", "temperature":"42" },
{ "humidity":"1.19580378113", "windspeed":"4", "timestamp":"2016-05-12 22:17:16.673449", "temperature":"44" },
{ "humidity":"1.48390111389", "windspeed":"5", "timestamp":"2016-05-12 22:17:21.676121", "temperature":"40" },
{ "humidity":"2.17072130368", "windspeed":"4", "timestamp":"2016-05-12 22:17:26.678824", "temperature":"44" },
{ "humidity":"2.91624485076", "windspeed":"5", "timestamp":"2016-05-12 22:17:31.685784", "temperature":"41" },
{ "humidity":"3.85944632174", "windspeed":"5", "timestamp":"2016-05-12 22:17:36.692890", "temperature":"43" },
{ "humidity":"3.2972457761", "windspeed":"2", "timestamp":"2016-05-12 22:17:41.697353", "temperature":"37" },
{ "humidity":"4.79520321499", "windspeed":"5", "timestamp":"2016-05-12 22:17:46.702844", "temperature":"37" },
{ "humidity":"2.74641431196", "windspeed":"4", "timestamp":"2016-05-12 22:17:51.705267", "temperature":"41" }]













2.74641431196,4,2016-05-12 22:17:51.705267,41
3.22570083564,5,2016-05-12 22:17:56.711248,37
2.32643115318,5,2016-05-12 22:18:01.716877,42
4.98622041066,5,2016-05-12 22:18:06.720261,38
2.90320651522,2,2016-05-12 22:18:11.725250,40
1.36438746207,1,2016-05-12 22:18:16.727457,41
4.35164277057,1,2016-05-12 22:18:21.729662,44
2.23844914868,0,2016-05-12 22:18:26.736369,37
3.204148779,5,2016-05-12 22:18:31.741733,38
0.778755855442,4,2016-05-12 22:18:36.746903,40
2.18762775593,5,2016-05-12 22:18:41.749746,35
2.34022692445,1,2016-05-12 22:18:46.754384,45
0.654409728911,3,2016-05-12 22:18:51.759980,39
2.59940414684,5,2016-05-12 22:18:56.764985,43
2.51003757397,4,2016-05-12 22:19:01.767424,40
4.2283639703,5,2016-05-12 22:19:06.770051,36
0.999877520304,3,2016-05-12 22:19:11.775356,38
3.36427824015,1,2016-05-12 22:19:16.779921,37
2.76474932239,2,2016-05-12 22:19:21.785105,40
0.903644086896,0,2016-05-12 22:19:26.789530,40
4.18910721388,4,2016-05-12 22:19:31.793019,38
1.83484115606,5,2016-05-12 22:19:36.794800,39
2.10481057558,1,2016-05-12 22:19:41.797968,38
4.90977548663,1,2016-05-12 22:19:46.804502,44
0.38905985619,5,2016-05-12 22:19:51.808781,45
2.64858900624,3,2016-05-12 22:19:56.814036,35
2.45501713651,4,2016-05-12 22:20:01.821054,37
1.70371104182,1,2016-05-12 22:20:06.823755,38
0.270849639926,4,2016-05-12 22:20:11.827779,41
0.00415335348831,5,2016-05-12 22:20:16.832587,43
2.88525312132,2,2016-05-12 22:20:21.838229,35
1.31545441042,1,2016-05-12 22:20:26.841282,42
2.61968977981,4,2016-05-12 22:20:31.844487,35
2.55103487352,0,2016-05-12 22:20:36.851241,43
0.740933164291,4,2016-05-12 22:20:41.855066,40
4.88144438071,2,2016-05-12 22:20:46.856710,39
2.24330827884,3,2016-05-12 22:20:51.860959,36
4.33551421003,3,2016-05-12 22:20:56.863422,41
3.04063384861,1,2016-05-12 22:21:01.867362,42
3.47167361113,4,2016-05-12 22:21:06.872406,40
1.62191772174,0,2016-05-12 22:21:11.874432,43
2.02134567408,4,2016-05-12 22:21:16.877655,36
4.94464401487,1,2016-05-12 22:21:21.880509,43
1.21065760636,1,2016-05-12 22:21:26.882927,40
3.8604438643,4,2016-05-12 22:21:31.884562,39
4.9196136402,3,2016-05-12 22:21:36.890261,38
0.287614130133,1,2016-05-12 22:21:41.895076,36
4.26787130374,0,2016-05-12 22:21:46.899452,45
4.72764769656,1,2016-05-12 22:21:51.902916,38
2.71794432998,2,2016-05-12 22:21:56.908134,36
3.15870859831,3,2016-05-12 22:22:01.910534,36
1.06538250066,0,2016-05-12 22:22:06.917933,39
4.16580332904,1,2016-05-12 22:22:11.920230,45
3.85330850974,3,2016-05-12 22:22:16.923745,40
4.63469106635,5,2016-05-12 22:22:21.928557,41
0.431294165572,3,2016-05-12 22:22:26.930465,43
4.99738132214,3,2016-05-12 22:22:31.936123,42
1.32096414868,3,2016-05-12 22:22:36.940553,41
4.88266546602,3,2016-05-12 22:22:41.945420,35
2.80792708692,1,2016-05-12 22:22:46.947928,45
1.73091112995,1,2016-05-12 22:22:51.951752,43
0.879015782333,4,2016-05-12 22:22:56.956958,41
4.96713188754,4,2016-05-12 22:23:01.959625,39
1.35944241227,2,2016-05-12 22:23:06.965360,41
1.71698887492,3,2016-05-12 22:23:11.971197,36
4.15300743526,2,2016-05-12 22:23:16.972605,45
1.17612187766,0,2016-05-12 22:23:21.977396,36
4.36932751543,3,2016-05-12 22:23:26.978828,43
3.59207754667,3,2016-05-12 22:23:31.984437,41
2.31800006193,3,2016-05-12 22:23:36.990685,40
2.63496373168,2,2016-05-12 22:23:41.993870,38
0.320707950162,1,2016-05-12 22:23:47.001525,37
2.52054289425,4,2016-05-12 22:23:52.007473,43
3.4475971635,3,2016-05-12 22:23:57.009402,37
1.8195943866,2,2016-05-12 22:24:02.012388,39
3.88266796107,2,2016-05-12 22:24:07.017075,35
1.50955875935,5,2016-05-12 22:24:12.025623,39
3.39311752582,5,2016-05-12 22:24:17.028431,41
3.1521474134,4,2016-05-12 22:24:22.032938,43
3.70561479008,2,2016-05-12 22:24:27.039728,36
2.14424001752,3,2016-05-12 22:24:32.043321,43
2.10891278492,3,2016-05-12 22:24:37.049498,45
1.07892345105,4,2016-05-12 22:24:42.052735,45
3.20206177745,5,2016-05-12 22:24:47.058092,43
4.59949804219,5,2016-05-12 22:24:52.061477,41
4.40825524523,3,2016-05-12 22:24:57.065274,38
1.83016409718,5,2016-05-12 22:25:02.067628,36
4.55834998972,5,2016-05-12 22:25:07.071214,41
1.41682644163,5,2016-05-12 22:25:12.076725,41
3.34279566097,1,2016-05-12 22:25:17.081862,41
3.34802111883,3,2016-05-12 22:25:22.086364,40
4.78852565717,4,2016-05-12 22:25:27.091455,36
4.70069060563,0,2016-05-12 22:25:32.094003,38
3.39257133237,3,2016-05-12 22:25:37.098052,43
3.07666064368,2,2016-05-12 22:25:42.104660,43
3.60285715088,4,2016-05-12 22:25:47.111777,41
4.00871265289,3,2016-05-12 22:25:52.114100,40
4.738907017,1,2016-05-12 22:25:57.118119,45
4.93529107997,4,2016-05-12 22:26:02.123893,36
2.86931657821,3,2016-05-12 22:26:07.130062,45
1.73208008364,5,2016-05-12 22:26:12.135969,37
3.14461414514,1,2016-05-12 22:26:17.140295,44
1.14431939928,3,2016-05-12 22:26:22.146183,35
1.73285728398,3,2016-05-12 22:26:27.148487,35
0.117328517048,5,2016-05-12 22:26:32.153095,42
4.02537034537,2,2016-05-12 22:26:37.156513,42
1.30921355933,2,2016-05-12 22:26:42.165348,39
1.43057025288,4,2016-05-12 22:26:47.169557,42
4.16427497414,2,2016-05-12 22:26:52.174611,40
3.64479845588,2,2016-05-12 22:26:57.179478,41
4.84579648935,2,2016-05-12 22:27:02.182872,40
2.51417162274,5,2016-05-12 22:27:07.188446,36
1.91319128968,0,2016-05-12 22:27:12.193655,35
2.37853185622,5,2016-05-12 22:27:17.200086,35
3.80372735728,0,2016-05-12 22:27:22.201600,40
3.16840482131,5,2016-05-12 22:27:27.206424,37
3.86269850139,0,2016-05-12 22:27:32.211994,37
2.64984720207,1,2016-05-12 22:27:37.217164,45
2.15749766409,1,2016-05-12 22:27:42.221236,44
3.36329302946,4,2016-05-12 22:27:47.226596,37
2.52743088472,3,2016-05-12 22:27:52.231763,38
0.279686391741,1,2016-05-12 22:27:57.235210,39
4.14463899582,1,2016-05-12 22:28:02.239052,36
3.1824168648,3,2016-05-12 22:28:07.243816,36
3.86070883393,5,2016-05-12 22:28:12.246782,37
3.43885712099,0,2016-05-12 22:29:22.570255,41
0.500074402641,0,2016-05-12 22:29:27.634421,35
1.84017903101,3,2016-05-12 22:29:32.639116,44
1.21411752782,5,2016-05-12 22:29:37.641594,36
2.43671220225,2,2016-05-12 22:29:42.645312,43
2.84090174486,4,2016-05-12 22:29:47.649397,42
0.388308402275,3,2016-05-12 22:29:52.651626,42
1.87996305386,1,2016-05-12 22:29:57.659008,42
3.14076515788,2,2016-05-12 22:30:02.663471,43
0.860659743802,2,2016-05-12 22:30:07.668842,39
1.94612821872,1,2016-05-12 22:30:12.674292,37
3.969653301,4,2016-05-12 22:30:17.677632,39
4.22207580803,4,2016-05-12 22:30:22.682352,35
4.16608206458,0,2016-05-12 22:30:27.688008,40
0.0646295054552,0,2016-05-12 22:30:32.691152,43
4.99672567106,4,2016-05-12 22:30:37.696279,42
2.40006723485,3,2016-05-12 22:30:42.702297,44
3.48466302869,5,2016-05-12 22:30:47.707220,37
1.70416867174,4,2016-05-12 22:30:52.714253,45
0.906722040023,4,2016-05-12 22:30:57.721742,44
4.16543637283,1,2016-05-12 22:31:02.726852,39
3.18970600314,2,2016-05-12 22:31:07.729625,44
3.72100166006,4,2016-05-12 22:31:12.736221,44
3.57018148144,0,2016-05-12 22:31:17.742235,36
3.63811834666,3,2016-05-12 22:31:22.746831,35
1.14462190919,3,2016-05-12 22:31:27.749178,45
4.56010855524,2,2016-05-12 22:31:32.756111,36
1.35416179785,3,2016-05-12 22:31:37.759878,43
0.958622050542,2,2016-05-12 22:31:42.767164,42
1.39382116074,4,2016-05-12 22:31:47.772559,38
3.78490263617,5,2016-05-12 22:31:52.775784,42
3.80355345512,2,2016-05-12 22:31:57.780630,40
2.75323945894,5,2016-05-12 22:32:02.785158,35
4.12578468159,5,2016-05-12 22:32:07.788718,41
1.21190131393,0,2016-05-12 22:32:12.793721,43
3.84105676856,0,2016-05-12 22:32:17.801086,41
3.67616980685,1,2016-05-12 22:32:22.805937,43
1.00267065007,2,2016-05-12 22:32:27.810282,41
2.51593187079,2,2016-05-12 22:32:32.816189,44
1.8832885893,0,2016-05-12 22:32:37.821245,39
2.41407857029,2,2016-05-12 22:32:42.825037,35
2.89687677139,5,2016-05-12 22:32:47.830965,44
3.38163278505,4,2016-05-12 22:32:52.836944,43
0.526502354596,4,2016-05-12 22:32:57.840298,42
3.6527913006,0,2016-05-12 22:33:02.844070,44
3.63638346305,2,2016-05-12 22:33:07.850270,39
4.96417677965,3,2016-05-12 22:33:12.853555,39
3.82792021204,4,2016-05-12 22:33:17.859760,41
4.94420806524,4,2016-05-12 22:33:22.864335,45
0.252712694136,0,2016-05-12 22:33:27.869497,37
2.73724944735,2,2016-05-12 22:33:32.873478,37
1.69748836874,0,2016-05-12 22:33:37.877487,38
0.640808514474,2,2016-05-12 22:33:42.883817,42
1.5643673418,4,2016-05-12 22:33:47.890716,44
3.69060286191,1,2016-05-12 22:33:52.894757,41
3.34490040794,2,2016-05-12 22:33:57.899584,43
3.33245335546,4,2016-05-12 22:34:02.902730,35
1.94192271196,3,2016-05-12 22:34:07.906378,40
2.45511006991,3,2016-05-12 22:34:12.910122,42
4.59203155276,2,2016-05-12 22:34:17.914626,36
0.880397556934,4,2016-05-12 22:34:22.920812,45
4.77816613084,0,2016-05-12 22:34:27.924829,44
4.79330068172,0,2016-05-12 22:34:32.931977,43
0.355974379983,5,2016-05-12 22:34:37.939000,40
1.06430085965,2,2016-05-12 22:34:42.945068,37
1.75576364594,2,2016-05-12 22:34:47.950054,45
4.73756393254,0,2016-05-12 22:34:52.956405,40
2.30338552334,1,2016-05-12 22:34:57.961650,44
3.66998448423,3,2016-05-12 22:35:02.965902,39
2.47194958049,3,2016-05-12 22:35:07.971987,45
3.61186723664,4,2016-05-12 22:35:12.978365,44
1.71502354923,2,2016-05-12 22:35:17.984259,43
2.50933218821,4,2016-05-12 22:35:22.986637,45
2.57666584318,4,2016-05-12 22:35:27.989485,43
0.0993899378533,1,2016-05-12 22:35:32.992824,35
1.78155370081,4,2016-05-12 22:35:37.999333,41
4.49038607751,0,2016-05-12 22:35:43.004678,39
0.766697428998,0,2016-05-12 22:35:48.010538,41
1.69764358975,2,2016-05-12 22:35:53.013993,39
4.06862635483,0,2016-05-12 22:35:58.018196,35
1.35921547009,1,2016-05-12 22:36:03.025259,35
3.56375191483,3,2016-05-12 22:36:08.028445,44
1.32631634287,0,2016-05-12 22:36:13.033054,40
3.68408583449,1,2016-05-12 22:36:18.041106,39
1.18260566611,3,2016-05-12 22:36:23.044318,43
1.63496173594,2,2016-05-12 22:36:28.048071,42
3.52320429888,3,2016-05-12 22:36:33.049837,38
4.72019928361,1,2016-05-12 22:36:38.057483,37
2.6014906795,1,2016-05-12 22:36:43.061167,43
3.19063188637,5,2016-05-12 22:36:48.066831,35
3.19063188637,5,2016-05-12 22:36:48.066831,35
1.24280635732,4,2016-05-12 22:36:53.071215,37
2.78503709663,0,2016-05-12 22:36:58.078398,43
2.3433687936,3,2016-05-12 22:37:03.080799,36
4.43515802293,2,2016-05-12 22:37:08.083744,38
1.54397757789,4,2016-05-12 22:37:13.088454,42
1.71479563379,5,2016-05-12 22:37:18.094658,39
2.31966344658,4,2016-05-12 22:37:23.100799,43
3.6153187063,3,2016-05-12 22:37:28.103511,36
3.56822848172,4,2016-05-12 22:37:33.108460,35
3.91877670105,3,2016-05-12 22:37:38.110727,38
4.52890536909,4,2016-05-12 22:37:43.113464,38
0.426661427124,0,2016-05-12 22:37:48.118249,40
3.94032100528,3,2016-05-12 22:37:53.122183,39
1.37304749354,0,2016-05-12 22:37:58.128112,36
4.74436431478,3,2016-05-12 22:38:03.132587,44
4.9320809023,1,2016-05-12 22:38:08.136054,41
2.09894254162,1,2016-05-12 22:38:13.142105,41
0.70029820826,2,2016-05-12 22:38:18.146602,36
0.033942146584,4,2016-05-12 22:38:23.151955,35
2.7571831864,0,2016-05-12 22:38:28.156164,42
1.454521561,1,2016-05-12 22:38:33.162144,45
2.70802552775,4,2016-05-12 22:38:38.165366,42
0.329984806383,5,2016-05-12 22:38:43.171878,35
3.18426256048,0,2016-05-12 22:38:48.177946,45
3.6116328386,3,2016-05-12 22:38:53.181517,44
4.01765811484,1,2016-05-12 22:38:58.184336,39
0.411721745846,3,2016-05-12 22:39:03.186211,43
2.04530145577,3,2016-05-12 22:39:08.189506,35
0.579644482746,1,2016-05-12 22:39:13.195176,44
1.20330705353,3,2016-05-12 22:39:18.201169,40
4.92373804552,4,2016-05-12 22:39:23.204256,39
4.40540070817,5,2016-05-12 22:39:28.210756,42
2.01164280557,3,2016-05-12 22:39:33.216224,35
0.67094853147,1,2016-05-12 22:39:38.218507,39
4.07474670489,0,2016-05-12 22:39:43.223252,44
3.170378574,4,2016-05-12 22:39:48.226524,39
0.477383271241,5,2016-05-12 22:39:53.229423,39
2.69320308078,3,2016-05-12 22:39:58.235113,40
1.91672879616,1,2016-05-12 22:40:03.238724,43
3.75120392732,2,2016-05-12 22:40:08.244008,36
1.66263999062,2,2016-05-12 22:40:13.247883,45
4.32214434926,0,2016-05-12 22:40:18.252126,39
0.181212664047,3,2016-05-12 22:40:23.257525,43
2.67051608279,0,2016-05-12 22:40:28.260130,38
1.8040320338,1,2016-05-12 22:40:33.262276,45
1.09556701006,4,2016-05-12 22:40:38.267769,43
2.99125635992,4,2016-05-12 22:40:43.274204,35
3.36387493615,3,2016-05-12 22:40:48.280414,39
0.681740838434,5,2016-05-12 22:40:53.284125,36
3.9868261436,1,2016-05-12 22:40:58.287782,39
0.204636267766,3,2016-05-12 22:41:03.296619,44
1.56065052278,4,2016-05-12 22:41:08.300419,37
3.34281888434,2,2016-05-12 22:41:13.302338,40
2.32371541119,4,2016-05-12 22:41:18.306929,37
1.77134437518,3,2016-05-12 22:41:23.313788,38
0.0901141163734,3,2016-05-12 22:41:28.318304,35
3.57289265832,0,2016-05-12 22:41:33.323362,45
1.10927143382,0,2016-05-12 22:41:38.332137,40
1.75230352038,0,2016-05-12 22:41:43.337767,38
1.92901211632,2,2016-05-12 22:41:48.344653,35
1.17771441479,2,2016-05-12 22:41:53.349513,41
4.23074862086,2,2016-05-12 22:41:58.355182,38
3.94782850734,3,2016-05-12 22:42:03.362863,41
2.8652073168,3,2016-05-12 22:42:08.374451,35
4.34042812206,3,2016-05-12 22:42:13.380027,36
2.68285193923,4,2016-05-12 22:42:18.385986,35
4.84254427219,5,2016-05-12 22:42:23.392369,36
1.99166265254,5,2016-05-12 22:42:28.395150,38
0.129009511269,2,2016-05-12 22:42:33.400482,44
2.80709878014,2,2016-05-12 22:42:38.407063,37
2.41852044338,0,2016-05-12 22:42:43.409493,39
2.19779991186,5,2016-05-12 22:42:48.416174,42
2.93253875274,3,2016-05-12 22:42:53.422524,41
0.04817714324,5,2016-05-12 22:42:58.425686,44
3.42124421482,2,2016-05-12 22:43:03.428595,37
1.45240392722,3,2016-05-12 22:43:08.432097,35
0.400130397059,5,2016-05-12 22:43:13.434230,44
3.05300891032,3,2016-05-12 22:43:18.439480,39
4.74192085905,4,2016-05-12 22:43:23.441937,44
2.7422143383,5,2016-05-12 22:43:28.447637,35
1.75271086806,1,2016-05-12 22:43:33.454119,39
2.05506376979,0,2016-05-12 22:43:38.457643,37
4.7915348354,5,2016-05-12 22:43:43.460595,35
4.67674507546,0,2016-05-12 22:43:48.463807,37
0.822838799233,0,2016-05-12 22:43:53.468913,45
0.265527152075,0,2016-05-12 22:43:58.471929,42
2.78062443267,2,2016-05-12 22:44:03.477551,35
0.85628891674,0,2016-05-12 22:44:08.484111,37
1.6698012372,1,2016-05-12 22:44:13.487995,42
1.06426867249,1,2016-05-12 22:44:18.494305,35
1.67822072471,4,2016-05-12 22:44:23.497796,37
2.76393711899,0,2016-05-12 22:44:28.504381,42
2.16957305562,0,2016-05-12 22:44:33.506828,41
4.54911151843,4,2016-05-12 22:44:38.508519,40
0.887218617507,4,2016-05-12 22:44:43.515279,38
2.96518418152,5,2016-05-12 22:44:48.520617,42
0.0862171581131,2,2016-05-12 22:44:53.523204,39
2.868209004,5,2016-05-12 22:44:58.528090,35
0.403239830825,5,2016-05-12 22:45:03.534013,39
3.36587671313,2,2016-05-12 22:45:08.536870,36
4.52742874042,0,2016-05-12 22:45:13.541182,43
3.59203177561,5,2016-05-12 22:45:18.545919,45
1.47116526693,3,2016-05-12 22:45:23.549239,35
3.77570800157,3,2016-05-12 22:45:28.552999,35
4.6368817073,4,2016-05-12 22:45:33.555697,43
0.269524675109,1,2016-05-12 22:45:38.563251,38
0.176850416622,0,2016-05-12 22:45:43.568632,41
0.134414697335,1,2016-05-12 22:45:48.574061,44
0.0295285498014,4,2016-05-12 22:45:53.575849,41
1.05354555281,1,2016-05-12 22:45:58.581887,37
2.83921951276,1,2016-05-12 22:46:03.587384,35
2.33392724046,5,2016-05-12 22:46:08.591845,40
0.287812117155,2,2016-05-12 22:46:13.595739,39
4.98598178792,3,2016-05-12 22:46:18.599422,43
0.878040164709,0,2016-05-12 22:46:23.605708,38
2.44573055331,2,2016-05-12 22:46:28.607593,35
3.38334436159,0,2016-05-12 22:46:33.610899,35
0.503234830714,3,2016-05-12 22:46:38.613770,42
4.58639101096,3,2016-05-12 22:46:43.621973,45
1.95808065446,5,2016-05-12 22:46:48.624784,44
0.84486346772,5,2016-05-12 22:46:53.628787,42
4.2454511865,5,2016-05-12 22:46:58.633180,37
0.184667191045,3,2016-05-12 22:47:03.636459,37
4.00442871756,1,2016-05-12 22:47:08.642203,45
4.05185337508,4,2016-05-12 22:47:13.647378,38
4.81408940126,5,2016-05-12 22:47:18.652775,45
0.966945799444,1,2016-05-12 22:47:23.655042,37
3.17573209567,4,2016-05-12 22:47:28.662232,37
3.5507639044,2,2016-05-12 22:47:33.665486,45
2.59852358379,1,2016-05-12 22:47:38.671065,40
1.88745494762,2,2016-05-12 22:47:43.673485,37
2.44330989072,2,2016-05-12 22:47:48.679965,41
4.96460563237,2,2016-05-12 22:47:53.683163,42
1.35143519948,5,2016-05-12 22:47:58.690725,40
2.24802890623,2,2016-05-12 22:48:03.697401,38
2.98657233406,0,2016-05-12 22:48:08.702376,35
3.66009193818,0,2016-05-12 22:48:13.709897,44
3.07098675957,0,2016-05-12 22:48:18.714386,36
2.40933782006,2,2016-05-12 22:48:23.720727,43
0.640072929201,0,2016-05-12 22:48:28.728251,43
2.50470290338,4,2016-05-12 22:48:33.731923,35
1.18098754057,1,2016-05-12 22:48:38.733604,37
2.15058972341,2,2016-05-12 22:48:43.739450,44
3.19976808179,3,2016-05-12 22:48:48.742998,35
4.48400810751,5,2016-05-12 22:48:53.748165,37
4.95549951575,3,2016-05-12 22:48:58.752480,44
3.55622190901,0,2016-05-12 22:49:03.757942,36
1.9042854149,1,2016-05-12 22:49:08.760364,42
1.31334804507,4,2016-05-12 22:49:13.764038,44
3.76981716426,0,2016-05-12 22:49:18.767740,38
3.41884178617,1,2016-05-12 22:49:23.771007,43
1.34767276875,1,2016-05-12 22:49:28.773120,35
4.34514201657,1,2016-05-12 22:49:33.777470,41
2.60323132868,3,2016-05-12 22:49:38.780216,45
2.63263877237,1,2016-05-12 22:49:43.784512,39
1.32652021849,4,2016-05-12 22:49:48.789399,40
1.67858531676,4,2016-05-12 22:49:53.791162,39
1.36992976215,2,2016-05-12 22:49:58.795512,41
2.8200387855,5,2016-05-12 22:50:03.801219,45
2.67956710331,5,2016-05-12 22:50:08.807381,41
4.76776924689,3,2016-05-12 22:50:13.812737,43
1.60248552788,5,2016-05-12 22:50:18.818008,42
3.23867196732,2,2016-05-12 22:50:23.824696,43
2.90375612422,1,2016-05-12 22:50:28.827994,44
2.55748241177,3,2016-05-12 22:50:33.834174,43
0.501223239297,1,2016-05-12 22:50:38.837749,42
4.73664926914,3,2016-05-12 22:50:43.840246,45
0.577902394532,2,2016-05-12 22:50:48.845382,43
0.854834869139,1,2016-05-12 22:50:53.850330,42
1.51271074588,5,2016-05-12 22:50:58.855999,38
1.30103688667,0,2016-05-12 22:51:03.860068,42
3.35388773566,0,2016-05-12 22:51:08.861565,41
0.129085276223,3,2016-05-12 22:51:13.866157,35
2.2497296594,4,2016-05-12 22:51:18.871315,42
1.98925565437,2,2016-05-12 22:51:23.875973,35
3.16884880108,2,2016-05-12 22:51:28.880701,40
3.74659121635,1,2016-05-12 22:51:33.885631,36
2.52077162066,5,2016-05-12 22:51:38.888346,44
3.32908256866,2,2016-05-12 22:51:43.894078,40
1.22715053803,3,2016-05-12 22:51:48.898715,40
1.88703673102,0,2016-05-12 22:51:53.903139,45
3.5596911878,5,2016-05-12 22:51:58.908355,42
0.49942731307,5,2016-05-12 22:52:03.915005,40
4.8302920129,0,2016-05-12 22:52:08.920884,40
4.75342627875,1,2016-05-12 22:52:13.925659,35
1.88363967754,1,2016-05-12 22:52:18.928389,43
3.55491683749,5,2016-05-12 22:52:23.934532,36
1.58918143942,5,2016-05-12 22:52:28.941449,42
4.87280574691,4,2016-05-12 22:52:33.946971,35
4.50892661664,5,2016-05-12 22:52:38.953655,36
0.654915796093,4,2016-05-12 22:52:43.958218,42
3.84503150228,4,2016-05-12 22:52:48.964494,40
3.24868787846,0,2016-05-12 22:52:53.966716,35
3.26234293142,0,2016-05-12 22:52:58.973820,42
4.97576075237,3,2016-05-12 22:53:03.980545,42
3.37547628054,1,2016-05-12 22:53:08.984540,42
0.10470684146,0,2016-05-12 22:53:13.991882,38
4.76825900807,5,2016-05-12 22:53:18.997137,41
1.41800426951,3,2016-05-12 22:53:24.001352,45
0.153748795795,1,2016-05-12 22:53:29.007973,45
2.11580050008,2,2016-05-12 22:53:34.011617,43
4.98683911846,4,2016-05-12 22:53:39.016446,43
4.8394046815,5,2016-05-12 22:53:44.023031,40
3.52587679193,0,2016-05-12 22:53:49.025379,45
2.12974790803,5,2016-05-12 22:53:54.030071,44
0.689216665848,5,2016-05-12 22:53:59.035356,44
1.91178361858,2,2016-05-12 22:54:04.040689,43
2.40845850685,2,2016-05-12 22:54:09.045607,45
3.64963982986,3,2016-05-12 22:54:14.051707,43
2.05516063884,5,2016-05-12 22:54:19.056097,45
4.41623185966,3,2016-05-12 22:54:24.060405,39
0.436423379851,4,2016-05-12 22:54:29.064220,36
2.63551803943,0,2016-05-12 22:54:34.067056,45
0.990918264435,4,2016-05-12 22:54:39.073274,43
4.25893735137,5,2016-05-12 22:54:44.076441,43
1.02556200927,3,2016-05-12 22:54:49.081528,40
4.0500773017,3,2016-05-12 22:54:54.084229,36
1.19693444457,3,2016-05-12 22:54:59.086362,45
2.9829214666,5,2016-05-12 22:55:04.092604,43
4.32323063112,2,2016-05-12 22:55:09.099250,42
0.922057562896,3,2016-05-12 22:55:14.103842,36
4.84358217866,5,2016-05-12 22:55:19.109279,35
4.31502915044,5,2016-05-12 22:55:24.112370,38
0.985444684192,1,2016-05-12 22:55:29.118658,42
1.61628857774,3,2016-05-12 22:55:34.122958,43
2.16432541403,3,2016-05-12 22:55:39.126939,42
3.75523887085,5,2016-05-12 22:55:44.130901,39
1.05068476382,2,2016-05-12 22:55:49.138159,44
1.31207285702,0,2016-05-12 22:55:54.142852,43
0.762735110561,0,2016-05-12 22:55:59.148038,44
1.01953444861,0,2016-05-12 22:56:04.151604,39
2.22635495897,4,2016-05-12 22:56:09.154155,38
3.15289887585,4,2016-05-12 22:56:14.157249,45
3.52568045978,5,2016-05-12 22:56:19.160095,39
4.99631123789,3,2016-05-12 22:56:24.166226,39
2.64470849158,1,2016-05-12 22:56:29.170484,35
0.121496093549,2,2016-05-12 22:56:34.174400,43
4.36321172479,5,2016-05-12 22:56:39.178835,45
2.64600286258,1,2016-05-12 22:56:44.181861,36
4.10259374884,3,2016-05-12 22:56:49.186673,43
4.95951166431,5,2016-05-12 22:56:54.192383,37
0.84587147879,5,2016-05-12 22:56:59.199000,36
2.97090278805,3,2016-05-12 22:57:04.202646,45
3.91856315774,2,2016-05-12 22:57:09.207024,45
1.87689152464,0,2016-05-12 22:57:14.210271,44
2.32323707052,1,2016-05-12 22:57:19.213802,35
4.80098246351,3,2016-05-12 22:57:24.218880,36
4.11899089189,4,2016-05-12 22:57:29.222271,36
1.39263419075,3,2016-05-12 22:57:34.226738,42
0.803189982093,2,2016-05-12 22:57:39.231857,39
0.244683122858,3,2016-05-12 22:57:44.237978,41
4.36581659187,4,2016-05-12 22:57:49.245243,40
4.5948689077,4,2016-05-12 22:57:54.248229,40
3.36614088821,1,2016-05-12 22:57:59.251897,38
3.09581250867,3,2016-05-12 22:58:04.258427,43
4.86569194144,4,2016-05-12 22:58:09.265198,44
2.72635980921,0,2016-05-12 22:58:14.268203,36
4.31197219809,2,2016-05-12 22:58:19.271097,36
4.87484297609,0,2016-05-12 22:58:24.274531,39
3.52878957943,4,2016-05-12 22:58:29.278172,43
0.773853158842,4,2016-05-12 22:58:34.280697,36
4.31325701492,4,2016-05-12 22:58:39.283784,39
0.259793041477,5,2016-05-12 22:58:44.287968,37
1.18795127083,5,2016-05-12 22:58:49.292227,36
3.9946181007,2,2016-05-12 22:58:54.294111,37
1.19707767595,1,2016-05-12 22:58:59.297664,41
3.70700924552,2,2016-05-12 22:59:04.300216,41
4.69659760127,4,2016-05-12 22:59:09.305610,39
2.59733597236,3,2016-05-12 22:59:14.307870,38
4.87685711141,4,2016-05-12 22:59:19.312643,35
3.37296978333,4,2016-05-12 22:59:24.316584,36
2.38408320642,2,2016-05-12 22:59:29.318698,40
0.728648351662,5,2016-05-12 22:59:34.325045,43
4.91675123011,2,2016-05-12 22:59:39.327106,38
2.39711250856,4,2016-05-12 22:59:44.329719,44
4.36286057178,5,2016-05-12 22:59:49.336539,39
3.25919779583,4,2016-05-12 22:59:54.342785,39
2.73062267558,1,2016-05-12 22:59:59.345564,42
2.957658161,2,2016-05-12 23:00:04.348136,36
1.28577641674,4,2016-05-12 23:00:09.349364,39
0.873854280785,0,2016-05-12 23:00:14.355365,37
0.129590064257,3,2016-05-12 23:00:19.361497,43
0.553990696424,3,2016-05-12 23:00:24.364905,41
0.420190408361,4,2016-05-12 23:00:29.366656,38
1.11938867536,3,2016-05-12 23:00:34.370845,45
4.09361685715,0,2016-05-12 23:00:39.377052,40
0.533766616319,5,2016-05-12 23:00:44.382157,42
2.3136591598,5,2016-05-12 23:00:49.384522,42
3.08536185435,3,2016-05-12 23:00:54.388611,45
3.88283043333,1,2016-05-12 23:00:59.392868,40
4.40446152009,1,2016-05-12 23:01:04.396836,43
4.02392126855,0,2016-05-12 23:01:09.401883,36
0.469577032174,3,2016-05-12 23:01:14.405071,42
0.849909244063,5,2016-05-12 23:01:19.406559,38
4.4926211625,2,2016-05-12 23:01:24.411998,37
2.45369416909,2,2016-05-12 23:01:29.419302,38
1.2082115062,3,2016-05-12 23:01:34.425550,40
4.77485832001,3,2016-05-12 23:01:39.430415,40
1.0892739182,1,2016-05-12 23:01:44.435226,43
0.210226611922,3,2016-05-12 23:01:49.442041,41
0.522041496865,4,2016-05-12 23:01:54.446791,38
4.86339975124,1,2016-05-12 23:01:59.451005,45
0.665697267233,2,2016-05-12 23:02:04.453509,43
3.37254377667,5,2016-05-12 23:02:09.458263,40
0.625657144423,4,2016-05-12 23:02:14.463114,38
1.26277996064,0,2016-05-12 23:02:19.469039,44
3.60168168163,4,2016-05-12 23:02:24.473740,40
2.49061068319,0,2016-05-12 23:02:29.479732,36
0.831253611735,2,2016-05-12 23:02:34.483355,43
2.72861867764,5,2016-05-12 23:02:39.485114,39
0.550157097041,1,2016-05-12 23:02:44.490909,45
3.22335782544,5,2016-05-12 23:02:49.494007,40
3.18606115567,4,2016-05-12 23:02:54.498983,36
4.98960253162,1,2016-05-12 23:02:59.500343,35
4.83661388733,2,2016-05-12 23:03:04.505063,35
0.689840924585,1,2016-05-12 23:03:09.511185,43
4.54987790829,5,2016-05-12 23:03:14.517166,42
3.10742810162,4,2016-05-12 23:03:19.522188,38
2.84765749418,2,2016-05-12 23:03:24.527407,43
2.97202414236,0,2016-05-12 23:03:29.531653,42
3.06630020192,5,2016-05-12 23:03:34.538266,40
4.63273716854,2,2016-05-12 23:03:39.543524,37
1.48205050464,1,2016-05-12 23:03:44.550178,43
0.284434773221,4,2016-05-12 23:03:49.554680,36
0.677302082483,2,2016-05-12 23:03:54.559053,35
2.66085809638,4,2016-05-12 23:03:59.564503,44
1.7276659777,4,2016-05-12 23:04:04.569970,45
1.24760936413,5,2016-05-12 23:04:09.574202,43
4.78923252169,3,2016-05-12 23:04:14.578920,43
2.60418098669,5,2016-05-12 23:04:19.583143,43
2.18172230302,2,2016-05-12 23:04:24.590201,44
0.260402173295,1,2016-05-12 23:04:29.596853,40
3.60564772841,0,2016-05-12 23:04:34.603649,45
1.25900711268,3,2016-05-12 23:04:39.608932,40
2.47374067348,3,2016-05-12 23:04:44.614083,37
3.0737535763,5,2016-05-12 23:04:49.618154,45
0.40422799596,3,2016-05-12 23:04:54.623487,35
3.63723316831,3,2016-05-12 23:04:59.627319,43
4.3339251045,1,2016-05-12 23:05:04.633341,44
0.545176937433,4,2016-05-12 23:05:09.638813,41
4.43830964713,5,2016-05-12 23:05:14.643563,39
3.90879108779,3,2016-05-12 23:05:19.648896,45
2.91129964748,5,2016-05-12 23:05:24.655091,37
0.343814887664,3,2016-05-12 23:05:29.660740,42
1.22760619428,4,2016-05-12 23:05:34.665430,40
0.922274629632,5,2016-05-12 23:05:39.671154,43
4.59712465047,0,2016-05-12 23:05:44.678495,43
1.09736751708,3,2016-05-12 23:05:49.680762,41
0.727841843294,4,2016-05-12 23:05:54.684708,40
1.58799381365,0,2016-05-12 23:05:59.690350,36
0.140527523897,4,2016-05-12 23:06:04.692145,44
4.36586832183,5,2016-05-12 23:06:09.697869,39
0.369807043247,3,2016-05-12 23:06:14.701330,41
4.3027730778,1,2016-05-12 23:06:19.706232,36
2.16995407314,5,2016-05-12 23:06:24.710950,40
2.73243212153,2,2016-05-12 23:06:29.715775,40
2.48880241811,3,2016-05-12 23:06:34.722138,42
0.68260278522,2,2016-05-12 23:06:39.727344,41
0.0942062516599,0,2016-05-12 23:06:44.733356,36
1.37310409681,1,2016-05-12 23:06:49.739139,42
2.7588411158,2,2016-05-12 23:06:54.740352,41
2.71379770782,2,2016-05-12 23:06:59.745216,43
3.44305725253,3,2016-05-12 23:07:04.748821,38
1.7086907626,2,2016-05-12 23:07:09.754690,41
2.47282931838,4,2016-05-12 23:07:14.760669,45
1.57999937377,2,2016-05-12 23:07:19.766746,42
3.8879271383,5,2016-05-12 23:07:24.768985,37
3.75631365221,1,2016-05-12 23:07:29.775066,45
2.32885024769,2,2016-05-12 23:07:34.778732,44
4.14720325739,5,2016-05-12 23:07:39.782762,35
4.11148038921,3,2016-05-12 23:07:44.784592,41
4.62566493659,1,2016-05-12 23:07:49.787711,35
2.53211066913,4,2016-05-12 23:07:54.790628,42
0.970850292453,0,2016-05-12 23:07:59.794676,41
0.430155539025,1,2016-05-12 23:08:04.800387,35
2.84641131386,3,2016-05-12 23:08:09.804471,41
1.45776144371,2,2016-05-12 23:08:14.811347,42
3.99749824959,0,2016-05-12 23:08:19.816988,40
2.43346804654,0,2016-05-12 23:08:24.822552,45
4.83614709942,4,2016-05-12 23:08:29.827371,36
1.95763207947,0,2016-05-12 23:08:34.832684,38
2.2541112223,2,2016-05-12 23:08:39.837459,35
0.322091528117,0,2016-05-12 23:08:44.839530,39
4.20546240191,4,2016-05-12 23:08:49.846156,42
3.82252053851,0,2016-05-12 23:08:54.850956,41
0.946343734674,4,2016-05-12 23:08:59.856272,43
3.28584308498,5,2016-05-12 23:09:04.858089,39
1.11114684054,1,2016-05-12 23:09:09.864267,38
2.81700253597,4,2016-05-12 23:09:14.869891,38
3.25899834324,3,2016-05-12 23:09:19.875473,37
2.75420897836,5,2016-05-12 23:09:24.877452,43
1.41367120646,5,2016-05-12 23:09:29.883519,43
3.26208038922,2,2016-05-12 23:09:34.886856,36
4.87459964463,0,2016-05-12 23:09:39.890386,36
0.77449078286,0,2016-05-12 23:09:44.896234,35
3.59393283599,1,2016-05-12 23:09:49.901527,38
0.0982725195535,2,2016-05-12 23:09:54.905522,43
2.20408683202,4,2016-05-12 23:09:59.910475,43
4.77111885644,5,2016-05-12 23:10:04.915284,44
3.38849178748,0,2016-05-12 23:10:09.916871,37
0.349977633705,0,2016-05-12 23:10:14.920403,41
3.79190191462,1,2016-05-12 23:10:19.925800,45
3.14763285327,1,2016-05-12 23:10:24.931384,38
0.277760564234,5,2016-05-12 23:10:29.933877,40
1.45305351409,5,2016-05-12 23:10:34.936873,44
2.80168093274,4,2016-05-12 23:10:39.939995,36
4.39523708047,1,2016-05-12 23:10:44.944863,45
0.274018531464,4,2016-05-12 23:10:49.950060,43
1.78991742784,2,2016-05-12 23:10:54.954575,40
2.51029784976,0,2016-05-12 23:10:59.959788,36
4.13858463508,2,2016-05-12 23:11:04.966258,38
0.597830790747,0,2016-05-12 23:11:09.971249,37
2.28057476089,2,2016-05-12 23:11:14.973210,42
0.166943322485,0,2016-05-12 23:11:19.976697,35
4.17560016205,1,2016-05-12 23:11:24.982586,36
2.34234565724,1,2016-05-12 23:11:29.984745,38
4.05635214423,2,2016-05-12 23:11:34.990435,41
0.0519895360147,3,2016-05-12 23:11:39.992984,36
1.00546091025,0,2016-05-12 23:11:44.998850,35
1.56964061622,3,2016-05-12 23:11:50.003062,45
2.12306139651,2,2016-05-12 23:11:55.005383,45
2.93571592769,5,2016-05-12 23:12:00.008064,41
4.63452331068,2,2016-05-12 23:12:05.011179,39
1.97988596065,0,2016-05-12 23:12:10.015412,37
3.64246500454,4,2016-05-12 23:12:15.018172,37
3.38205003844,5,2016-05-12 23:12:20.023130,44
2.7131423413,5,2016-05-12 23:12:25.026872,39
1.64658585307,0,2016-05-12 23:12:30.031079,42
4.55962446389,2,2016-05-12 23:12:35.038015,36
3.33779344854,1,2016-05-12 23:12:40.042013,35
2.68968098641,4,2016-05-12 23:12:45.048275,39
4.40047398286,0,2016-05-12 23:12:50.051952,40
2.57036670761,2,2016-05-12 23:12:55.058296,38
2.54395941947,2,2016-05-12 23:13:00.062026,44
2.93563121665,2,2016-05-12 23:13:05.066378,36
1.88190522566,2,2016-05-12 23:13:10.069718,41
2.28650594113,5,2016-05-12 23:13:15.075863,35
4.64569280161,3,2016-05-12 23:13:20.079179,38
4.3238741307,4,2016-05-12 23:13:25.082340,45
4.50244601988,1,2016-05-12 23:13:30.088496,38
0.449692058174,5,2016-05-12 23:13:35.094870,44
1.09833778386,5,2016-05-12 23:13:40.100669,37
4.16481106969,4,2016-05-12 23:13:45.107525,44
4.96359715168,3,2016-05-12 23:13:50.112488,43
2.24610836992,5,2016-05-12 23:13:55.115637,43
3.44666824718,0,2016-05-12 23:14:00.120341,41
2.85268237655,4,2016-05-12 23:14:05.126815,45
2.16570430822,5,2016-05-12 23:14:10.133676,43
1.5547742588,2,2016-05-12 23:14:15.138356,35
3.16872887672,0,2016-05-12 23:14:20.140473,43
0.395063247957,4,2016-05-12 23:14:25.144988,40
4.86414944891,5,2016-05-12 23:14:30.150188,42
3.16904718668,0,2016-05-12 23:14:35.155058,43
0.11810640159,5,2016-05-12 23:14:40.158881,39
0.858424182154,4,2016-05-12 23:14:45.165525,44
3.24341666459,1,2016-05-12 23:14:50.169091,37
1.00085096496,5,2016-05-12 23:14:55.172941,42
2.8933045858,5,2016-05-12 23:15:00.177256,35
4.48627720998,5,2016-05-12 23:15:05.179513,38
2.1129593107,2,2016-05-12 23:15:10.183013,38
2.07301930463,0,2016-05-12 23:15:15.188043,37
4.67923857144,0,2016-05-12 23:15:20.193043,43
1.96113750447,4,2016-05-12 23:15:25.197037,38
0.158428933673,1,2016-05-12 23:15:30.201342,40
3.35177542584,4,2016-05-12 23:15:35.207633,41
3.66179578572,1,2016-05-12 23:15:40.209723,36
1.45527261188,3,2016-05-12 23:15:45.213123,41
1.98041095998,0,2016-05-12 23:15:50.218093,36
0.2101067405,1,2016-05-12 23:15:55.224531,43
1.4378055279,0,2016-05-12 23:16:00.230659,40
3.47768123927,4,2016-05-12 23:16:05.236950,38
2.52278855481,0,2016-05-12 23:16:10.241717,35
2.11320101531,3,2016-05-12 23:16:15.246557,44
0.467704891249,5,2016-05-12 23:16:20.251693,41
3.90144473261,1,2016-05-12 23:16:25.256833,38
4.55169458967,3,2016-05-12 23:16:30.263235,37
2.34771738964,1,2016-05-12 23:16:35.269864,37
0.127188592677,2,2016-05-12 23:16:40.274442,42
3.11784849015,0,2016-05-12 23:16:45.280821,42
1.61619879558,5,2016-05-12 23:16:50.284687,39
2.94859789834,3,2016-05-12 23:16:55.291104,44
1.38637806414,0,2016-05-12 23:17:00.296768,35
0.319885158824,5,2016-05-12 23:17:05.302113,45
4.81811801821,1,2016-05-12 23:17:10.307415,38
0.889273008946,4,2016-05-12 23:17:15.315314,42
3.2001364813,0,2016-05-12 23:17:20.322268,42
2.96907608471,4,2016-05-12 23:17:25.327175,45
0.379685540304,2,2016-05-12 23:17:30.332376,40
2.35349211435,1,2016-05-12 23:17:35.334828,45
1.39062527944,5,2016-05-12 23:17:40.339997,40
2.2665787911,3,2016-05-12 23:17:45.343252,36
1.15380236929,4,2016-05-12 23:17:50.349941,43
4.46959990826,0,2016-05-12 23:17:55.356097,38
3.36427166415,3,2016-05-12 23:18:00.364686,41
1.92256042269,1,2016-05-12 23:18:05.370051,39
4.84067024446,0,2016-05-12 23:18:10.373603,43
4.82961903043,3,2016-05-12 23:18:15.376805,42
3.08957256462,5,2016-05-12 23:18:20.381932,38
3.17379945313,3,2016-05-12 23:18:25.385618,40
0.226140540416,0,2016-05-12 23:18:30.388852,36
0.932562341397,3,2016-05-12 23:18:35.391896,42
4.98744307837,5,2016-05-12 23:18:40.396739,44
3.8436034336,4,2016-05-12 23:18:45.401921,41
1.83243714458,0,2016-05-12 23:18:50.405955,35
2.03428021331,2,2016-05-12 23:18:55.411002,40
0.188127318142,5,2016-05-12 23:19:00.416136,38
0.202802143967,1,2016-05-12 23:19:05.421355,36
2.37001141778,5,2016-05-12 23:19:10.423971,44
2.76011764694,0,2016-05-12 23:19:15.430038,39
2.51073707191,1,2016-05-12 23:19:20.447531,42
4.34015324913,3,2016-05-12 23:19:25.451171,45
1.94442882642,1,2016-05-12 23:19:30.455287,39
3.33577116068,5,2016-05-12 23:19:35.459651,40
0.326539116581,3,2016-05-12 23:19:40.462246,35
4.08063399986,0,2016-05-12 23:19:45.467462,39
3.32091978548,1,2016-05-12 23:19:50.473626,40
2.05794216757,0,2016-05-12 23:19:55.476024,42
3.49321695041,5,2016-05-12 23:20:00.479282,45
1.97732807122,5,2016-05-12 23:20:05.486003,38
1.75377643745,4,2016-05-12 23:20:10.493705,40
0.146107111363,5,2016-05-12 23:20:15.501143,44
1.69527335319,0,2016-05-12 23:20:20.507026,39
3.14654780618,2,2016-05-12 23:20:25.510344,37
2.69875009767,1,2016-05-12 23:20:30.512063,41
4.89841779806,0,2016-05-12 23:20:35.516706,41
2.73737596068,5,2016-05-12 23:20:40.519045,39
1.04996513146,1,2016-05-12 23:20:45.530240,37
1.54384793923,5,2016-05-12 23:20:50.535040,40
4.69276301398,2,2016-05-12 23:20:55.538122,37
1.28260324751,4,2016-05-12 23:21:00.540514,39
0.214692709729,0,2016-05-12 23:21:05.546465,36
3.60500952972,3,2016-05-12 23:21:10.550397,40
3.35125336255,2,2016-05-12 23:21:15.558257,45
1.14005854516,2,2016-05-12 23:21:20.565669,38
2.89386584298,2,2016-05-12 23:21:25.569551,39
1.51071024023,1,2016-05-12 23:21:30.575891,37
4.64473617833,3,2016-05-12 23:21:35.578220,40
1.62914997718,5,2016-05-12 23:21:40.582651,42
4.39361932136,2,2016-05-12 23:21:45.587044,35
3.04093273225,2,2016-05-12 23:21:50.594122,44
2.28507937595,5,2016-05-12 23:21:55.599544,43
4.42778666814,4,2016-05-12 23:22:00.602468,36
2.97238294687,3,2016-05-12 23:22:05.607423,38
0.160163504513,4,2016-05-12 23:22:10.611660,42
4.53804720886,4,2016-05-12 23:22:15.615128,36
3.78157885905,3,2016-05-12 23:22:20.618513,43
4.48702446425,2,2016-05-12 23:22:25.622965,36
0.480735136388,5,2016-05-12 23:22:30.627424,40
4.04745339983,4,2016-05-12 23:22:35.631882,43
0.59492877537,3,2016-05-12 23:22:40.637506,42
1.45216597362,5,2016-05-12 23:22:45.642541,41
3.19305503135,1,2016-05-12 23:22:50.645816,42
1.81751611776,4,2016-05-12 23:22:55.648197,38
1.72478285329,2,2016-05-12 23:23:00.653650,38
2.35485492514,5,2016-05-12 23:23:05.660443,43
3.3462458538,1,2016-05-12 23:23:10.665262,43
1.33658905952,5,2016-05-12 23:23:15.669029,35
1.7999872167,1,2016-05-12 23:23:20.673888,35
1.11357030484,5,2016-05-12 23:23:25.676137,42
3.20472913863,5,2016-05-12 23:23:30.681268,44
1.41420971829,3,2016-05-12 23:23:35.686840,42
2.57606103306,0,2016-05-12 23:23:40.692246,44
3.98957973016,0,2016-05-12 23:23:45.695678,44
2.88995132206,5,2016-05-12 23:23:50.700267,36
1.01587552333,3,2016-05-12 23:23:55.703618,42
2.38031045447,4,2016-05-12 23:24:00.707746,44
3.09748496964,2,2016-05-12 23:24:05.713835,38
0.470170026386,3,2016-05-12 23:24:10.715399,35
2.4477880035,3,2016-05-12 23:24:15.716908,41
4.14647424701,3,2016-05-12 23:24:20.723312,42
0.42533760739,3,2016-05-12 23:24:25.727360,43
3.87883892864,0,2016-05-12 23:24:30.732159,44
2.65653980583,2,2016-05-12 23:24:35.736397,41
2.67764215096,2,2016-05-12 23:24:40.738943,36
1.39725190648,3,2016-05-12 23:24:45.744529,40
3.62347567048,5,2016-05-12 23:24:50.750175,42
3.64880967654,5,2016-05-12 23:24:55.752630,45
1.93557410481,2,2016-05-12 23:25:00.760351,39
0.464490793705,0,2016-05-12 23:25:05.762504,45
3.48565292944,1,2016-05-12 23:25:10.769132,37
4.89536967781,4,2016-05-12 23:25:15.774611,45
1.97754884863,2,2016-05-12 23:25:20.778667,41
0.315259316158,2,2016-05-12 23:25:25.783053,41
2.66702606242,2,2016-05-12 23:25:30.787249,42
3.61401783073,4,2016-05-12 23:25:35.792324,43
3.45899612582,3,2016-05-12 23:25:40.799210,43
4.35282626851,5,2016-05-12 23:25:45.801306,42
3.11931236559,0,2016-05-12 23:25:50.803418,36
2.42932869187,5,2016-05-12 23:25:55.807094,36
3.2171991455,4,2016-05-12 23:26:00.811195,41
2.84207576865,1,2016-05-12 23:26:05.817335,42
0.663615496659,0,2016-05-12 23:26:10.824400,40
0.539331401029,4,2016-05-12 23:26:15.832425,45
2.75406945756,3,2016-05-12 23:26:20.838290,37
4.43965739451,1,2016-05-12 23:26:25.843248,45
2.10214341198,5,2016-05-12 23:26:30.845823,39
3.50234581533,3,2016-05-12 23:26:35.852271,38
3.45291471118,0,2016-05-12 23:26:40.860254,36
3.5884966112,3,2016-05-12 23:26:45.866042,36
3.65562336218,2,2016-05-12 23:26:50.870163,36
3.22787492289,0,2016-05-12 23:26:55.874997,41
1.41590509835,2,2016-05-12 23:27:00.879532,36
2.48730121526,5,2016-05-12 23:27:05.882013,44
3.5854412735,3,2016-05-12 23:27:10.886479,36
3.53958020616,2,2016-05-12 23:27:15.891185,41
2.77574896183,5,2016-05-12 23:27:20.897460,42
0.830350768942,2,2016-05-12 23:27:25.900477,38
0.728109268493,3,2016-05-12 23:27:30.904629,45
0.0431325167329,1,2016-05-12 23:27:35.911019,35
1.29994090977,2,2016-05-12 23:27:40.916800,42
3.11665454833,2,2016-05-12 23:27:45.924227,41
2.57592465402,4,2016-05-12 23:27:50.927812,39
0.964683161203,1,2016-05-12 23:27:55.930184,40
2.15761978036,0,2016-05-12 23:28:00.934962,43
0.924057341522,3,2016-05-12 23:28:05.937863,38
1.62350364078,3,2016-05-12 23:28:10.941128,38
2.64453892738,4,2016-05-12 23:28:15.944673,39
1.49441604039,1,2016-05-12 23:28:20.950785,45
1.58813945949,3,2016-05-12 23:28:25.953273,43
3.58994181694,5,2016-05-12 23:28:30.957330,36
2.71347875943,4,2016-05-12 23:28:35.959811,44
4.37068620994,3,2016-05-12 23:28:40.964196,37
3.90957861683,1,2016-05-12 23:28:45.968286,36
3.30131998385,4,2016-05-12 23:28:50.973618,35
3.11243031866,2,2016-05-12 23:28:55.978291,44
1.32775843109,5,2016-05-12 23:29:00.983261,37
1.23837808118,5,2016-05-12 23:29:05.986383,38
4.46897008153,1,2016-05-12 23:29:10.987805,43
3.13684365015,4,2016-05-12 23:29:15.993875,39
2.01812010967,5,2016-05-12 23:29:21.001063,36
2.12528013373,1,2016-05-12 23:29:26.006033,40
1.43452545128,5,2016-05-12 23:29:31.013605,38
2.08740379047,3,2016-05-12 23:29:36.017600,43
4.57696773921,2,2016-05-12 23:29:41.021899,40
1.03306787163,1,2016-05-12 23:29:46.024928,35
3.2272839842,4,2016-05-12 23:29:51.031579,45
1.68634554966,4,2016-05-12 23:29:56.037648,43
0.441779669793,2,2016-05-12 23:30:01.041656,35
2.91542298743,1,2016-05-12 23:30:06.046922,39
0.304226758391,0,2016-05-12 23:30:11.049347,39
4.43416819417,5,2016-05-12 23:30:16.059303,44
3.30999760719,4,2016-05-12 23:30:21.063112,43
4.19809941735,0,2016-05-12 23:30:26.065976,40
4.06351489593,0,2016-05-12 23:30:31.072202,45
4.14919538557,0,2016-05-12 23:30:36.076148,44
2.3430754765,0,2016-05-12 23:30:41.082216,45
1.5543139471,0,2016-05-12 23:30:46.085454,45
3.73283808585,1,2016-05-12 23:30:51.091395,36
1.76122760279,4,2016-05-12 23:30:56.095649,38
3.37782838216,5,2016-05-12 23:31:01.101228,42
2.98266594093,3,2016-05-12 23:31:06.103600,44
4.76840785712,3,2016-05-12 23:31:11.106023,42
0.118341525223,1,2016-05-12 23:31:16.112656,35
3.88472859103,2,2016-05-12 23:31:21.116763,35
2.91147965789,4,2016-05-12 23:31:26.119859,35
1.02994048262,0,2016-05-12 23:31:31.126141,36
2.80853346717,1,2016-05-12 23:31:36.130399,37
1.89844720536,2,2016-05-12 23:31:41.133569,44
0.645164445926,5,2016-05-12 23:31:46.139605,40
4.13181021743,1,2016-05-12 23:31:51.144010,42
1.38886765769,4,2016-05-12 23:31:56.149554,42
4.46075795239,1,2016-05-12 23:32:01.151956,42
0.0161281814299,3,2016-05-12 23:32:06.154473,36
2.51406746817,2,2016-05-12 23:32:11.159271,41
2.44782341223,2,2016-05-12 23:32:16.163022,42
4.16062237341,4,2016-05-12 23:32:21.168418,37
4.82563803264,3,2016-05-12 23:32:26.174845,43
1.72404477521,2,2016-05-12 23:32:31.178589,37
2.06088600404,3,2016-05-12 23:32:36.183520,43
0.336933483926,4,2016-05-12 23:32:41.186484,45
3.66951231336,5,2016-05-12 23:32:46.191576,40
4.65831908378,1,2016-05-12 23:32:51.197907,45
1.55891220203,5,2016-05-12 23:32:56.203949,36
2.61400606286,4,2016-05-12 23:33:01.210546,41
1.58520693337,5,2016-05-12 23:33:06.217256,42
3.06524041955,4,2016-05-12 23:33:11.226025,40
1.36621647848,3,2016-05-12 23:33:16.228746,36
2.37449884796,1,2016-05-12 23:33:21.230968,35
1.84247008046,4,2016-05-12 23:33:26.234731,39
1.56894058671,0,2016-05-12 23:33:31.238073,44
4.15079334635,4,2016-05-12 23:33:36.244388,41
1.36635308854,1,2016-05-12 23:33:41.250904,43
3.38657823306,1,2016-05-12 23:33:46.258122,35
2.94423698458,0,2016-05-12 23:33:51.263021,38
3.91103718898,2,2016-05-12 23:33:56.266863,44
0.947081101473,4,2016-05-12 23:34:01.269982,42
1.9175379801,5,2016-05-12 23:34:06.274912,40
1.59905344793,5,2016-05-12 23:34:11.278773,41
3.53986590013,3,2016-05-12 23:34:16.282237,36
0.796223945879,0,2016-05-12 23:34:21.285357,40
0.128981281842,4,2016-05-12 23:34:26.288015,45
4.62803799363,1,2016-05-12 23:34:31.290695,35
4.43346229805,3,2016-05-12 23:34:36.296621,41
2.41451962642,2,2016-05-12 23:34:41.302857,39
3.13372267743,5,2016-05-12 23:34:46.305283,35
1.22951938405,0,2016-05-12 23:34:51.308251,44
4.29165875592,1,2016-05-12 23:34:56.314068,40
4.27079788955,3,2016-05-12 23:35:01.317304,44
1.71781164219,1,2016-05-12 23:35:06.323649,39
3.77897065451,1,2016-05-12 23:35:11.330295,39
3.92440209182,4,2016-05-12 23:35:16.334997,41
3.39765128342,2,2016-05-12 23:35:21.336787,35
0.5386515079,1,2016-05-12 23:35:26.340081,35
0.900495727373,5,2016-05-12 23:35:31.347344,44
1.39710135532,5,2016-05-12 23:35:36.358253,43
2.03862781869,0,2016-05-12 23:35:41.363536,37
2.28247940788,3,2016-05-12 23:35:46.365710,40
1.79413983819,5,2016-05-12 23:35:51.371357,39
0.988342902167,4,2016-05-12 23:35:56.374190,39
1.55285447017,4,2016-05-12 23:36:01.379697,45
1.48681992044,2,2016-05-12 23:36:06.382812,39
4.73734188844,5,2016-05-12 23:36:11.384766,44
1.81887606368,0,2016-05-12 23:36:16.386443,36
1.11882944872,4,2016-05-12 23:36:21.390189,43
3.40766552407,2,2016-05-12 23:36:26.392470,39
4.0326784975,5,2016-05-12 23:36:31.396774,45
0.324220578822,3,2016-05-12 23:36:36.403430,38
4.4183973908,0,2016-05-12 23:36:41.405991,37
0.898052879899,1,2016-05-12 23:36:46.411847,43
2.1450659604,3,2016-05-12 23:36:51.415124,40
2.77950167393,4,2016-05-12 23:36:56.420699,36
0.227086457568,0,2016-05-12 23:37:01.424131,41
1.06413279592,1,2016-05-12 23:37:06.426334,44
3.40810246487,2,2016-05-12 23:37:11.427850,43
3.46208507874,1,2016-05-12 23:37:16.432462,41
3.18311726207,0,2016-05-12 23:37:21.434999,44
1.26297911535,2,2016-05-12 23:37:26.441485,40
0.801906420828,4,2016-05-12 23:37:31.443628,42
2.62426160697,5,2016-05-12 23:37:36.450376,41
3.80115948656,5,2016-05-12 23:37:41.457528,39
2.87425257227,2,2016-05-12 23:37:46.462563,35
3.81443822223,1,2016-05-12 23:37:51.464612,37
3.25089024909,0,2016-05-12 23:37:56.470871,39
2.44382844939,1,2016-05-12 23:38:01.476682,35
4.97732113633,0,2016-05-12 23:38:06.481253,44
3.23102418521,0,2016-05-12 23:38:11.487878,43
3.8533439625,3,2016-05-12 23:38:16.492952,45
3.43223606542,1,2016-05-12 23:38:21.495826,43
2.35708896232,4,2016-05-12 23:38:26.501183,43
0.889682177306,3,2016-05-12 23:38:31.503316,43
0.112462473116,1,2016-05-12 23:38:36.509301,44
3.8091789857,2,2016-05-12 23:38:41.515647,38
0.794199382745,0,2016-05-12 23:38:46.518328,44
0.296058152915,2,2016-05-12 23:38:51.520595,42
1.21571404988,4,2016-05-12 23:38:56.525308,41
3.12487520598,4,2016-05-12 23:39:01.529515,36
3.1630879871,0,2016-05-12 23:39:06.537071,40
2.63931036065,5,2016-05-12 23:39:11.541608,39
0.307911255088,4,2016-05-12 23:39:16.544792,36
0.0963940504703,4,2016-05-12 23:39:21.549359,43
3.82308993562,2,2016-05-12 23:39:26.556561,35
4.09701798116,5,2016-05-12 23:39:31.563781,35
2.87064461748,0,2016-05-12 23:39:36.568958,42
1.95455396952,3,2016-05-12 23:39:41.572651,39
0.920004008442,3,2016-05-12 23:39:46.578196,39
0.928569086084,4,2016-05-12 23:39:51.584741,36
1.37314931398,5,2016-05-12 23:39:56.588741,43
0.792363555148,3,2016-05-12 23:40:01.591254,38
2.90441826035,3,2016-05-12 23:40:06.597906,37
2.10009740908,4,2016-05-12 23:40:11.604619,36
1.56705656264,2,2016-05-12 23:40:16.609681,43
4.80527534883,3,2016-05-12 23:40:21.612282,38
1.05137039422,0,2016-05-12 23:40:26.617741,38
3.04062988982,4,2016-05-12 23:40:31.621245,35
0.124798249858,5,2016-05-12 23:40:36.627883,36
3.17186402202,0,2016-05-12 23:40:41.635052,43
1.34972906951,0,2016-05-12 23:40:46.637327,40
0.3016332446,5,2016-05-12 23:40:51.644432,39
0.587810200385,1,2016-05-12 23:40:56.650179,39
2.91332780352,2,2016-05-12 23:41:01.655583,44
4.15879612032,5,2016-05-12 23:41:06.662581,44
0.872224900955,0,2016-05-12 23:41:11.667769,43
2.9564468271,1,2016-05-12 23:41:16.671603,38
4.68496153471,2,2016-05-12 23:41:21.675555,35
2.51145065236,1,2016-05-12 23:41:26.677765,36
1.22537077148,5,2016-05-12 23:41:31.683128,44
3.46403614841,0,2016-05-12 23:41:36.685319,41
3.93495451465,0,2016-05-12 23:41:41.687917,38
3.82092036343,0,2016-05-12 23:41:46.692837,45
2.87738712758,2,2016-05-12 23:41:51.695041,45
4.02280443316,4,2016-05-12 23:41:56.700016,45
2.96008556093,1,2016-05-12 23:42:01.704191,42
0.564406001147,0,2016-05-12 23:42:06.709935,35
3.61047449987,4,2016-05-12 23:42:11.714682,40
2.79236656838,5,2016-05-12 23:42:16.718696,45
3.68651988001,5,2016-05-12 23:42:21.725047,39
2.5004377119,1,2016-05-12 23:42:26.729875,36
2.73475418108,3,2016-05-12 23:42:31.733702,35
4.5982324042,2,2016-05-12 23:42:36.735892,38
1.09109486404,3,2016-05-12 23:42:41.739704,39
4.46092978806,3,2016-05-12 23:42:46.744176,39
1.93063100319,4,2016-05-12 23:42:51.748592,37
4.59415446382,0,2016-05-12 23:42:56.752773,38
2.42545393571,2,2016-05-12 23:43:01.758139,40
3.94963538747,1,2016-05-12 23:43:06.763833,43
0.730392346697,4,2016-05-12 23:43:11.769030,41
4.06037615347,2,2016-05-12 23:43:16.773695,37
1.63680596554,2,2016-05-12 23:43:21.776506,42
2.25324035049,1,2016-05-12 23:43:26.782699,36
0.89725969193,1,2016-05-12 23:43:31.788904,35
0.5493556177,5,2016-05-12 23:43:36.792766,41
0.901895502446,3,2016-05-12 23:43:41.795403,40
3.71821185129,0,2016-05-12 23:43:46.796904,35
0.750882629935,3,2016-05-12 23:43:51.800302,44
1.80101705723,3,2016-05-12 23:43:56.802311,39
3.74225198056,5,2016-05-12 23:44:01.807798,43
4.18553996476,4,2016-05-12 23:44:06.810276,43
2.74832684461,5,2016-05-12 23:44:11.814900,44
4.07074954552,2,2016-05-12 23:44:16.817187,36
3.64904853435,0,2016-05-12 23:44:21.819078,42
2.26219100962,3,2016-05-12 23:44:26.822836,44
