#!/bin/bash

echo "Start initialization of flask app."

if [[ $(find -name "requirements.txt") ]]
then
  echo "Installing requirements"
  pip install -r requirements.txt
else
  echo "File with python package requirements doesn't exists"
fi

echo "Setup Flask DB..."
flask setup-db

echo "Creating tables..."
flask create-table

echo "Running application..."
flask run
