CREATE TABLE IF NOT EXISTS traffic
(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    HTTPCount INTEGER NOT NULL,
    FTPCount INTEGER NOT NULL,
    SSHCount INTEGER NOT NULL,
    SSDPCount INTEGER NOT NULL,
    SMTPCount INTEGER NOT NULL,
    DHCPCount INTEGER NOT NULL,
    POPCount INTEGER NOT NULL,
    MISCCount INTEGER NOT NULL
);