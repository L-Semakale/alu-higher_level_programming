-- a script that creates the table unique_id on your MySQL server
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT VALUE 1 UNIQUE, name VARCHAR(256))
