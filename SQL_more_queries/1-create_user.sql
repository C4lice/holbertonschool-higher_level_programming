-- Create the user if it does not already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Give all privileges to *.*
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Apply privileges
FLUSH PRIVILEGES;