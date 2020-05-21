#!/bin/bash

kubectl proxy --port=8080 &
sudo python3 app.py &
