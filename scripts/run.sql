ADD JAR /home/hadoo/hive/contrib/hive-contrib-0.8.1.jar

CREATE EXTERNAL TABLE rawResults
    (numAgents STRING,
     alpha STRING,
     beta STRING,
     energy STRING,
     avgDegree STRING,
     maxDegree STRING,
     accept STRING)
    ROW FORMAT SERDE 'org.apache.hadoop.hive.contrib.serde2.RegexSerDe'
    WITH SERDEPROPERTIES(
        "input.regex" = "([\d|\.]+)\s+([\d|\.]+)\s+([\d|\.]+)\s+([\d|\.]+)\s+([\d|\.]+)\s+([\d|\.]+)\s+([\d|\.]+)",
        "output.format.string" = "%1$i %2$f %3$f %4$f %5$f %6$f")
    STORED AS TEXTFILE LOCATION 's3://doutorado/results/';

CREATE EXTERNAL TABLE avgResults
    (numAgents INT,
     alpha DOUBLE,
     beta DOUBLE,
     energy DOUBLE,
     avgDegree DOUBLE,
     maxDegree DOUBLE,
     accept DOUBLE)
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ' \t' LINES TERMINATED BY '\n'
    STORED AS TEXTFILE LOCATION 's3://doutorado/avgResults/';

INSERT OVERWRITE TABLE avgResults
SELECT numAgents, alpha, beta, avg(energy), avg(avgDegree), avg(maxDegree), avg(accept) FROM rawResults
GROUP BY numAgents, alpha, beta;

