-- Task 6.States table
-- script that creates the database hbtn_0d_usa and the table states (in hbtn_0d_usa)
-- Description: id INT unique, auto generated (can`t be null & is primary key,
-- cont... description: name VARCHAR (256)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
	);
