CREATE DATABASE burgercollector;

CREATE USER burger_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE burgercollector TO burger_admin;

