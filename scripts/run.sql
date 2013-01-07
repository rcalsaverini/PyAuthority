CREATE EXTERNAL TABLE rawResults
    (numAgents INT,
     alpha DOUBLE,
     beta DOUBLE,
     energy DOUBLE,
     avgDegree DOUBLE,
     maxDegree DOUBLE,
     accept DOUBLE)
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ' ' LINES TERMINATED BY '\n'
    STORED AS TEXTFILE LOCATION 's3://doutorado/results/';

CREATE EXTERNAL TABLE avgResults
    (numAgents INT,
     alpha DOUBLE,
     beta DOUBLE,
     energy DOUBLE,
     avgDegree DOUBLE,
     maxDegree DOUBLE,
     accept DOUBLE)
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ' ' LINES TERMINATED BY '\n'
    STORED AS TEXTFILE LOCATION 's3://doutorado/avgResults/';

CREATE EXTERNAL TABLE num
    (numAgents INT,
     alpha DOUBLE,
     beta DOUBLE,
     numResults INT)
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ' ' LINES TERMINATED BY '\n'
    STORED AS TEXTFILE LOCATION 's3://doutorado/resultCount/';

CREATE EXTERNAL TABLE stddevResults
    (numAgents INT,
     alpha DOUBLE,
     beta DOUBLE,
     energy DOUBLE,
     avgDegree DOUBLE,
     maxDegree DOUBLE,
     accept DOUBLE)
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ' ' LINES TERMINATED BY '\n'
    STORED AS TEXTFILE LOCATION 's3://doutorado/stddevResults/';

CREATE EXTERNAL TABLE percentilesResults05
    (numAgents INT,
     alpha DOUBLE,
     beta DOUBLE,
     energy05 DOUBLE,
     avgDegree05 DOUBLE,
     maxDegree05 DOUBLE,
     accept05 DOUBLE)
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ' ' LINES TERMINATED BY '\n'
    STORED AS TEXTFILE LOCATION 's3://doutorado/percentile05/';

CREATE EXTERNAL TABLE percentilesResults95
    (numAgents INT,
     alpha DOUBLE,
     beta DOUBLE,
     energy95 DOUBLE,
     avgDegree95 DOUBLE,
     maxDegree95 DOUBLE,
     accept95 DOUBLE)
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ' ' LINES TERMINATED BY '\n'
    STORED AS TEXTFILE LOCATION 's3://doutorado/percentile95/';

INSERT OVERWRITE TABLE num
SELECT numAgents, alpha, beta, count(*) FROM rawResults
GROUP BY numAgents, alpha, beta;

INSERT OVERWRITE TABLE avgResults
SELECT numAgents, alpha, beta, avg(energy), avg(avgDegree), avg(maxDegree), avg(accept) FROM rawResults
GROUP BY numAgents, alpha, beta;

INSERT OVERWRITE TABLE stddevResults
SELECT numAgents, alpha, beta, stddev_samp(energy), stddev_samp(avgDegree), stddev_samp(maxDegree), stddev_samp(accept) FROM rawResults
GROUP BY numAgents, alpha, beta;

INSERT OVERWRITE TABLE percentilesResults05
SELECT numAgents, alpha, beta, percentile_approx(energy, 0.05),
                               percentile_approx(avgDegree, 0.05),
                               percentile_approx(maxDegree, 0.05),
                               percentile_approx(accept, 0.05) FROM rawResults
GROUP BY numAgents, alpha, beta;

INSERT OVERWRITE TABLE percentilesResults95
SELECT numAgents, alpha, beta, percentile_approx(energy, 0.95),
                               percentile_approx(avgDegree, 0.95),
                               percentile_approx(maxDegree, 0.95),
                               percentile_approx(accept, 0.95) FROM rawResults
GROUP BY numAgents, alpha, beta;

