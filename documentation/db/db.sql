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