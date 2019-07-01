

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
	-D mapreduce.job.reduces=1 \
	-input /user/$USER/assignment1/task7 \
	-output /user/$USER/assignment1/task8 \
	-mapper mapper.py \
	-file mapper.py \
	-reducer reducer.py \
	-file reducer.py