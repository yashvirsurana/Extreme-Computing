
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
	-input /data/assignments/ex2/part1/large/* \
	-output /user/s1368177/assignment2/task1 \
	-mapper mapper.py \
	-file mapper.py \
	-combiner combiner.py \
	-file combiner.py \
	-reducer reducer.py \
	-file reducer.py