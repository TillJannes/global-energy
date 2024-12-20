CREATE SCHEMA IF NOT EXISTS eschema;

CREATE TABLE IF NOT EXISTS eschema.conf_files(
    name TEXT,
    date_added DATE,
    description TEXT,
    path TEXT
);