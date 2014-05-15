#!/bin/sh
cat jive-turkey/requirements.txt | awk '{ system("flask/bin/pip install "$1) }'
