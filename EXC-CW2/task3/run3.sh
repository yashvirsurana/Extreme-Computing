hdfs dfs -rm -r /user/s1368177/ex2/task3trial

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
	-D mapreduce.job.reduces=1 \
	-D mapreduce.partition.keycomparator.options=-k1n \
	-input /data/assignments/ex2/part2/stackSmall.txt \
	-output /user/s1368177/ex2/task3trial \
	-mapper mapper.py \
	-file mapper.py \
	-combiner combiner.py \
	-file combiner.py \
	-reducer reducer.py \
	-file reducer.py