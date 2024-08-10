#!/bin/bash

# Change directory to the target location
cd /home/ubuntu/hluboka_reporting_api || exit

# Activate the virtual environment
source /home/ubuntu/areal_repo_api/venv/bin/activate

# Execute the Python script
python /home/ubuntu/hluboka_reporting_api/dummy_day_creation.py