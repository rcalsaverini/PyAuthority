CREATE EXTERNAL TABLE parameters
    (numAgents INT,
     alpha DOUBLE,
     beta DOUBLE,
     nsteps INT,
     burnin INT,
     thin INT)
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ' ' LINES TERMINATED BY '\n'
    STORED AS TEXTFILE LOCATION 's3://doutorado/parameters/';

CREATE EXTERNAL TABLE results
    (numAgents INT,
     alpha DOUBLE,
     beta DOUBLE,
     energy DOUBLE,
     avgDegree DOUBLE,
     maxDegree DOUBLE,
     accept DOUBLE)
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ' ' LINES TERMINATED BY '\n'
    STORED AS TEXTFILE LOCATION 's3://doutorado/results/'



FROM (
    MAP
        burnin, nsteps
    USING
        'echo'
    FROM
        parameters) map_out SELECT * ;

FROM
    (MAP
        numAgents, alpha, beta, burnin, nsteps, thin
     USING
        'runAuthorityMCMC' AS numAgents, alpha, beta, energy, avgDegree, maxDegree, accept
     FROM
        parameters
    ) map_output
INSERT OVERWRITE TABLE parameters SELECT *;

