DROP TABLE IF EXISTS LINE;
CREATE TABLE LINE(
    id CHAR(1) NOT NULL,
    status ENUM('O', 'P', 'M', 'U') NOT NULL COMMENT 'status must be: O, P, M, U: operational, partial outage, major outage, under maintenance.',
    color CHAR(6) NOT NULL COMMENT 'HEX code of the color',
    type ENUM('M', 'C', 'TB', 'B') NOT NULL COMMENT 'type must be: M, C, TB, B: metro, cable, trolley and electric bus, bus.'
);

DROP TABLE IF EXISTS STATION;
CREATE TABLE STATION(
    line CHAR(1) NOT NULL COMMENT 'FK of line(id)',
    id VARCHAR(40) NOT NULL,
    sites_of_interest JSON NULL,
    services JSON NULL,
    status ENUM('O', 'P', 'M', 'U') NOT NULL COMMENT 'status must be: O, P, M, U: operational, partial outage (closed station with transit), major outage, under maintenance.'
);

DROP TABLE IF EXISTS ALIAS;
CREATE TABLE ALIAS(
    station VARCHAR(40) NOT NULL COMMENT 'FK of station(id)',
    alternate VARCHAR(100) NOT NULL COMMENT 'Name of the station'
);

DROP TABLE IF EXISTS REPORT;
CREATE TABLE REPORT(
    id VARCHAR(40) NOT NULL,
    title VARCHAR(100) NOT NULL COMMENT 'title of the report',
    type ENUM('V', 'S', 'L', 'C', 'W') NOT NULL COMMENT 'type must be: V, S, L, C, W: vehicles, stations, lines, contact means, webpage.',
    description VARCHAR(250) NULL COMMENT 'description of the report',
    date DATETIME NOT NULL COMMENT 'date and time the report was uploaded'
);

DROP TABLE IF EXISTS USER;
CREATE TABLE USER(
    email VARCHAR(100) NOT NULL COMMENT 'email of the user',
    pwd VARCHAR(100) NOT NULL COMMENT 'password of the user',
    name VARCHAR(50) NOT NULL COMMENT 'name of the user',
    status ENUM('1', '0') NOT NULL COMMENT 'status must be: 1, 0: active, banned.',
    credits INT(4) NOT NULL COMMENT 'number of credits of the user, credits is used to limit the amount of request to the API. Resets every month to 40.',
    secret_key VARCHAR(100) NOT NULL COMMENT 'not public key of the user, is a unique alternative identifiers',
    public_key VARCHAR(100) NOT NULL COMMENT 'public key of the user, is a unique alternative identifiers',
    allowed_domains JSON NOT NULL COMMENT 'domains to which the user has access'
);