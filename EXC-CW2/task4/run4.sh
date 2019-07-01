

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
	-D mapreduce.job.reduces=1 \
	-D mapreduce.partition.keycomparator.options=-k1n \
	-input /data/assignments/ex2/part2/stackLarge.txt \
	-output /user/$USER/ex2/task4temp \
	-mapper mapper.py \
	-file mapper.py \
	-reducer reducer.py \
	-file reducer.py

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
	-D mapreduce.job.reduces=1 \
	-D mapreduce.partition.keycomparator.options=-k1n \
	-input /user/$USER/ex2/task4temp/* \
	-output /user/s1368177/assignment2/task4 \
	-mapper mapper2.py \
	-file mapper2.py \
	-reducer reducer2.py \
	-file reducer2.py