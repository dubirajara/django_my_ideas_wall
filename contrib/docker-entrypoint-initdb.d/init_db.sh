#!/bin/env bash
psql -U postgres -c "CREATE USER postgresuser PASSWORD 'postgrespass'"
psql -U postgres -c "ALTER USER postgresuser WITH SUPERUSER"
psql -U postgres -c "CREATE DATABASE ideasdb OWNER postgresuser"
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE ideasdb TO postgresuser;"
