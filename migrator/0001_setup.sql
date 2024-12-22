CREATE SCHEMA IF NOT EXISTS e_schema;

CREATE TABLE IF NOT EXISTS e_schema.consumers(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(200)
);
