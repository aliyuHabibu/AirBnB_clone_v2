-- Prepares a MySQL server for the project

-- Create a new test database
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- Create a new user
CREATE USER IF NOT EXISTS `hbnb_test`@`localhost` IDENTIFIED BY "hbnb_test_pwd";

-- Grant privileges to new user
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO `hbnb_test`@`localhost`;

-- Grant new user read permission to the performace schema
GRANT SELECT ON `performance_schema`.* TO `hbnb_test`@`localhost`;
