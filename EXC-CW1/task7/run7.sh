

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
	-input /user/$USER/ex1/uniLarge.txt \
	-output /user/$USER/assignment1/task7 \
	-mapper mapper.py \
	-file mapper.py \
	-reducer reducer.py \
	-file reducer.py