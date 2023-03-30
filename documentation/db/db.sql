DROP TABLE IF EXISTS LINE;
CREATE TABLE LINE(
    id CHAR(1) NOT NULL,
    status ENUM('O', 'P', 'M', 'U') NOT NULL COMMENT 'status must be: O, P, M, U: operational, partial outage, major outage, under maintenance.',
    color CHAR(6) NOT NULL COMMENT 'HEX code of the color',
    type ENUM('M', 'C', 'TB', 'B') NOT NULL COMMENT 'type must be: M, C, TB, B: metro, cable, trolley and electric bus, bus.'
);
