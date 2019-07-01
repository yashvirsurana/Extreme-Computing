hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
	-input /user/$USER/ex1/webLarge.txt \
	-output /user/$USER/assignment1/task1 \
	-mapper mapper.py \
	-file mapper.py 
