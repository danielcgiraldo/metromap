/* V1 */

DROP TABLE IF EXISTS LINE;
CREATE TABLE LINE(
    id CHAR(1),
    status ENUM('O', 'P', 'M', 'U') NOT NULL COMMENT 'status must be: O, P, M, U: operational, partial outage, major outage, under maintenance.',
    color CHAR(6) NOT NULL COMMENT 'HEX code of the color',
    type ENUM('M', 'C', 'TB', 'B') NOT NULL COMMENT 'type must be: M, C, TB, B: metro, cable, trolley and electric bus, bus.',
    CONSTRAINT pk_line 
        PRIMARY KEY (id)
);

DROP TABLE IF EXISTS STATION;
CREATE TABLE STATION(
    line CHAR(1) COMMENT 'FK of line(id)',
    id VARCHAR(40) NOT NULL,
    sites_of_interest JSON NULL,
    services JSON NULL,
    status ENUM('O', 'P', 'M', 'U') NOT NULL COMMENT 'status must be: O, P, M, U: operational, partial outage (closed station with transit), major outage, under maintenance.',
    CONSTRAINT fk1
        FOREIGN KEY(line)
            REFERENCES LINE(id)
                ON UPDATE CASCADE
                ON DELETE RESTRICT,
    CONSTRAINT pk_station
        PRIMARY KEY(line, id)
);

DROP TABLE IF EXISTS ALIAS;
CREATE TABLE ALIAS(
    alternate VARCHAR(100) COMMENT 'Name of the station',
    line CHAR(1) COMMENT 'FK of STATION(line)',
    station VARCHAR(40) COMMENT 'FK of STATION(id)',
    CONSTRAINT fk2
        FOREIGN KEY(line, station)
            REFERENCES STATION(line, id)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
    CONSTRAINT pk_alias
        PRIMARY KEY(alternate, line, station)
);

DROP TABLE IF EXISTS INCIDENT;
CREATE TABLE INCIDENT(
    id varchar(20) COMMENT 'incident number #:',
    status ENUM('0','1') NOT NULL COMMENT 'status must be either 1 Open or 0 Closed',
    CONSTRAINT pk_incident
        PRIMARY KEY (id)
);

DROP TABLE IF EXISTS AFFECTED_STATION;
CREATE TABLE AFFECTED_STATION(
    incident varchar(20) COMMENT 'FK of INCIDENT(id)',
    line CHAR(1) COMMENT 'FK of STATION(line)',
    station varchar(40) COMMENT 'FK of STATION(id)',
    CONSTRAINT pk_line 
        PRIMARY KEY (line, station, incident),
    CONSTRAINT fk3
        FOREIGN KEY (incident)
            REFERENCES INCIDENT(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
    CONSTRAINT fk4
        FOREIGN KEY (line, station)
            REFERENCES STATION(line, id)
                ON UPDATE CASCADE
                ON DELETE CASCADE
);

DROP TABLE IF EXISTS NOTIFICATION;
CREATE TABLE NOTIFICATION(
    tweet_id varchar(40) COMMENT 'id of the tweet to fetch content',
    incident varchar(20) NOT NULL COMMENT 'FK of INCIDENT(id)',
    date DATETIME NOT NULL COMMENT 'Includes both date and hour format',
    CONSTRAINT pk_notification
        PRIMARY KEY (tweet_id),
    CONSTRAINT fk5
        FOREIGN KEY (incident)
            REFERENCES INCIDENT(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE
);


DROP TABLE IF EXISTS REPORT;
CREATE TABLE REPORT(
    id VARCHAR(40),
    title VARCHAR(100) NOT NULL COMMENT 'title of the report',
    type ENUM('V', 'S', 'L', 'C', 'W') NOT NULL COMMENT 'type must be: V, S, L, C, W: vehicles, stations, lines, contact means, webpage.',
    description VARCHAR(250) NULL COMMENT 'description of the report',
    date DATETIME NOT NULL COMMENT 'date and time the report was uploaded',
    CONSTRAINT pk_report
        PRIMARY KEY (id)
);

DROP TABLE IF EXISTS USER;
CREATE TABLE USER(
    email VARCHAR(100) COMMENT 'email of the user',
    pwd VARCHAR(100) NOT NULL COMMENT 'password of the user',
    name VARCHAR(50) NOT NULL COMMENT 'name of the user',
    status ENUM('1', '0') NOT NULL COMMENT 'status must be: 1, 0: active, banned.',
    credits INT(4) NOT NULL COMMENT 'number of credits of the user, credits is used to limit the amount of request to the API. Resets every month to 40.',
    secret_key VARCHAR(100) UNIQUE COMMENT 'not public key of the user, is a unique alternative identifiers',
    public_key VARCHAR(100) UNIQUE COMMENT 'public key of the user, is a unique alternative identifiers',
    allowed_domains JSON NOT NULL COMMENT 'domains to which the user has access',
    CONSTRAINT pk_user
        PRIMARY KEY (email)
);