#!/usr/bin/env bash
alembic upgrade 874c17f78d9d
wait $! 
python seeder.py