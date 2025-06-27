-- script that create the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (id),
    CONSTRAINT citie_in_state FOREIGN KEY (state_id) REFERENCES states(id)
);
