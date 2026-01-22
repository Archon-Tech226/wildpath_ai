#!/bin/bash

# ------------------------------
# Build script for Django project
# ------------------------------

# Exit immediately if any command fails
set -e

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Running Django migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build complete!"
