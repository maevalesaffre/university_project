all: doc station_velo.jar

doc:
	# génération de la documentation
	javadoc -sourcepath src -d doc -subpackages vehicle main observer strategy worker exceptions

cls:
	# compilation des classes
	javac -sourcepath src -d classes ./src/main/*.java ./src/exceptions/*.java  ./src/observer/*.java ./src/strategy/*.java ./src/vehicle/*.java ./src/vehicle/bike/*.java ./src/vehicle/bike/bikeDecorator/*.java ./src/exceptions/*.java ./src/worker/*.java

test: cls
	# tests
	javac -d classes -classpath ./lib/junit-console.jar ./src/main/*.java ./src/observer/*.java ./src/strategy/*.java ./src/vehicle/*.java ./src/vehicle/bike/*.java ./src/vehicle/bike/bikeDecorator/*.java ./src/exceptions/*.java ./src/worker/*.java ./test/worker/*.java ./test/vehicle/bike/bikeDecorator/*.java ./test/strategy/*.java ./test/observer/*.java
	java -jar ./lib/junit-console.jar -cp classes --scan-classpath --disable-banner

station_velo.jar: cls
	# construction du jar
	jar cvfe station_velo.jar main.Main -C classes main -C classes exceptions -C classes vehicle -C classes observer -C classes strategy -C classes worker
	mkdir jar
	mv station_velo.jar jar

station_velo:
	# execution du jar
	java -jar jar/station_velo.jar


clean:
	# nettoyage des fichiers
	rm -r doc classes jar
