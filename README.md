Hadoop-Map-Reducer-using-AWS-Java-API
=====================================
http://dumps.wikimedia.org/other/pagecounts-raw/
This page contains page count files of Wikimedia from 2007 to 2013 on the monthly basis. This is terabyte of data. In this microtask, I used Amazon’s Map Reduce which in turn uses Google’s Hadoop system to analyze the big data. From the link below
pagecounts-20130601-000000.gz, I got the data of page count of 1 June, 2013.
This file contains very large data. Therefore, I take a small sample of data from this file, which you can find in input folder. I used python to maintain the analysis process. 
In a MapReduce program, data stored as Key/Value pairs, is processed by a Mapfunction. Mappers output a transformed set of key/value pairs, which are subsequently processed by a Reduce function. 
You can check the output in the out folder. Output data is divided into three files because Map reduces works on Master and Slave configuration. Master instance divides the whole task into slave instance. This will select only lines starts from ‘en’. This way we can get any sort of data out of the file by splitting every line into sub parts. 
