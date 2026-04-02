#!/bin/bash
#---
# name: Blog UI
# description: Django development server
# http: 8000
#---
export PATH="$HOME/.local/bin:$PATH"
cd "$(dirname "$0")/../../"
python3 manage.py runserver 0.0.0.0:8000
