USE Apps;
SELECT * FROM Ratings;
LOAD DATA LOCAL INFILE '/home/iudh/Documentos/IronHack/prework/03-MySQL/apple_store.csv' REPLACE INTO TABLE Ratings 
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
INTO TABLE Ratings;
SELECT * FROM Ratings;