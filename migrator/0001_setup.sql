CREATE SCHEMA IF NOT EXISTS eschema;

CREATE TABLE IF NOT EXISTS eschema.conf_files(
    id SERIAL PRIMARY KEY,
    name TEXT,
    date_added DATE,
    description TEXT,
    path TEXT
);
