-- Prepares a MySQL server for the project

-- Create the database
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

-- Create the new user
CREATE USER  IF NOT EXISTS `hbnb_dev`@`localhost` IDENTIFIED BY "hbnb_dev_pwd";

-- Grant privilege on the new database to the new user
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO `hbnb_dev`@`localhost`;

-- Grant read privilege on performance_schema
GRANT SELECT ON `performance_schema`.* TO `hbnb_dev`@`localhost`;


