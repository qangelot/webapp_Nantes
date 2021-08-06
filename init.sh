#!/bin/bash
set -e

echo "Starting SSH server..."
service ssh start

gunicorn wsgy:app -b :5000 
